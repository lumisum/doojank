# Alignment stack and operating notes

Use this reference when selecting or running the alignment engine.

## Recommended stack

| Component | Role | Use |
| --- | --- | --- |
| Xingyu Lyrics Aligner (`xingyu-align`) | Local command-line wrapper for trusted lyric alignment | Preferred when already installed. It takes local audio plus line-by-line trusted lyrics, uses WhisperX CTC alignment without ASR in the main path, and emits `lyrics.swlrc`, `lyrics.lrc`, `alignment.json`, and `report.json`. |
| WhisperX | CTC forced-alignment engine underneath the preferred Chinese flow | Chinese uses `zh`; the upstream alignment code includes a Chinese wav2vec2 model and supports character-level timestamps. Use it to time known text, not to replace the supplied lyrics. |
| FFmpeg / ffprobe | Decode common audio formats and inspect duration | Use for format validation and duration checks. Keep the original timeline; any transformed or separated track must be compared back to it. |
| Python standard library | Convert line intervals from SWLRC to SRT | The bundled `scripts/swlrc_to_srt.py` avoids an extra SRT dependency and refuses incomplete or mismatched line mappings. |

Do not install packages or download multi-gigabyte model weights silently. If the needed CLI or Chinese model is missing, explain what is missing and ask before installing or downloading it. Keep audio and lyrics local; do not upload them to a hosted transcription service.

## Xingyu workflow

Check availability and the runtime first:

```bash
xingyu-align doctor
xingyu-align models status --language zh
```

If the Chinese model is already available, align the exact lyric file:

```bash
xingyu-align align \
  --audio "/path/to/song.wav" \
  --lyrics "/path/to/lyrics.txt" \
  --output-dir "/path/to/alignment-result" \
  --language zh \
  --device cpu
```

Review `report.json`, especially `summary.coverage`, `summary.skipped_line_count`, `summary.estimated_token_count`, and `warnings`. Check that `lyrics.swlrc` has one timed line block for every non-empty lyric line. A skipped line or incomplete line timing must not be turned into a fabricated SRT cue.

Convert only after that review:

```bash
python3 "/path/to/song-srt-builder/scripts/swlrc_to_srt.py" \
  --lyrics "/path/to/lyrics.txt" \
  --swlrc "/path/to/alignment-result/lyrics.swlrc" \
  --output "/path/to/song.srt"
```

The converter checks line counts and compares normalized lyric characters against SWLRC tokens. It uses the original lyric line for display and the SWLRC line interval for timing. If a line was skipped or the texts do not match, correct the source/alignment and rerun; do not force conversion.

## Fallbacks and limitations

- If Xingyu is unavailable but WhisperX is installed, use its known-transcript alignment API with the Chinese `zh` alignment model and character timing output. Group characters back into the user's original lyric lines. Preserve exact source text and report any unsupported characters or unaligned spans.
- Do not make `stable-ts` a required dependency. It offers plain-text alignment, but its upstream GitHub repository was archived in May 2026. Use only if it is already present and it produces a better reviewed result for the specific recording.
- Do not make Demucs a required dependency. Its upstream repository is archived, and source separation can alter edges or introduce artifacts. If the accompaniment masks the vocal, prefer a user-provided vocal stem; otherwise treat separation as an optional comparison pass and verify all timestamps against the original mix.
- CTC and Whisper aligners are trained primarily on speech and can drift on sustained notes, melisma, vibrato, backing vocals, and dense mixes. A machine score or valid SRT syntax does not prove the line is synchronized. Review uncertain intervals by listening to the original audio.

## Primary documentation

- [Xingyu Lyrics Aligner README](https://github.com/wangjiqing/xingyu-lyrics-aligner)
- [Xingyu best-usage guide](https://github.com/wangjiqing/xingyu-lyrics-aligner/blob/main/docs/guides/best-usage.zh-CN.md)
- [Xingyu SWLRC v1 specification](https://github.com/wangjiqing/xingyu-lyrics-aligner/blob/main/docs/specs/swlrc-v1.md)
- [WhisperX repository](https://github.com/m-bain/whisperX)
- [WhisperX Chinese alignment model mapping](https://github.com/m-bain/whisperX/blob/main/whisperx/alignment.py)
- [stable-ts repository and archive status](https://github.com/jianfch/stable-ts)
- [Demucs repository and maintenance status](https://github.com/facebookresearch/demucs)

