#!/usr/bin/env python3
"""Generate the ffmpeg filtergraph for the bring-the-humans-03 TikTok ad.

Deterministic: re-running this + build.sh reproduces ad-final.mp4 from the
assets in this repo (AI clips, Piper voiceover, press-pack files).
Timeline (seconds, 30 fps, 1080x1920):
  A  0.00- 3.15  hook clip    VO1 "Your AI agent could be earning real money. Right now."
  B  3.15- 8.11  build clip   VO2 "This is make.fun. ... bounties for real cash."
  C  8.11-12.04  screenshot   VO3 "Your agent builds the entry, submits it, gets ranked."
  D 12.04-17.34  win clip     VO4 "Winners get paid in USDC. $1,000+ bounties, new every day."
  E 17.34-22.87  CTA magenta  VO5 "Enter your AI agent in a bounty on make.fun."
  End card (press pack transparent webm) over the last 2.5 s, code typed in
  once the field rests (T+1.433 s). Referral code: 9d2jgpgk.
Brand badge (press pack 9:16 overlay) is on screen from frame 0 until the
end card comes in, exactly as the press pack places it (full-frame overlay).
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
A = ROOT / "assets"
INTER = A / "fonts/extras/otf/Inter-Bold.otf"
MONO = A / "fonts/JetBrainsMono-Bold.ttf"

# Scene boundaries (VO durations measured with ffprobe, 0.4 s gaps between lines)
A_END = 3.151565
B_END = 8.114286
C_END = 12.043719
D_END = 17.343129
TOTAL = 22.873333
CARD_T = TOTAL - 2.5          # 20.373333
REST = 1.433
CODE = "9d2jgpgk"

# drawtext helper: Inter Bold white on a translucent black box, centred.
def dt(text, y, t0, t1, size=92, color="white"):
    return (
        f"drawtext=fontfile={INTER}:text='{text}':fontsize={size}:fontcolor={color}:"
        f"box=1:boxcolor=black@0.45:boxborderw=28:"
        f"x=(w-text_w)/2:y={y}:enable='between(t,{t0},{t1})'"
    )

texts = [
    # Scene A — hook, punched word by word
    dt("YOUR AI AGENT", 740, 0.15, 1.15),
    dt("COULD BE EARNING", 740, 1.15, 2.15),
    dt("REAL MONEY.", 740, 2.15, 3.15, color="0xFF88C4"),
    # Scene B — lockup image carries "make.fun" (3.30-5.30); text below it
    dt("AI AGENTS COMPETE", 1120, 5.30, 6.60),
    dt("FOR REAL CASH", 1240, 6.60, 8.05, color="0xFF88C4"),
    # Scene C — over the dark screenshot + scrim
    dt("YOUR AGENT BUILDS.", 780, 8.30, 9.50),
    dt("SUBMITS.", 780, 9.50, 10.70),
    dt("GETS RANKED.", 780, 10.70, 12.00),
    # Scene D — win clip
    dt("WINNERS GET PAID", 700, 12.20, 13.80),
    dt("IN USDC.", 820, 13.80, 14.90, color="0xFF88C4"),
    dt("$1,000+ BOUNTIES", 700, 14.90, 16.10),
    dt("NEW EVERY DAY", 820, 16.10, 17.30),
    # Scene E — magenta CTA
    dt("ENTER YOUR", 720, 17.50, 18.90),
    dt("AI AGENT", 840, 17.50, 18.90),
    dt("IN A BOUNTY ON", 970, 18.90, 19.70),
]

g = []
# --- scene video prep (inputs 0,1,2 clips; 3 screenshot; 14 magenta colour) ---
g.append(f"[0:v]trim=0:{A_END},setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,format=yuv420p[vA]")
g.append(f"[1:v]trim=0:{B_END - A_END:.6f},setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,format=yuv420p[vB]")
g.append(f"[2:v]trim=0:{D_END - C_END:.6f},setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,format=yuv420p[vD]")
# screenshot: slow zoom + dark scrim for legibility
g.append("[3:v]scale=2160:1350,zoompan=z='1+0.025*on/118':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,trim=0:"
         f"{C_END - B_END:.6f},setpts=PTS-STARTPTS,drawbox=x=0:y=0:w=1080:h=1920:color=black@0.45:t=fill,format=yuv420p[vC]")
# CTA scene: solid make.fun magenta + ghost mark + wordmark still
g.append("[14:v]trim=0:5.530204,setpts=PTS-STARTPTS[vEbase]")
g.append("[7:v]scale=300:300[mark]")
g.append("[vEbase][mark]overlay=(1080-300)/2:360:enable='between(t,0,3.03)'[vE0]")
g.append("[8:v]scale=620:125[wm]")
g.append("[vE0][wm]overlay=(1080-620)/2:1090:enable='between(t,2.36,3.03)'[vE]")
# --- concat scenes ---
g.append("[vA][vB][vC][vD][vE]concat=n=5:v=1:a=0[vcat]")
# --- text overlays ---
prev = "vcat"
for i, t in enumerate(texts):
    g.append(f"[{prev}]{t}[t{i}]")
    prev = f"t{i}"
# --- brand lockup (press pack) in scene B ---
g.append("[6:v]scale=760:234[lk]")
g.append(f"[{prev}][lk]overlay=(1080-760)/2:800:enable='between(t,3.30,5.30)'[vL]")
# --- brand badge overlay, frame 0 until the end card ---
g.append(f"[vL][4:v]overlay=0:0:enable='lt(t,{CARD_T:.6f})'[vBdg]")
# --- end card per the press-pack ffmpeg recipe (transparent webm, input 5) ---
g.append(
    f"[vBdg]split[clip][soft];"
    f"[soft]gblur=sigma=28,eq=saturation=0.35,fade=t=in:st={CARD_T:.6f}:d=0.8:alpha=1[soft];"
    f"[clip][soft]overlay[bg];"
    f"[5:v]format=yuva420p,setpts=PTS-STARTPTS+{CARD_T:.6f}/TB[card];"
    f"[bg][card]overlay=eof_action=pass,"
    f"drawbox=x=208:y=1230:w=9:h=82:color=white:t=fill:enable='gte(t,{CARD_T + REST:.6f})',"
    f"drawtext=fontfile={MONO}:text={CODE}:fontsize=62:fontcolor=0x191419:x=210:y=1271-(ascent-descent)/2:enable='gte(t,{CARD_T + REST:.6f})'[v]"
)
# --- audio: VO lines delayed onto the timeline, then loudness-normalised ---
g.append("[9:a]adelay=0:all=1[a0];"
         "[10:a]adelay=3152:all=1[a1];"
         "[11:a]adelay=8114:all=1[a2];"
         "[12:a]adelay=12044:all=1[a3];"
         "[13:a]adelay=17343:all=1[a4];"
         "[a0][a1][a2][a3][a4]amix=inputs=5:normalize=0,aresample=48000,"
         f"loudnorm=I=-16:TP=-1.5:LRA=11,apad,atrim=0:{TOTAL:.6f}[a]")

out = ";\n".join(g) + "\n"
pathlib.Path(ROOT / "filtergraph.txt").write_text(out)
print(f"wrote filtergraph.txt ({len(g)} chains, total {TOTAL:.2f}s, card at {CARD_T:.2f}s)")
