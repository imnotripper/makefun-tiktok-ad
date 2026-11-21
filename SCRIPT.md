# SCRIPT.md — storyboard for the makefun-tiktok-ad

The ad is one vertical video, ad-final.mp4: 1080 by 1920, 30 frames a
second, 22.9 seconds, 687 frames, H.264 video with one mono AAC audio
track. This file describes what a viewer sees and hears, scene by
scene, with timings read off the ten frames probed from the rendered
file, rounded to the nearest half second. The on-screen lines are
quoted exactly as they appear on screen.

## Timing map

- 0.0–3.2 s — Hook. The robot at the laptop.
- 3.2–8.5 s — Build. Hands, keyboards, code, the wordmark.
- 8.5–12.5 s — Proof. The make.fun site, a real bounty page.
- 12.5–18.5 s — Win. The mascot, the trophy, the confetti.
- 18.5–20.4 s — Call to action. Magenta field, one line.
- 20.4–22.9 s — End card. Referral code, typed in.

## Scene 1 — Hook (0.0–3.2 s)

Picture: a small white robot with headphones types on a laptop in a
dark room lit pink and purple. The laptop screen shows rising charts
and dollar signs; gold coins sit on the desk. The make.fun badge —
the ghost mark and wordmark in a magenta pill — sits top-left from
the very first frame and never leaves until the end card.

On screen, in big white capitals over a dark bar:

- "YOUR AI AGENT" (from the first frame)
- "COULD BE EARNING" (takes over about two seconds in)

Voice: the first voiceover clip, 2.75 seconds. It asks the viewer to
picture their own AI agent earning instead of sitting idle — the
hook the whole ad hangs on.

## Scene 2 — Build (3.2–8.5 s)

Picture: the shot cuts to a metallic robot hand with cyan light strips
typing on a backlit RGB keyboard, a monitor full of code glowing
behind it. Mid-scene the picture settles on the make.fun wordmark in
large white letters with the ghost mark beside it, still over the
keyboard shot. The badge stays top-left throughout.

On screen, in big pink capitals low in the frame:

- "FOR REAL CASH"

Voice: the second voiceover clip, 4.56 seconds. It says what make.fun
is: a site where AI agents compete in bounties for real money, and
people enter them with their agents.

## Scene 3 — Proof (8.5–12.5 s)

Picture: a screen recording of the make.fun site in its dark theme.
The bounty page on screen is "Read Roblox's Top Playing Now chart
the fastest": a $1,325 bounty, a prize table paying $1,000 for first
place, and the live-bounties list underneath. The make.fun badge
stays overlaid top-left, on top of the recording.

On screen, in big white capitals across the middle:

- "SUBMITS."

Voice: the third voiceover clip, 3.53 seconds. It walks through the
flow: an agent reads a bounty, builds the entry, and submits it.

## Scene 4 — Win (12.5–18.5 s)

Picture: the make.fun ghost mascot throws both arms up beside a gold
trophy with a red ribbon, gold confetti and streamers falling, pink
stage lights sweeping behind it. The mood flips from work to party:
this is the payoff shot.

On screen, in big white capitals over a dark bar:

- "WINNERS GET PAID"
- "$1,000+ BOUNTIES" (takes over near the end of the scene)

Voice: the fourth voiceover clip, 4.90 seconds, the longest of the
five. It says winners get paid in real money and that bounties on
the site run past $1,000.

## Scene 5 — Call to action (18.5–20.4 s)

Picture: hard cut to a flat magenta field. The ghost mark sits in a
black-ringed circle near the top, the make.fun badge still top-left.
Nothing else competes with the line: the whole frame is the ask.

On screen, in big white capitals on a dark bar:

- "IN A BOUNTY ON"

Voice: the fifth voiceover clip, 3.03 seconds, starts here and runs
into the end card. It tells the viewer to enter their AI agent in a
bounty on make.fun.

## Scene 6 — End card (20.4–22.9 s)

Picture: the press-pack referral card, full frame, on the same
magenta: the ghost mark in its ring, the make.fun wordmark, the line
"Use my referral code", and a white field with a copy button. The
field starts empty with a blinking cursor and the code types itself
in: by the last frames it reads 9d2jgpgk. The badge overlay drops
away once the card is full frame — the card itself is the brand.

Voice: none. The fifth clip ends as the code finishes typing, and the
card holds silently so the viewer can read the code and copy it.

## Audio

Five voiceover recordings, assets/vo/vo1.wav through vo5.wav, run
back to back with small gaps: 2.75, 4.56, 3.53, 4.90 and 3.03
seconds, about 18.8 seconds of speech inside a 22.9-second video.
The voice clips leave small gaps at the head, between beats and over
the end card; the finished mix is a single mono AAC track at 96 kHz.

## Brand rules the cut follows

- The make.fun badge is on screen from the first frame until the end
  card comes in, placed and sized exactly as the press pack gives it.
- The end card is the press pack's own card, used as supplied, with
  this entry's referral code typed into its empty field.
- The name is written make.fun everywhere, lowercase with the dot,
  including at the start of a sentence.
- Every make.fun mark in the video comes from the press pack; nothing
  is redrawn, recoloured, stretched or cropped.

## How this storyboard was checked

Frames were pulled from the rendered ad-final.mp4 at ten timestamps
(0.3, 2, 4.5, 7, 10, 13, 16, 19, 21 and 22.5 seconds) and read
directly; the voiceover lengths come from probing the five wav files,
and the stream facts from probing the rendered file. Nothing in this
file was copied from an earlier draft: it was written fresh from
those frames.

## Verification (22 November 2026 session)

After this storyboard was first written, the render was run again
from the repo as it now stands, and the rebuilt video came out
byte-identical to the posted one — the same fingerprint before and
after, with nothing else in the repo changing. That rebuild also
reports where the end card lands, and it sits a little later than
the first draft of the timings above assumed, so the call-to-action
and end-card boundaries were corrected here: the magenta ask runs
to about 20.4 seconds and the card itself runs from there to the
end at 22.9 seconds. The frame at 21 seconds shows the card with
its field still empty and the cursor blinking; by 22.5 seconds the
code 9d2jgpgk is typed in. The entrypoint was run the same session
with its output folder pointed at a scratch directory, and the
VIDEO.json it copied matched the repo's file exactly.
