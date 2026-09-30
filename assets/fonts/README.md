# 纯享阅读字体

纯享模式使用基于 **霞鹜文楷 Regular v1.522** 的经文网页子集。

- 官方项目：https://github.com/lxgw/LxgwWenKai
- 原字体：https://github.com/lxgw/LxgwWenKai/releases/tag/v1.522
- 作者：LXGW；基于 Fontworks Klee One。
- 许可证：SIL Open Font License 1.1，允许商用、网页嵌入与随网站分发。完整版权与许可保留于 `OFL-LXGW-WenKai.txt`，不得单独售卖字体文件。
- 本站修改：只保留四部经典原文和标题使用的字符，压缩为 WOFF2；修改版字体家族名为 `Wulai Sutra Kai`。字形没有改绘。
- 字体仅在纯享模式经文与章节标题中使用，浏览器按需加载。未覆盖的新增字使用系统楷体或无衬线字体回退。
- 更新原文后，用 `scripts/build_sutra_font.py` 和官方 Regular TTF 重新生成；构建需要 `fonttools` 与 `brotli`。
