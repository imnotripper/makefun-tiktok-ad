#!/usr/bin/env python3
"""Render ad-final-v3.mp4 for bring-the-humans-03.

All footage is new for v3:
- Scene 1: fresh generated still (orange desk robot) + Ken Burns move.
- Scene 2: terminal/editor animation drawn from scratch with PIL.
- Scene 3: fresh generated still (overhead workbench) + Ken Burns move.
- Scene 4: confetti celebration drawn from scratch with PIL, using the
  press-pack ghost mark.
- Scenes 5-6: brand cards built from press-pack art (same as v2 rules).
No frame is derived from the v1/v2 generated clips under assets/gen.
No money / earnings / prize / crypto / referral wording anywhere.
"""
import math
import random
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
BASE = "/home/hatch/workspace/makefun/bots/bring-the-humans-03"
FONT = f"{BASE}/assets/fonts/JetBrainsMono-Bold.ttf"
BADGE = Image.open(f"{BASE}/assets/press/badge-9x16.png").convert("RGBA")
MARK = Image.open(f"{BASE}/assets/press/kit/make-fun-press-kit/mark-on-dark-1024.png").convert("RGBA")

DESK = f"{BASE}/v3/gen/media-generation-bth03-v3-desk-0-9d48059e-372b-43b5-aba4-616a80016105.webp"
BUILD = f"{BASE}/v3/gen/media-generation-bth03-v3-build-0-a2c9f590-2f46-4dca-b6b4-aaafb0be36fd.webp"

MAGENTA = (194, 24, 143)
PINK = (241, 91, 158)
WHITE = (255, 255, 255)
DARK = (10, 10, 17)


def font(size):
    return ImageFont.truetype(FONT, size)


def cover(img, tw, th):
    """Resize+crop image to exactly cover tw x th."""
    iw, ih = img.size
    s = max(tw / iw, th / ih)
    img = img.resize((math.ceil(iw * s), math.ceil(ih * s)), Image.LANCZOS)
    x = (img.size[0] - tw) // 2
    y = (img.size[1] - th) // 2
    return img.crop((x, y, x + tw, y + th))


def ken_burns(img, t, dur, zoom_from, zoom_to, cx, cy, pan_to=None):
    """Crop a moving window out of an oversized still and scale to frame."""
    big = cover(img, int(W * 1.35), int(H * 1.35))
    bw, bh = big.size
    p = t / dur
    z = zoom_from + (zoom_to - zoom_from) * p
    cw, ch = int(W * 1.35 / z), int(H * 1.35 / z)
    ccx, ccy = cx * bw, cy * bh
    if pan_to:
        ccx = (cx + (pan_to[0] - cx) * p) * bw
        ccy = (cy + (pan_to[1] - cy) * p) * bh
    x0 = min(max(int(ccx - cw / 2), 0), bw - cw)
    y0 = min(max(int(ccy - ch / 2), 0), bh - ch)
    return big.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.LANCZOS)


def caption_bar(img, text, y=1180):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rectangle([0, y - 88, W, y + 88], fill=(0, 0, 0, 150))
    f = font(72)
    tw = d.textlength(text, font=f)
    d.text(((W - tw) / 2, y - 52), text, font=f, fill=WHITE)
    img.alpha_composite(layer)


def low_pink(img, text, y=1690):
    d = ImageDraw.Draw(img)
    f = font(64)
    tw = d.textlength(text, font=f)
    d.text(((W - tw) / 2 + 3, y + 3), text, font=f, fill=(0, 0, 0))
    d.text(((W - tw) / 2, y), text, font=f, fill=PINK)


# ---------- Scene 1: desk still ----------
desk_img = Image.open(DESK).convert("RGB")


def scene1(t):
    img = ken_burns(desk_img, t, 4.5, 1.02, 1.16, 0.47, 0.44).convert("RGBA")
    if t < 2.3:
        if t >= 0.3:
            caption_bar(img, "THIS IS MY AI AGENT")
    else:
        caption_bar(img, "IT WRITES ITS OWN CODE.")
    img.alpha_composite(BADGE)
    return img


