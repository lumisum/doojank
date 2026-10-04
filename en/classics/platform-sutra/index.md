---
layout: default
lang: en
translation_key: classic-platform-sutra
title: Platform Sutra
description: "Read Platform Sutra in the original Chinese, with Chinese study notes and an English reading interface."
permalink: /en/classics/platform-sutra/
---

<article class="scripture-page" data-mode="parallel">
  <button type="button" class="pure-reader-exit" data-pure-exit hidden aria-label="Exit immersive mode">Exit immersive mode <span aria-hidden="true">↗</span></button>
  <header class="scripture-hero">
    <img src="{{ '/assets/scriptures/platform-sutra-banner.png' | relative_url }}" alt="Pine-green contemplative artwork for Platform Sutra" fetchpriority="high">
    <div class="scripture-hero-shade" aria-hidden="true"></div>
    <div class="scripture-hero-copy">
      <p class="scripture-kicker with-icon"><svg class="ui-icon" aria-hidden="true"><use href="#icon-lotus"></use></svg>Chan · Wisdom · Practice</p>
      <h1>Platform Sutra</h1>
      <p lang="zh-CN"><strong>无相 · 无念 · 无住</strong></p>
    </div>
    <a class="scripture-hero-back" href="{{ '/en/classics/' | relative_url }}">‹ Library</a>
  </header>

  <section class="scripture-intro section-shell" aria-labelledby="scripture-intro-title">
    <div>
      <p class="eyebrow with-icon"><svg class="ui-icon" aria-hidden="true"><use href="#icon-sutra"></use></svg>A classic of practice and everyday life</p>
      <h2 id="scripture-intro-title">Follow the Sixth Patriarch’s teaching into daily life.</h2>
    </div>
    <div class="scripture-intro-copy">
      <p>This reader presents the ten principal chapters of the Platform Sutra of the Sixth Patriarch: Huineng’s search, teaching, and exchanges with disciples. It explores wisdom, nonattachment to form and thought, non-clinging, concentration, and practice. Original passages and Wulai’s chapter notes remain in Chinese.</p>
      <p>The source is CBETA’s Platform Sutra, Taishō T48 No. 2008, compiled by Zongbao. The ten principal chapters are included; introductory encomia and appended inscriptions are not part of this reading text. Main text is extracted from XML and converted to simplified Chinese. Editions vary in headings and wording. <a href="{{ '/classics/platform-sutra/source/T48n2008.xml' | relative_url }}">Source XML</a> · <a href="https://github.com/cbeta-org/xml-p5/blob/master/T/T48/T48n2008.xml">CBETA edition</a> · <a href="https://cbeta.org/copyright">License details</a>. CBETA materials are for noncommercial use; this prepared text is shared under CC BY-NC-SA 4.0.</p>
      <p class="translation-note">The original text and study notes are intentionally preserved in Chinese. This page provides an English reading interface, not a translation of the classic.</p>
    </div>
  </section>

  <section class="scripture-reader" aria-label="Original text reader">
    <div class="scripture-controls">
      <div class="reader-mode" role="group" aria-label="Choose reading mode">
        <button type="button" class="reader-mode-button" data-reader-mode="original" aria-pressed="false">Original only</button>
        <button type="button" class="reader-mode-button" data-reader-mode="parallel" aria-pressed="true">Text + Chinese notes</button>
              <button type="button" class="reader-mode-button" data-reader-mode="pure" aria-pressed="false">Immersive mode</button>
      </div>
      <div class="reader-audio-control" data-audio-state="loading" role="group" aria-label="Background music">
        <audio id="scripture-audio" src="{{ '/assets/audio/wulai-reading.mp3' | relative_url }}" loop preload="none"></audio>
        <button type="button" class="reader-audio-toggle" data-audio-toggle aria-pressed="false" aria-label="Play background music">
          <span aria-hidden="true">♫</span><span data-audio-toggle-label>Play music</span>
        </button>
        <label class="reader-audio-volume">
          <span>Volume</span>
          <input type="range" data-audio-volume min="0" max="0.25" step="0.01" value="0.08" aria-label="Music volume">
          <output data-audio-volume-value>8%</output>
        </label>
        <span class="reader-audio-status" data-audio-status aria-live="polite">Attempting playback</span>
      </div>
      <div class="reader-tools" aria-label="Reading tools">
        <button type="button" data-font-step="-1" aria-label="Decrease text size">A−</button>
        <button type="button" data-font-step="1" aria-label="Increase text size">A+</button>
        <button type="button" data-index-toggle aria-expanded="false" aria-controls="scripture-index">Contents <span aria-hidden="true">⌄</span></button>
      </div>
    </div>
    <div class="scripture-progress" aria-hidden="true">
      <span id="scripture-chapter-count">Loading sections</span>
      <span class="scripture-progress-track"><span id="scripture-progress-bar"></span></span>
      <span>Read at your own pace</span>
    </div>
    <nav id="scripture-index" class="scripture-index-nav" aria-label="Contents" hidden>
      <ol id="scripture-index-list"></ol>
    </nav>
    <div class="scripture-reading-note" data-parallel-note>
      <span class="reading-note-mark" aria-hidden="true"><svg class="ui-icon"><use href="#icon-dharma"></use></svg></span>
      <p><strong>Reading note</strong> · Read the original first, then consult the Chinese study notes. Leave unresolved questions open and return to the text and reliable commentaries.</p>
    </div>
    <div id="scripture-content" class="scripture-content" aria-live="polite" aria-busy="true">
      <p class="scripture-loading">Loading the Chinese text…</p>
    </div>
    <p id="scripture-error" class="scripture-error" hidden>The text could not be loaded. <a href="{{ '/classics/platform-sutra/original.txt' | relative_url }}">Open the Chinese plain text</a> to continue.</p>
    <div class="scripture-endnote">
      <span aria-hidden="true"><svg class="ui-icon"><use href="#icon-dharma"></use></svg></span>
      <p>May this reading return to the choices of everyday life.</p>
      <a href="{{ '/en/' | relative_url }}#classics">Back to Wulai</a>
    </div>
  </section>
</article>
<script id="scripture-source-url" type="application/json">{{ '/classics/platform-sutra/original.txt' | relative_url | jsonify }}</script>
<script id="scripture-reader-config" type="application/json">{"sectionUnit":"品"}</script>
<script id="scripture-notes-data" type="application/json">{{ site.data.platform_sutra | jsonify }}</script>
<script src="{{ '/assets/js/scripture-reader.js' | relative_url }}?v={{ site.time | date: '%s' }}" defer></script>
