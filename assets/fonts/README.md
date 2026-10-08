# 全站阅读字体

全站中文延续经典纯享模式的霞鹜文楷字形，英文使用 Adobe Source Serif 4。字体随网站托管，不依赖第三方字体服务。

## 中文：霞鹜文楷

- 官方项目：https://github.com/lxgw/LxgwWenKai
- 版本：v1.522，Regular 与 Medium；来源：https://github.com/lxgw/LxgwWenKai/releases/tag/v1.522
- 作者：LXGW；基于 Fontworks Klee One。
- SIL Open Font License 1.1：允许商用、网页嵌入与随网站分发，完整版权与许可保留于 `OFL-LXGW-WenKai.txt`；不得单独售卖字体文件。
- 本站修改：转换为 WOFF2 并按 Unicode 范围分包；修改版内部家族名为 `DooJank Reading Kai`，没有改绘字形。
- 核心包包含 GB2312 常用字符与当前页面使用的原字体支持字符；其余原字体支持字符分为补充包，浏览器遇到对应字符时再加载。中文简繁内容与四部经典共用此字体。
- Regular 用于 CSS 字重 100–499，Medium 用于 500–900。这是两个真实静态字重的映射，不代表提供九个独立字重。
- 使用 `scripts/build_reading_fonts.py regular.ttf medium.ttf` 重建；需要 `fonttools` 和 `brotli`。生成文件位于 `reading-kai/`，文件名带内容哈希以避免旧字体缓存。
- 旧经文子集 `wulai-sutra-kai.woff2` 与 `scripts/build_sutra_font.py` 保留作历史资源；当前全站与纯享模式使用上述共用字体。

## 英文：Source Serif 4

- 官方项目：https://github.com/adobe-fonts/source-serif
- 作者：Adobe，Frank Grießhammer 等；版本 4.005。
- 使用官方发布分支的未修改 Roman 与 Italic 可变 WOFF2 字体，字重 200–900，光学字号 8–60；网页启用自动光学字号。
- 官方字体文件来源：`WOFF2/VAR/SourceSerif4Variable-Roman.ttf.woff2` 与 `WOFF2/VAR/SourceSerif4Variable-Italic.ttf.woff2`。
- SIL Open Font License 1.1：允许商用与网页嵌入；完整版权与许可保留于 `OFL-Source-Serif-4.md`。

## 页面应用

默认布局加载 `reading-kai/reading-kai.css` 与 `assets/css/typography.css`，覆盖中文、英文首页、文章、导航、表单与经典阅读页面。Latin 字符优先使用 Source Serif 4，汉字使用文楷。字号、行距与阅读模式功能保持原有设置，标题与重点保留更重的字重。

公众号、X 导出的复制正文继续使用平台兼容的字体设置；平台粘贴不会嵌入本站字体文件。
