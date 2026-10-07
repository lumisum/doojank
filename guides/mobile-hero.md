# DooJank 竖屏 Banner

## 资源与构图

- 2026-10-07，使用内置 image_gen，以现有全景图为风格与主体参考，生成新的 3:4 竖幅构图。
- 原图：`exec-fc48124a-477c-48fd-b182-b127391e519c.png`；原生成文件保留。
- 网页资产：`assets/doojank/river-hero-portrait.webp`，900×1200；仅等比缩小与WebP压缩，不改画面、不叠字。
- 上部安静墨蓝天空供中英文页面文字使用，下部完整呈现舟客、灯与水面；金色夕照靠近中下部，避免在标题后形成亮斑。

## 方向切换

首页使用 picture/source，条件为 `(orientation: portrait) and (max-width: 1024px)`。手机和窄屏平板竖向窗口加载竖屏图；横向窗口与桌面使用原有全景图。按实际窗口比例判断，不通过设备名称猜测方向；浏览器旋转时自动重新选择图源。两种语言共用无字图片，标题仍为可选择、可检索的页面文字。

竖屏布局单独处理横幅高度、居中标题、文字区域及安全裁切；手机横屏另收紧文字高度，保留全景人物在左、文字在右的安排。宽屏电脑竖向窗口超过1024px仍使用全景资源。经典和文章各自的内容封面保持原画幅。

## 最终提示词

Use case: stylized-concept.
Asset type: a dedicated PORTRAIT mobile website hero background for DooJank, a personal philosophy and life journal named 'a traveler crossing a river'.
Input image: the attached panoramic river landscape is a STYLE AND SUBJECT REFERENCE, not a crop target. Create a NEW complete vertical composition, portrait 3:4.
Preserve the same timeless river traveler, misty limestone mountains, slate ink-blue water, muted pearl fog, warm sunset gold, realistic painterly texture and gentle human warmth.
Composition is carefully designed for a mobile website: TOP 48 percent has quiet dark slate-blue open sky and soft, low-contrast distant mountain mist, generous calm central negative space for live website typography. NO sun or bright cloud directly in this upper central text zone. At about 60 percent down, a modest warm sunset is visible between distant mountain walls. LOWER 30 percent contains a FULLY VISIBLE small wooden ferry and anonymous standing traveler with dark linen cloak, woven conical hat and small amber lantern, viewed from behind, traveler centered slightly to the right, entire boat stays inside central 78 percent horizontal safety. Traveler and boat should be a meaningful small part of vast landscape, not a close-up portrait. Water reflections give depth below the boat, boat bottom around 86 percent so it remains safe in responsive cropping. High distant view with layered mountains on both edges and an open river corridor into the distance. The upper typography area must feel like real atmosphere, not an artificial blank rectangle.
Photographic fine-art landscape with subtle painterly texture, calm spacious philosophical mood, rich but restrained gold. Not technology, not fantasy hero, no weapons.
NO text, no letters, no title, no logo, no UI, no border, no circle inset, no watermark. Finished portrait image 3:4.

