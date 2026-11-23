# SCRIPT-V3.md — storyboard for ad-final-v3.mp4 (bring-the-humans-03)

## Why v3 exists

The v2 cut (ad-final-v2.mp4, TikTok posts 7710770039959424263 and
7710777775631633672 on @ahmadkahfah) is region-blocked by TikTok for
US viewers: a US fetch of either post returns statusCode 10231
"cross_border_violation" with no playAddr (diagnosis verified
2026-11-23). The most likely cause is duplicate/reused content —
the second v2 post is byte-identical to the first, and v2 itself is
a re-trim of the same three generated clips (assets/gen hook/build/
win) as the v1 upload TikTok removed. make.fun only accepts videos
viewable in the US, and its reader classified the blocked posts as
photo posts. Deadline: 2026-11-25 02:00 WIB.

V3 is therefore built from **entirely new footage**. No frame is
sourced from, trimmed from, or derived from the v1/v2 clips.

## How the footage was made

Video generation was not available for this account/region (the
media pipeline returned a lasting region restriction), so v3 was
built from two other kinds of genuinely new material:

- Two still images generated fresh for v3 on 2026-11-23
  (v3/gen/media-generation-bth03-v3-desk-*.webp and
  v3/gen/media-generation-bth03-v3-build-*.webp), animated with
  Ken Burns moves in the render.
- Screen content drawn and animated from scratch with PIL: a code
  editor / terminal scene (the agent typing its own entry code,
  running checks, submitting) and a confetti celebration scene
  built around the press-pack ghost mark.

The story is unchanged and compliant: an AI agent that writes
code, builds a real project, and enters a coding competition on
make.fun. There is no money, earnings, prize, dollar, crypto,
USDC, referral or play-code wording anywhere in the picture, the
on-screen text, or the audio (the audio track is silent, as in
v2). No TikTok or commercial sounds are used.

## Timing map

- 0.0–4.5 s — Desk. New character, new setting.
- 4.5–9.5 s — Terminal. The agent codes and submits, drawn live.
- 9.5–14.0 s — Workbench. Robot arms assemble a tiny robot.
- 14.0–18.5 s — Celebration. Ghost mark and falling confetti.
- 18.5–20.5 s — Call to action. Magenta field, one line.
- 20.5–23.0 s — End card. The mark, the name, the bounty name.

Total 23.0 s, 1080×1920, 30 fps, H.264 + AAC (silent stereo).

## Scene 1 — Desk (0.0–4.5 s)

Picture: a freshly generated still — a small round **orange** robot
with a glowing teal pixel face at a sunlit, plant-filled desk,
typing on a laptop showing code. Bright daytime room, books and
plants; nothing like v2's dark pink-purple neon room or its white
headphone robot. Slow Ken Burns push-in (zoom 1.02 → 1.16).

The make.fun badge (press-pack badge-9x16.png, ghost mark and
wordmark in a magenta pill) sits top-left from the first frame and
stays until the end card, exactly as in v2.

On screen, in big white capitals over a dark bar:

- "THIS IS MY AI AGENT" (0.3–2.3 s)
- "IT WRITES ITS OWN CODE." (2.3–4.5 s)

## Scene 2 — Terminal (4.5–9.5 s)

Picture: an editor window drawn from scratch, titled
"agent — main.ts". Syntax-coloured code types itself in character
by character:

- `const brief = await readBrief("bring-the-humans");`
- `const entry = agent.build(brief);`
- `entry.tests.run();   // 14 passed`
- `await entry.submit();   // live on make.fun`

Below it, a terminal pane prints, line by line:

- `$ makefun check` → `✓ all checks passed`
- `$ makefun submit` → `✓ entry submitted`

This is real screen-capture-style material of an agent building
and submitting an entry — content that did not exist in v1/v2.

On screen, in big pink capitals low in the frame (no bar):

- "IT BUILDS REAL PROJECTS" (4.5–9.5 s)

## Scene 3 — Workbench (9.5–14.0 s)

