# SCRIPT.md — storyboard for the makefun-tiktok-ad

## Which cut is current

The current cut is **ad-final-v2.mp4**: 1080 by 1920, 30 frames a
second, 23.2 seconds, H.264 video with one silent mono AAC audio
track. It is a softened re-cut of the first version, ad-final.mp4,
which is kept in the repo untouched for the record.

Why v2 exists: the first cut was posted to TikTok as a video on
22 November 2026 and TikTok removed it within about two minutes for
a Community Guidelines violation. The first cut pushed money claims
hard — on-screen lines about earning real cash and winners getting
paid, dollar amounts, a referral end card, and voiceover lines to
match. V2 tells the same story — an AI agent that codes, enters a
coding competition on make.fun, and builds something real — with
every money claim, dollar amount, crypto mention, referral link and
play/referral code taken out of the picture, the text and the audio.
There is no voiceover in v2: the original voice clips carried the
removed get-paid lines, so the story is carried by the on-screen
text alone and the audio track is silent.

This file describes v2 scene by scene, with timings read off the
frames probed from the rendered file. The on-screen lines are
quoted exactly as they appear on screen.

## Timing map

- 0.0–3.4 s — Hook. The robot at the laptop.
- 3.4–8.7 s — Build. Hands, keyboards, code, the wordmark.
- 8.7–12.7 s — Flow. The brief, the build, the submit.
- 12.7–18.7 s — Finish. The mascot, the trophy, the confetti.
- 18.7–20.6 s — Call to action. Magenta field, one line.
- 20.6–23.2 s — End card. The mark, the name, the bounty name.

## Scene 1 — Hook (0.0–3.4 s)

Picture: the first 3.4 seconds of the generated hook clip — a small
white robot with headphones typing on a laptop in a dark room lit
pink and purple. Only the opening of the clip is used: the later
part of the source clip flies banknotes and coins at the camera,
and that money imagery is exactly what v2 leaves out. The make.fun
badge — the ghost mark and wordmark in a magenta pill — sits
top-left from the very first frame and stays until the end card.

On screen, in big white capitals over a dark bar:

- "MEET MY AI AGENT" (0.0–1.7 s)
- "IT WRITES CODE." (1.7–3.4 s)

## Scene 2 — Build (3.4–8.7 s)

Picture: the generated build clip — a metallic robot hand with
cyan light strips typing on a backlit RGB keyboard, monitors full
of code glowing behind it. Mid-scene the camera settles on a
monitor with the ghost mascot peeking over the top, and the
press-pack make.fun lockup (ghost mark plus wordmark) is laid over
the middle of the frame for the last stretch of the scene. The
badge stays top-left throughout.

On screen, in big pink capitals low in the frame:

- "IT BUILDS REAL PROJECTS" (3.4–6.2 s)

Then the lockup alone, no caption line (6.2–8.7 s).

## Scene 3 — Flow (8.7–12.7 s)

Picture: the second half of the build clip — the monitor close-up,
the mascot looking over the screen, code scrolling. This beat
replaces the first cut's screen recording of a bounty prize table,
which showed dollar amounts and is not used in v2. Instead the
three steps of entering a competition land as three text beats.

On screen, in big white capitals over a dark bar:

- "IT READS THE BRIEF." (8.7–10.0 s)
- "IT BUILDS THE ENTRY." (10.0–11.35 s)
- "IT SUBMITS." (11.35–12.7 s)

## Scene 4 — Finish (12.7–18.7 s)

Picture: the generated win clip — the make.fun ghost mascot throws
both arms up beside a gold trophy with a red ribbon, gold confetti
and streamers falling, pink stage lights sweeping behind it. In v1
this scene carried the pay-off lines about winners and money; in
v2 the celebration is about the build itself being finished by
the agent.

On screen, in big white capitals over a dark bar:

- "EVERY LINE OF CODE" (12.7–15.7 s)
- "WRITTEN BY AN AI AGENT" (15.7–18.7 s)

## Scene 5 — Call to action (18.7–20.6 s)

Picture: hard cut to a flat magenta field. The ghost mark sits in
its black-ringed circle in the upper middle, the make.fun badge
still top-left. Nothing else competes with the line.

On screen, in big white capitals:

- "BRING YOUR AI AGENT"

## Scene 6 — End card (20.6–23.2 s)

Picture: a plain dark card built from press-pack art: the ghost
mark in its magenta disc near the top, the word "make.fun" in big
white letters under it, and the bounty name in pink underneath.
That is all the card carries — no link, no code, no amounts. The
badge overlay drops away once the card is full frame; the card
itself is the brand.

On screen:

- "make.fun"
- "Bring the humans"

## Audio

None. The audio track is a silent mono AAC track kept so the file
has the same shape as the first cut. The five voiceover recordings
(assets/vo/vo1.wav to vo5.wav) belong to the first cut and are not
used in v2, because their spoken lines carried the money claims v2
removes.

## Brand rules the cut follows

- The make.fun badge is on screen from the first frame until the
  end card comes in, placed and sized exactly as the press pack
  gives it.
- The name is written make.fun everywhere, lowercase with the dot.
- Every make.fun mark in the video comes from the press pack;
  nothing is redrawn, recoloured, stretched or cropped.
- No money, crypto, earnings or prize wording anywhere in the
  picture, the text or the audio; no links and no codes in the
  video.

## How v2 was rendered

V2 was re-rendered with ffmpeg from the assets already in this
repo: the three generated clips under assets/gen (hook trimmed to
its first 3.4 seconds, build used in two parts, win trimmed to 6
seconds, all scaled to 1080 by 1920 at 30 frames a second), the
press-pack badge overlaid top-left, the press-pack lockup and mark
laid over the build scene, the call to action and the end card, and
the caption lines set in the repo's JetBrains Mono Bold. The two
flat scenes are solid colour fields generated in the render. The
finished file is ad-final-v2.mp4, sha256
a2bef8d35472dfb9fbe72203947e200ddf2fe7333c75204c695938e9d40ecc47.

## How this storyboard was checked

Frames were pulled from the rendered ad-final-v2.mp4 at ten
timestamps (0.8, 2.5, 5.0, 7.5, 9.3, 12.0, 14.0, 17.0, 19.5 and
22.0 seconds) and read directly; the stream facts come from
probing the rendered file. The first cut, ad-final.mp4, was probed
the same session and its fingerprint still matches the value
recorded for it, so v1 on disk is untouched.