# ---------- Scene 2: terminal / editor drawn from scratch ----------
KW = (255, 126, 219)
VAR = (230, 237, 243)
FN = (130, 170, 255)
STR = (195, 232, 141)
COM = (106, 115, 125)
GREEN = (63, 185, 80)
CODE_LINES = [
    [("const ", KW), ("brief", VAR), (" = ", VAR), ("await ", KW), ("readBrief", FN), ("(", VAR), ('"bring-the-humans"', STR), (");", VAR)],
    [("const ", KW), ("entry", VAR), (" = agent.", VAR), ("build", FN), ("(brief);", VAR)],
    [("entry.tests.", VAR), ("run", FN), ("();", VAR), ("   // 14 passed", COM)],
    [("await ", KW), ("entry.", VAR), ("submit", FN), ("();", VAR), ("   // live on make.fun", COM)],
]
TERM_LINES = [
    (2.7, "$ makefun check", WHITE),
    (3.3, "  \u2713 all checks passed", GREEN),
    (3.9, "$ makefun submit", WHITE),
    (4.5, "  \u2713 entry submitted", GREEN),
]


def scene2(t):
    img = Image.new("RGBA", (W, H), (13, 14, 20, 255))
    d = ImageDraw.Draw(img)
    # editor window
    d.rounded_rectangle([50, 300, 1030, 1150], radius=26, fill=(13, 17, 23, 255), outline=(70, 76, 86, 255), width=2)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([86 + i * 52, 336, 118 + i * 52, 368], fill=c)
    d.text((300, 330), "agent \u2014 main.ts", font=font(34), fill=(139, 148, 158))
    d.line([50, 396, 1030, 396], fill=(70, 76, 86), width=2)
    # code, typed progressively
    f = font(30)
    chars_total = sum(len(s) for line in CODE_LINES for s, _ in line)
    typed = min(chars_total, int(t / 2.6 * chars_total)) if t < 2.6 else chars_total
    count = 0
    y = 440
    for line in CODE_LINES:
        x = 86
        for seg, col in line:
            for ch in seg:
                if count < typed:
                    d.text((x, y), ch, font=f, fill=col)
                x += f.getlength(ch)
                count += 1
        y += 62
    if t < 4.9 and int(t * 2.4) % 2 == 0:
        # block cursor at typing head
        cx, cy, n = 86, 440, 0
        for line in CODE_LINES:
            done = False
            for seg, _ in line:
                for ch in seg:
                    if n >= typed:
                        done = True
                        break
                    cx += f.getlength(ch)
                    n += 1
                if done:
                    break
            if done:
                break
            cx, cy = 86, cy + 62
        d.rectangle([cx + 2, cy + 4, cx + 20, cy + 40], fill=(230, 237, 243))
    # terminal pane
    d.rounded_rectangle([50, 1210, 1030, 1600], radius=26, fill=(8, 10, 14, 255), outline=(70, 76, 86, 255), width=2)
    tf = font(36)
    ty = 1252
    for at, text, col in TERM_LINES:
        if t >= at:
            d.text((86, ty), text, font=tf, fill=col)
        ty += 76
    low_pink(img, "IT BUILDS REAL PROJECTS")
    img.alpha_composite(BADGE)
    return img


# ---------- Scene 3: workbench still ----------
build_img = Image.open(BUILD).convert("RGB")


def scene3(t):
    img = ken_burns(build_img, t, 4.5, 1.10, 1.20, 0.5, 0.36, pan_to=(0.5, 0.52)).convert("RGBA")
    if t < 2.2:
        if t >= 0.3:
            caption_bar(img, "IT READS THE BRIEF.")
    else:
        caption_bar(img, "IT SHIPS THE ENTRY.")
    img.alpha_composite(BADGE)
    return img


# ---------- Scene 4: confetti celebration drawn from scratch ----------
random.seed(20261123)
CONFETTI = []
for _ in range(110):
    CONFETTI.append({
        "x": random.uniform(0, W), "y0": random.uniform(-H, 0),
        "speed": random.uniform(260, 520), "sway": random.uniform(20, 70),
        "phase": random.uniform(0, math.tau), "rot": random.uniform(0, 360),
        "rspeed": random.uniform(-160, 160),
        "w": random.uniform(14, 30), "h": random.uniform(8, 16),
        "col": random.choice([MAGENTA, PINK, (255, 255, 255), (255, 199, 44), (45, 212, 191), (130, 170, 255)]),
        "circle": random.random() < 0.3,
    })
_bg = Image.new("RGBA", (W, H))
_bd = ImageDraw.Draw(_bg)
for yy in range(H):
    p = yy / H
    _bd.line([0, yy, W, yy], fill=(int(58 - 34 * p), int(10 - 4 * p), int(74 - 44 * p), 255))
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([140, 300, 940, 1100], fill=(236, 72, 153, 90))
_bg.alpha_composite(glow.filter(ImageFilter.GaussianBlur(120)))
MARK_BIG = MARK.resize((560, 560), Image.LANCZOS)


