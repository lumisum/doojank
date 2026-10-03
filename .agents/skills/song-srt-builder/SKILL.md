---
name: song-srt-builder
description: Generate line-level SRT subtitles, lyric-background images, and song covers from user-provided lyrics and audio. Use when supplied lyrics must be synchronized and visualized; preserve the trusted wording instead of replacing it with ASR output.
---

# Song SRT Builder

Create a UTF-8 SRT whose cues follow the vocal performance, 12 coherent lyric-background images, and two song covers, using the supplied lyrics as the authoritative text.

## Inputs and defaults

- Require both the audio file and the trusted lyrics. Reuse lyrics already supplied in the conversation when they are clearly the source text.
- For this user's local music workflow, first search `/Users/elonmar/Music/AI音乐汇/<song title>/` for the song's audio, trusted lyric TXT, and any recognition SRT. Treat the matching song folder as the default output directory.
- When a trusted lyric TXT and an ASR/recognition SRT both exist, use the TXT as the lyric authority and correct the SRT cue text against it before any image work. Ignore title lines, Suno/style metadata, section labels, Markdown marker characters, SRT numbering, and timestamps when comparing; retain lyric words enclosed by Markdown formatting.
- For correction of an existing SRT, change only incorrect or missing lyric text. Preserve its cue numbering, timestamps, and chronological order; do not rerun alignment or alter timing unless the user explicitly asks for a new alignment. After edits, confirm the normalized lyric sequence matches the trusted TXT and confirm every timestamp line is unchanged.
- Accept WAV and other audio formats supported by the installed decoder. If an attached audio file is not available as a local path, ask the user to attach it in a usable form; never estimate timestamps from lyrics alone.
- Preserve lyric wording, repetitions, punctuation, ad-libs, and meaningful line breaks. Remove only subtitle numbering and timecodes if the user supplied an SRT as the lyric source. Do not add words inferred from the recording.
- Default to one cue per lyric line or sung phrase. Split a long line only at a musically supported phrase boundary, keeping every original character and its chronological order.
- If no output location is specified, save `<audio-basename>.srt` beside the audio. Keep temporary lyrics, model output, and alignment reports outside tracked source directories.

## Repository boundary

Song audio, lyrics, subtitles, cover art, background frames and generated descriptions stay local and must not be committed or pushed to this article repository. Keep outputs in the music directory above, outside the repository. If the user explicitly chooses a repository location, use an ignored `songs/<title>/` directory and confirm the outputs are ignored before staging anything. Reusable skill instructions and converter code may be tracked; article illustrations and the existing website reading ambience are separate site assets.

## Lyric-background images

- When both lyrics and their audio are provided, generate 12 background images and two covers by default along with the SRT, unless the user narrows the requested deliverables. The full visual set is 14 images.
- Read the complete lyric and divide its narrative into 12 chronological, semantically balanced sections. Distribute images across the whole song according to meaning and emotional progression, rather than splitting only by character count.
- Before generating images, prepare a 12-frame storyboard that records each lyric section, its real-world scene, the people and actions shown, and its emotional purpose. If the user supplies a related article or other context, read it first and use it to resolve the song's intended subject and ambiguous lines.
- Ground scenes in the lyrics and supplied context. Use workplace, family, historical, spiritual, or other settings only when supported; do not impose a generic romance, school, or scenery narrative. Do not carry people or a setting template from a previous song. Reuse a protagonist only when continuity serves this song; otherwise vary people, roles, and locations across the storyboard.
- Use the built-in `image_gen` tool, with one distinct generation call per image. Do not replace the set with a contact sheet or near-duplicate variants.
- Make human characters a clear visual focus in the sequence. Use a recurring protagonist when it supports continuity; let actions, choices, expressions, and relationships carry the lyric's meaning. Do not default to scenery-only images.
- Generate vertical 9:16 compositions intended as song backgrounds. This is the default for every song in this user's workflow. Reserve uncluttered space for later subtitle overlays. Do not bake in lyrics, captions, logos, or watermarks.
- Keep a coherent visual language across the set while giving each frame a distinct lyric-specific scene. Avoid generic symbolism that does not communicate the relevant lyric.
- Save the images in chronological order as `01.png` through `12.png` in `<audio-basename>_背景图/` beside the SRT by default. Follow an output location explicitly requested by the user. Keep temporary prompts and intermediates outside tracked source directories.
- Inspect all 12 results for the requested aspect ratio, visible human subjects, lyric relevance, and subtitle-safe composition. Regenerate any result that misses those requirements.

