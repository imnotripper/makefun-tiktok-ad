// main.ts — entrypoint for bring-the-humans-03.
//
// Copies VIDEO.json from this repository into the output directory the
// grader reads. That is the whole job: the house reads the TikTok
// video itself from the address inside VIDEO.json.
// Checked this session: run with MAKEFUN_OUTPUT_DIR set to a folder,
// it copies VIDEO.json over byte for byte.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = dirname(fileURLToPath(import.meta.url));
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(outputDir, { recursive: true });
copyFileSync(join(repoRoot, "VIDEO.json"), join(outputDir, "VIDEO.json"));
console.log(`Copied VIDEO.json to ${outputDir}.`);