Picture: a second freshly generated still — a top-down view of a
wooden workbench where two robotic arms assemble a tiny glowing
robot from circuit boards, wires and LEDs. Slow Ken Burns pan
downward with a gentle zoom (1.10 → 1.20). The badge stays
top-left.

On screen, in big white capitals over a dark bar:

- "IT READS THE BRIEF." (9.8–11.7 s)
- "IT SHIPS THE ENTRY." (11.7–14.0 s)

## Scene 4 — Celebration (14.0–18.5 s)

Picture: drawn from scratch — a deep purple stage gradient with a
soft magenta glow; the press-pack ghost mark (mark-on-dark) bounces
in the centre while 110 pieces of coloured confetti (magenta, pink,
white, gold, teal, blue) fall, sway and rotate. No trophy, no
medals — the celebration is the finished build itself. The badge
stays top-left.

On screen, in big white capitals over a dark bar, lower than in
the other scenes so the mark stays clear:

- "BUILT START TO FINISH" (14.0–16.2 s)
- "BY AN AI AGENT" (16.2–18.5 s)

## Scene 5 — Call to action (18.5–20.5 s)

Picture: hard cut to a flat magenta field. The ghost mark sits in
its black-ringed circle in the upper middle; the badge is still
top-left. One line only.

On screen, in big white capitals:

- "BRING YOUR AI AGENT"

## Scene 6 — End card (20.5–23.0 s)

Picture: a plain dark card built from press-pack art, following
the same brand rules as v2: the ghost mark in its magenta disc
near the top, "make.fun" in big white letters under it, and the
bounty name in pink underneath. No badge overlay on this card —
the card itself is the brand. No link, no code, no amounts.

On screen:

- "make.fun"
- "Bring the humans"

## Audio

None. A silent stereo AAC track is kept so the file has the same
shape as the earlier cuts. No voiceover, no music, no TikTok or
commercial sounds — original silence only.

## Brand rules the cut follows

- The make.fun badge is on screen from the first frame until the
  end card comes in, placed and sized exactly as the press pack
  gives it (the same full-frame overlay used for v2).
- The name is written make.fun everywhere, lowercase with the dot.
- Every make.fun mark in the video comes from the press pack;
  nothing is redrawn, recoloured, stretched or cropped.
- No money, crypto, earnings or prize wording anywhere in the
  picture, the text or the audio; no links and no codes in the
  video.

## How v3 was rendered

Rendered 2026-11-23 by `v3/render_v3.py` (kept in this repo): a
Python/PIL renderer that draws every frame at 1080×1920 and pipes
them to ffmpeg (libx264, CRF 20, yuv420p, 30 fps) with a silent
AAC track. Text is set in the repo's JetBrains Mono Bold, the same
font as v2. The finished file is ad-final-v3.mp4, 4,775,528 bytes,
sha256 c5beee844164b0477db6f42b6fbd8090e2690a7e706b6a7b4a12208d2456ffb5.

## How this storyboard was checked

The finished file was probed with ffprobe (H.264, 1080×1920,
30 fps, AAC, 23.000 s) and frames were pulled at ten timestamps
(1.2, 3.2, 6.0, 8.6, 10.8, 12.8, 15.2, 17.4, 19.5 and 21.8 s,
kept in v3/checks/) and read directly: every scene, caption line,
the badge placement and the end card are as described above, and
no frame contains money, earnings, prize, crypto or referral
content. The v1 and v2 files were not touched.

## Next steps (not done by this build)

1. Bro posts ad-final-v3.mp4 from @ahmadkahfah as a normal upload,
   with the TikTok "AI-generated content" label ON and the
   compliant caption from inapp-repost-plan.md §3.
2. Pippin verifies US viewability from this VM (whose egress is a
   US fetch): the new post's page data must return statusCode 0
   with a playAddr present. If it returns 10231 again, stop — the
   block is account-level, not content-level.
3. Only then, run the finisher recipe in inapp-repost-plan.md §4
   (updated VIDEO.json, bundle, kit check, submit) before the
   2026-11-25 02:00 WIB deadline.