### Covers

- Create two additional cover images: one landscape 16:9 version and one portrait 9:16 version. Compose each separately for its aspect ratio instead of cropping one into the other.
- Put the exact song title on both covers in large, clean, readable Chinese typography. Use the title supplied by the user or an unambiguous title from the conversation or audio filename; if it is unclear, ask the user before creating the covers.
- Design for click-through at thumbnail size: strong visual hierarchy, a memorable human subject or action, clear contrast, and a lyric-relevant visual hook. Keep the title immediately legible and avoid clutter.
- Keep cover text limited to the exact song title; do not add taglines, credits, logos, or watermarks.
- Save the covers as `横版.png` and `竖版.png` in `<audio-basename>_封面/` beside the SRT by default. Follow an output location explicitly requested by the user.
- Inspect both covers for correct title spelling, readability at small size, human subject, and correct orientation. Regenerate any cover with incorrect or garbled title text.

## Video title and description

- For every song workflow, prepare YouTube-style video title and description copy by default. Save it as `标题与描述.md` in the song folder.
- Write a concise, clickable title grounded in the song's actual theme; include the song title and avoid unsupported claims.
- Offer multiple short description options, each no more than 20 Chinese characters, focused on the song's idea, background, or creative motivation. Add a separate concise `创作动机` note when more context is needed to explain the song's inspiration.

## Alignment workflow

1. Inspect the audio duration and confirm it decodes. Use `ffprobe`/`ffmpeg` only for inspection or lossless-compatible decoding; do not time-stretch, trim, or shift the source.
2. For Chinese songs, prefer the local trusted-lyrics workflow in [references/alignment-stack.md](references/alignment-stack.md): `xingyu-align` uses WhisperX CTC forced alignment and keeps the supplied lyrics as display text. Check its report and warnings. Do not run ASR as the source of final lyrics.
3. If that CLI is unavailable, use an installed forced aligner that accepts a known transcript. For direct WhisperX alignment, use its supported Chinese (`zh`) alignment model and character timings, then group those timings by the supplied lyric lines. Do not pass a machine-generated transcript in place of the user's lyrics.
4. Preserve repeated lines as separate chronological occurrences. Keep vocalization lines when the source lyrics include them. If the audio has extra or missing sung text, note the mismatch instead of silently changing the lyrics.
5. Convert the aligner's line intervals to SRT with the bundled converter. Use the aligned line start and end; never infer every cue end from the next cue start when explicit line ends are available.

## Quality checks

- Compare every aligned line, in order, with the trusted lyric source. A missed line, changed text, duplicated occurrence, or mapping mismatch blocks delivery as a final SRT.
- Inspect the aligner's `report.json` for skipped lines, low coverage, estimated token times, and warnings. Treat skipped lines or low coverage as a draft that needs correction.
- Review cue boundaries against the vocal onset and release, especially long held notes, repeated choruses, instrumental breaks, overlapping vocals, and spoken sections. Do not use an audio-energy threshold alone as a proxy for sung words; accompaniment can continue through vocal pauses.
- Check that cue numbers are sequential, each start precedes its end, timestamps fit the audio, and cues are chronological. Preserve real overlaps but flag them for review rather than silently moving timestamps.
- If playback or boundary review is unavailable, label the SRT as machine-aligned and unverified. Millisecond formatting is not evidence of millisecond accuracy.

## Delivery

Return the SRT, all 12 background images, both covers, and the title/description file. State whether the audio was listened through or only machine-aligned, and mention unresolved alignment lines or warnings. Do not claim exact timing for spans that the aligner could not place confidently.
