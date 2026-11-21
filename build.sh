#!/usr/bin/env bash
# Render the bring-the-humans-03 TikTok ad from this repo's assets.
# Deterministic: re-running reproduces ad-final.mp4 (same assets, same script).
# Usage: ./build.sh   (outputs ad-final.mp4 + frame checks in checks/)
set -euo pipefail
cd "$(dirname "$0")"

python3 build_filter.py

ffmpeg -y -v error \
  -i assets/gen/media-generation-bth03-hook-clip-0-e9dc8886-3258-4bb4-8638-69e0d9e0aeea.mp4 \
  -i assets/gen/media-generation-bth03-build-clip-0-e5e11f06-feb4-46be-9916-ec777264b906.mp4 \
  -i assets/gen/media-generation-bth03-win-clip-0-288d64ec-b19e-4652-ac02-c313459b2216.mp4 \
  -loop 1 -framerate 30 -t 3.929433 -i assets/press/kit/make-fun-press-kit/screenshots/board-dark.png \
  -i assets/press/badge-9x16.png \
  -c:v libvpx-vp9 -i assets/press/card-9x16.webm \
  -i assets/press/kit/make-fun-press-kit/lockup-on-dark-2400.png \
  -i assets/press/kit/make-fun-press-kit/mark-on-dark-1024.png \
  -i assets/press/kit/make-fun-press-kit/referral-card/stills/3-wordmark.png \
  -i assets/vo/vo1.wav -i assets/vo/vo2.wav -i assets/vo/vo3.wav \
  -i assets/vo/vo4.wav -i assets/vo/vo5.wav \
  -f lavfi -i "color=c=0xC41C83:s=1080x1920:r=30:d=5.53" \
  -filter_complex_script filtergraph.txt \
  -map '[v]' -map '[a]' \
  -c:v libx264 -pix_fmt yuv420p -crf 20 -preset medium -r 30 \
  -c:a aac -b:a 160k -movflags +faststart -t 22.873333 \
  ad-final.mp4

mkdir -p checks
ffprobe -v error -show_entries format=duration,size -show_entries stream=width,height,r_frame_rate,codec_name -of default=nw=1 ad-final.mp4
# Frame checks: first frame (badge must be visible), mid scenes, end card (code must read 9d2jgpgk)
for t in 0.5 2.0 4.5 10.0 14.0 18.5 22.5; do
  ffmpeg -y -v error -ss "$t" -i ad-final.mp4 -frames:v 1 "checks/frame-$t.png"
done
echo "rendered ad-final.mp4 — inspect checks/frame-*.png"
