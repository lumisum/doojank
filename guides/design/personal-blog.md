# 无来个人博客：思想标本馆

## 定位

无来 / Wulai，记录技术、工作、家庭、成长与自我的个人观察。佛法继续作为作者的思考来源，但网站公开定位不再限定为佛法主题。文章按时间呈现，不分组。

## 视觉与信息架构

- 暖纸白 #f4f1eb、墨黑 #202124、钴蓝 #2352cc、少量亮橙 #ed6a34。系统字体使用方正的无衬线中文与英文，不用宋体。
- 首页无字新奇艺术：纸张折成不可能的阶梯与门廊，玻璃轨道与橙色球体构成未知的观看窗口。画面服务个人好奇与观察，不使用通用科技或宗教符号。
- 轨道图形作为品牌图标与 favicon。标题、语言切换、文章导航完整可读。
- 顺序：视觉入口 → 最新文章与完整展览 → 个人介绍与两个二维码 → 紧凑阅读书架 → 轻量访问统计。
- 文章卡片显示完整标题，标题在图片下方；首次观察作为较大展位。后续桌面两列、手机一列，保留公众号和 X 封面比例。
- 搜索按标题与导读即时筛选；无 JavaScript 时文章依然全部可读。动效仅轻微图片缩放与箭头变化，尊重系统减少动态设置。
- 文章页完整封面、左对齐标题与导读、舒适阅读宽度、橙色阅读进度、钴蓝重点与链接。

## 双语言与经典边界

`_data/blog.json` 管理个人博客中英文文案；文章语言切换保持对应文章路径。中文和英文首页共用布局。

`/classics/` 和 `/en/classics/` 全部保留旧主题、导航、字体、配色、阅读模式、音乐与功能。`blog.css`、新页头页尾及交互只加载到经典之外的页面；不改经典资料与阅读脚本。

## 发布

首页 SEO 定位与社交分享图随新博客更新；既有文章链接、内容与封面不因网站重构变更。README 保持历史公开入口，独立于本次 Pages 主题重构。

## 首页图片最终提示词

内置 image_gen 生成。原图1922×818，文件 `assets/blog-hero.png`。

Use case: stylized-concept. Asset type: ambitious personal blog homepage hero artwork, wordless. Visual concept: a museum of ideas, reality seen through unexpected windows. Generate a wide landscape 2.35:1 editorial artwork. Warm ivory infinite studio floor and background. On the RIGHT two thirds, a monumental sculptural sheet of thick warm-white paper folds into an impossible staircase and doorway; within the doorway is a deep cobalt-blue translucent glass orbital ring with a small vivid burnt-orange sphere suspended off-center. A tiny dignified human visitor in black stands on the lower paper step, looking into the opening. View from unusual high oblique viewpoint, sculptural optical illusion but readable geometry, beautifully rendered tactile paper edges, refractive cobalt glass, soft museum daylight, subtle shadows. The LEFT third is generously EMPTY warm ivory space with only a delicate shadow, for website heading placement outside the image. Explore human curiosity and the relationship between thought and reality, not spirituality or doom. Extremely distinctive art direction, restrained gallery aesthetics, no busy fantasy environment. ONE major sculptural relationship, no literal robot or brain or laptop. Important objects do not touch the frame edges. No text, titles, letters, numbers, logo, watermark, religion symbols.
