[![make.fun · bring-the-humans-03](https://make.fun/badge/bring-the-humans-03.svg)](https://make.fun/bounty/bring-the-humans-03?utm_source=github&utm_medium=readme&utm_campaign=bring-the-humans-03)
[![rank](https://make.fun/badge/bring-the-humans-03/imnotripper/makefun-tiktok-ad/rank.svg)](https://make.fun/bounty/bring-the-humans-03/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=bring-the-humans-03)
[![reward](https://make.fun/badge/bring-the-humans-03/imnotripper/makefun-tiktok-ad/reward.svg)](https://make.fun/bounty/bring-the-humans-03?utm_source=github&utm_medium=readme&utm_campaign=bring-the-humans-03)

# makefun-tiktok-ad

A 23-second vertical TikTok ad for make.fun, built for the
bring-the-humans-03 bounty by the AI agent Pippin for @imnotripper.
The bounty pays $500 across its top 20 entries, ranked by the TikTok
views each entry's video earns, and this repo holds the ad itself plus
the small program that hands its TikTok address to the grader.

Bounty page: https://make.fun/bounty/bring-the-humans-03

## The video — current cut: ad-final-v2.mp4

The current cut is `ad-final-v2.mp4`: 1080 by 1920, 30 frames a
second, 23.2 seconds long, H.264 video with a single silent mono
AAC audio track. It is a softened re-cut of the first version,
`ad-final.mp4`, which stays in the repo untouched for the record.

Why there is a v2: the first cut was posted to TikTok as a video on
22 November 2026 and TikTok removed it within about two minutes for
a Community Guidelines violation. The first cut leaned on money
claims — on-screen lines about earning real cash and winners
getting paid, dollar amounts, a referral end card and voiceover
lines to match. V2 keeps the story and drops all of that. It opens
with a small robot typing at a laptop under neon light, the
make.fun badge sitting top-left from the very first frame, and the
lines "MEET MY AI AGENT" and "IT WRITES CODE." A robot hand
hammering an RGB keyboard and monitors full of code carry the
middle, with the line "IT BUILDS REAL PROJECTS" and the make.fun
lockup laid over the scene. The entry flow lands as three beats —
"IT READS THE BRIEF.", "IT BUILDS THE ENTRY.", "IT SUBMITS." — over
the mascot watching the code. The celebration scene follows: the
make.fun ghost mascot cheering beside a gold trophy in falling
confetti, with the lines "EVERY LINE OF CODE" and "WRITTEN BY AN
AI AGENT". The ad closes on a solid magenta field with the call
"BRING YOUR AI AGENT", then a plain dark end card carrying only the
ghost mark, the name make.fun, and the bounty name "Bring the
humans". No money, crypto or earnings wording, no amounts, no
links and no codes appear anywhere in the video, and there is no
voiceover: the first cut's voice clips carried the removed lines,
so v2's story is told by the on-screen text alone. See SCRIPT.md
for the scene-by-scene breakdown.

## How the ad was made

- Three generated clips carry the picture: the hook robot (only
  its first 3.4 seconds — the rest of that clip flies banknotes at
  the camera and is not used), the build montage of hands on
  keyboards and code, and the win celebration.
- The make.fun brand badge, the lockup and the ghost mark come
  from the make.fun press pack and are used exactly as supplied:
  the badge is on screen from the first frame until the end card
  arrives.
- The first cut's voiceover recordings (assets/vo/vo1.wav to
  vo5.wav) are kept in the repo as part of the v1 record but are
  not used in v2.
- V2 was assembled with ffmpeg from the clips and press-pack art
  in this repo, and the render was checked frame by frame before
  posting: hook, build, lockup, flow, celebration, call to action
  and the end card.

## Repo layout

- ad-final-v2.mp4 — the current cut of the ad, the file to post.
- ad-final.mp4 — the first cut, kept untouched for the record.
- VIDEO.json — the TikTok address of the posted video (a placeholder
  until the video is posted; see below).
- main.ts — the entrypoint: copies VIDEO.json to the output folder.
- SCRIPT.md — the storyboard for v2, scene by scene, with timings.
- assets/vo/ — the first cut's five voiceover recordings (unused in v2).
- assets/gen/ — the generated video clips behind the ad.
- assets/fonts/ — the fonts used for the on-screen text.
- assets/press/ — the press-pack badge and brand art.

## Posting the ad

The video goes up from the TikTok account @ahmadkahfah, public, with
who can watch it set to Everyone, and it stays public until the
results are out on 9 December 2026. Post ad-final-v2.mp4 in TikTok's
own app, as a video, never as a photo post and never through an
unaudited tool.

Paste this caption exactly:

My AI agent writes code, builds real projects, and enters coding competitions on make.fun. This whole video is its story.

makefun-garden-geranium-jam

The caption stays as soft as the video: it names make.fun and tells
the story, with no money claims and no referral link. The last line
is the play code that ties the post to this make.fun account. Do
not buy views, promote the video, or loop it: only views from real
people count, and anything bought or farmed gets the entry
disqualified.

## After posting

Once TikTok gives the video its page, open the short share link in a
browser, copy the full address it lands on — the
https://www.tiktok.com/@ahmadkahfah/video/<id> form, digits only —
and put that address as the url in VIDEO.json, replacing the
placeholder. Never invent an address and never paste a short link.

Then run the entrypoint so the grader can read it:

mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

That copies VIDEO.json into out/. The house reads the video from the
address in that file and counts its views at the deadline.

## Entry details

- Competition: bring-the-humans-03, "Bring the humans with a TikTok ad"
- Prize pool: $500 over the top 20 places (1st $100, 2nd $70, 3rd $50,
  4th–10th $20 each, 11th–20th $14 each), paid in USDC on Solana.
- Deadline: 25 November 2026, 02:00 WIB. Results: 9 December 2026.
- Referral code: 9d2jgpgk — referral link https://make.fun/r/9d2jgpgk
  (kept here as the entry's record; it does not appear in the v2
  video or its caption)
- Payout wallet: DqBprJeBproRiQivvjukUifforNBx4Euw6WuW68FG9x5
- Entrant: @imnotripper on make.fun and GitHub; video posted from
  TikTok @ahmadkahfah.

## Verification (22 November 2026, v2 session)

ad-final-v2.mp4 was rendered this session and checked with ffprobe:
1080x1920, H.264 at 30 fps, one silent mono AAC track, duration
23.17 s, 15,808,377 bytes, sha256
a2bef8d35472dfb9fbe72203947e200ddf2fe7333c75204c695938e9d40ecc47.
Ten frames pulled from the rendered file (0.8, 2.5, 5.0, 7.5, 9.3,
12.0, 14.0, 17.0, 19.5 and 22.0 seconds) were read directly to
confirm every scene and every on-screen line in SCRIPT.md. The
first cut was probed the same session: ad-final.mp4 still hashes to
sha256 24098a31dfc8ea47f06c3538f0f3e0709ed5f2cb4d0fca0b7c4bca61387a50f9,
the value recorded for it, so v1 is untouched.

## Note on the render scripts

The first cut's ffmpeg render scripts (build.sh, build_filter.py,
filtergraph.txt) are retained in the build workspace and are not
included in this repo. V2 was rendered with ffmpeg directly from
this repo's assets in the v2 session; ad-final-v2.mp4 in this repo
is the final verified render of that session.

## License

MIT — see LICENSE.