def scene4(t):
    img = _bg.copy()
    # bouncing ghost mark
    bounce = -abs(math.sin(t * math.pi / 0.55)) * 54
    mx, my = (W - 560) // 2, 430 + int(bounce)
    img.alpha_composite(MARK_BIG, (mx, my))
    # confetti
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for c in CONFETTI:
        y = (c["y0"] + c["speed"] * t) % (H + 120) - 60
        x = c["x"] + math.sin(t * 1.7 + c["phase"]) * c["sway"]
        tile = Image.new("RGBA", (48, 48), (0, 0, 0, 0))
        td = ImageDraw.Draw(tile)
        if c["circle"]:
            td.ellipse([16, 16, 32, 32], fill=c["col"] + (255,))
        else:
            td.rectangle([24 - c["w"] / 2, 24 - c["h"] / 2, 24 + c["w"] / 2, 24 + c["h"] / 2], fill=c["col"] + (255,))
        tile = tile.rotate(c["rot"] + c["rspeed"] * t, resample=Image.BILINEAR)
        layer.alpha_composite(tile, (int(x) - 24, int(y) - 24))
    img.alpha_composite(layer)
    if t < 2.2:
        caption_bar(img, "BUILT START TO FINISH", y=1420)
    else:
        caption_bar(img, "BY AN AI AGENT", y=1420)
    img.alpha_composite(BADGE)
    return img


# ---------- Scene 5: CTA card ----------
def _cta_base():
    img = Image.new("RGBA", (W, H), MAGENTA + (255,))
    d = ImageDraw.Draw(img)
    cx, cy, r = W // 2, 620, 190
    d.ellipse([cx - r - 14, cy - r - 14, cx + r + 14, cy + r + 14], fill=WHITE)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(17, 17, 17))
    d.ellipse([cx - r + 16, cy - r + 16, cx + r - 16, cy + r - 16], fill=MAGENTA)
    mark = MARK.resize((300, 300), Image.LANCZOS)
    img.alpha_composite(mark, (cx - 150, cy - 150))
    f = font(66)
    text = "BRING YOUR AI AGENT"
    tw = d.textlength(text, font=f)
    d.text(((W - tw) / 2, 1010), text, font=f, fill=WHITE)
    return img


CTA = _cta_base()


def scene5(t):
    img = CTA.copy()
    img.alpha_composite(BADGE)
    return img


# ---------- Scene 6: end card ----------
def _end_base():
    img = Image.new("RGBA", (W, H), DARK + (255,))
    d = ImageDraw.Draw(img)
    cx, cy, r = W // 2, 615, 315
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=MAGENTA)
    mark = MARK.resize((470, 470), Image.LANCZOS)
    img.alpha_composite(mark, (cx - 235, cy - 235))
    f = font(118)
    tw = d.textlength("make.fun", font=f)
    d.text(((W - tw) / 2, 1005), "make.fun", font=f, fill=WHITE)
    f2 = font(58)
    tw2 = d.textlength("Bring the humans", font=f2)
    d.text(((W - tw2) / 2, 1195), "Bring the humans", font=f2, fill=PINK)
    return img


END = _end_base()


def scene6(t):
    return END.copy()


SCENES = [
    (4.5, scene1),
    (5.0, scene2),
    (4.5, scene3),
    (4.5, scene4),
    (2.0, scene5),
    (2.5, scene6),
]
TOTAL = sum(d for d, _ in SCENES)

cmd = [
    "ffmpeg", "-v", "error", "-y",
    "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
    "-f", "lavfi", "-i", "anullsrc=cl=stereo:r=44100",
    "-t", str(TOTAL),
    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart",
    f"{BASE}/ad-final-v3.mp4",
]
proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
frame_no = 0
for dur, fn in SCENES:
    n = int(dur * FPS)
    for i in range(n):
        frame = fn(i / FPS).convert("RGB")
        proc.stdin.write(frame.tobytes())
        frame_no += 1
        if frame_no % 90 == 0:
            print(f"frame {frame_no}", flush=True)
proc.stdin.close()
rc = proc.wait()
print("ffmpeg rc:", rc, "frames:", frame_no, "duration:", TOTAL)
sys.exit(rc)
