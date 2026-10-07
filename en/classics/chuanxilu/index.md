---
layout: default
lang: en
translation_key: classic-chuanxilu
title: Instructions for Practical Living
description: "Read Instructions for Practical Living in the original Chinese, with Chinese study notes and an English reading interface."
permalink: /en/classics/chuanxilu/
---

<article class="scripture-page" data-mode="parallel">
  <button type="button" class="pure-reader-exit" data-pure-exit hidden aria-label="Exit immersive mode">Exit immersive mode <span aria-hidden="true">↗</span></button>
  <header class="scripture-hero">
    <img src="{{ '/assets/scriptures/chuanxilu-banner.png' | relative_url }}" alt="Pine-green contemplative artwork for Instructions for Practical Living" fetchpriority="high">
    <div class="scripture-hero-shade" aria-hidden="true"></div>
    <div class="scripture-hero-copy">
      <p class="scripture-kicker with-icon"><svg class="ui-icon" aria-hidden="true"><use href="#icon-bodhi"></use></svg>Mind · Knowledge and action</p>
      <h1>Instructions for Practical Living</h1>
      <p lang="zh-CN"><strong>知行合一 · 致良知</strong></p>
    </div>
    <a class="scripture-hero-back" href="{{ '/en/classics/' | relative_url }}">‹ Library</a>
  </header>

  <section class="scripture-intro section-shell" aria-labelledby="scripture-intro-title">
    <div>
      <p class="eyebrow with-icon"><svg class="ui-icon" aria-hidden="true"><use href="#icon-sutra"></use></svg>Wang Yangming’s dialogues, letters, and recorded teaching</p>
      <h2 id="scripture-intro-title">Return philosophy to questions and action.</h2>
    </div>
    <div class="scripture-intro-copy">
      <p>Wang Yangming’s students recorded and compiled the Chuanxilu in three volumes of exchanges, letters, and other writings. The unity of knowing and acting, innate moral knowing, and the investigation of things unfold through concrete questions and disagreements. Reading by exchange helps show what each passage addresses. Text and personal study notes remain in Chinese; the notes are not scholarly annotations.</p>
      <p>The source is the three-volume Chinese Wikisource edition of Wang Shouren’s Chuanxilu. The prepared text follows its volume and record headings, converts characters to simplified Chinese, and removes webpage footnote markers. Adapted text is shared under CC BY-SA 4.0, with attribution and share-alike requirements. <a href="https://github.com/lumisum/doojank/blob/main/classics/chuanxilu/SOURCE.md">Preparation and licensing notes</a> · <a href="https://zh.wikisource.org/wiki/傳習錄">Wikisource edition</a>.</p>
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
    <p id="scripture-error" class="scripture-error" hidden>The text could not be loaded. <a href="{{ '/classics/chuanxilu/original.txt' | relative_url }}">Open the Chinese plain text</a> to continue.</p>
    <div class="scripture-endnote">
      <span aria-hidden="true"><svg class="ui-icon"><use href="#icon-dharma"></use></svg></span>
      <p>May this reading return to the choices of everyday life.</p>
      <a href="{{ '/en/' | relative_url }}#classics">Back to Wulai</a>
    </div>
  </section>
</article>
<script id="scripture-source-url" type="application/json">{{ '/classics/chuanxilu/original.txt' | relative_url | jsonify }}</script>
<script id="scripture-reader-config" type="application/json">{"sectionUnit":"节"}</script>
<script id="scripture-notes-data" type="application/json">{{ site.data.chuanxilu | jsonify }}</script>
<script src="{{ '/assets/js/scripture-reader.js' | relative_url }}?v={{ site.time | date: '%s' }}" defer></script>
