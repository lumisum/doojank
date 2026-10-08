# DooJank · 踱江客

网站对外品牌为 **DooJank**；2026-10-08起，中文名称由「渡江客」改为 **踱江客**。「踱」指缓步而行，强调从容观察的气质；「江」延续网站的山水意象。定位是哲学、人生与日常观察的个人博客。渡江是贯穿视觉的隐喻：人经历变化，在两岸之间继续看、继续问。以参考图的木舟、旅人、远山、灯与夕照形成记忆。

## 语言与链接

- `/`直接呈现英文首页，不按浏览器语言自动跳转。
- `/zh/`为中文首页，两版在导航中互切。
- `/en/`作为旧英文首页兼容入口，转往根目录并保留查询参数与锚点。
- 中文与英文文章的现有路径继续使用；返回首页指向对应语言。canonical、hreflang、x-default和sitemap与新入口一致。
- 公众号二维码目前对应原公众号「无来」，网站改名不代表公众号也已经改名，保留准确标签。
- 写作方法的已有名称与技能目录属于工作流程，本次不因网站改名擅自更换。

## 视觉

- 墨蓝 `#20323C`：导航图标、页脚与景深。
- 暖纸 `#F7F4ED`：页面与阅读背景。
- 雾灰 `#687478`：摘要、旁注与轻层次。
- 夕照金 `#996B34`：链接、重点与细线；浅金 `#B88D52`作边缘，不作为白底小字主色。
- 深墨 `#24343B`：标题；正文 `#35464E`。
- 全站中文采用霞鹜文楷，延续经典纯享模式的字形；英文采用 Adobe Source Serif 4，标题、正文与界面统一使用。两者均以 OFL 许可随站本地托管，保留常规、强调与英文斜体层级；中文按字符范围加载。字体来源、版权与重建规则见 `assets/fonts/README.md`。
- 全幅河山横幅，人物在左、文字在右；小圆头像从纸面接住横幅。上方保留四部经典封面，桌面四列；文章按时间桌面三列、平板两列、手机单列，标题不截断。
- 文章页保留封面入口、舒服的阅读宽度、自然段、可辨识链接和阅读进度。经典内部原有青松绿、阅读模式和音频功能继续沿用。
- 悬浮反馈使用图片轻微缩放、细线与文字颜色。尊重减少动态设置。
- 公众号和X复制页同步暖纸与墨色署名，正文复制不含背景。公众号15px、X语义化复制规则继续执行。

## 新图

三幅由内置image_gen生成。参照作者提供的 `b4c8f6b2-5337-45eb-8edb-a71e1df19d22.png` 的山水、舟客与色彩关系，制作无文字新横幅和旅人头像；俯瞰江面图用于关于区。图片中的人物为匿名象征，不作为作者真实肖像。

- `assets/doojank/river-hero.webp`：2160×720，3:1；原生成图 `exec-34809076-39f9-4650-9854-73cfc689beb2.png`。
- `assets/doojank/traveler.webp`：600×600；原生成图 `exec-f7a56106-8b27-4875-8b0e-9792b0ddc760.png`。
- `assets/doojank/river-perspective.webp`：800×1000，4:5；原生成图 `exec-a6ebe61b-4754-4805-87ca-d0a56ad0d804.png`。

检查原图后仅做安全比例适配、等比缩放与WebP压缩，主体不拉伸、不叠字。网站名称、标语由页面文字呈现，适应两种语言、搜索与辅助阅读。

## 生成提示词

### hero

Reinterpret the attached reference as a cinematic website hero landscape for DooJank, a philosophical personal journal named 'a traveler crossing the river'. Use the reference's karst mountain river, cloaked anonymous ferryman with woven conical hat, wooden boat, small amber lantern, twilight gold light and layered mist. Create a NEW finished seamless full landscape image, wide panoramic 3:1. Remove ALL words, lettering, logos, circles, inset avatar frames, white bands, and UI from the reference. The ferryman and wooden boat occupy the LEFT third, visible fully, small enough that the vast landscape matters more than the person. Sunrise/sunset gold reflection near center; RIGHT third contains atmospheric quiet slate-blue mountains and soft open sky suitable for live ivory website typography. Realistic fine-art landscape photograph meets delicate painterly oil texture, timeless, contemplative, high-end literary journal, not fantasy warrior, not technology, no swords or neon. Deep desaturated ink-blue water, warm apricot gold light, pearl grey fog, natural charcoal cloak. Impressive spacious perspective and real water texture, sophisticated restraint, no excessive glowing magic. Panoramic composition with generous edge safety. NO TEXT anywhere. NO avatar inset or layout elements.

### avatar

Create a square editorial portrait illustration for a philosophical personal journal, matching the attached landscape reference. A solitary anonymous river traveler viewed FROM BEHIND, dark charcoal linen cloak and woven conical hat, standing calmly at the stern of a small wooden boat with a tiny warm lantern. He is a traveler, no sword, no weapon, not an identifiable historical person. A wide river and distant layered karst mountains fade into slate-blue fog with golden sunset at horizon. Crop composition specifically for a circular avatar: conical hat, shoulders, lantern and boat stay within the central circle-safe 72 percent; head near middle upper third. Fine-art cinematic painterly realism, tactile quiet details, deep blue-grey, apricot amber, fog pearl, elegant warmth, not fantasy or tech. Square 1:1, no inset frames, NO text, NO logo, no watermark.

### perspective

Create a fine-art editorial image for the about section of DooJank ('a traveler crossing the river'), a personal philosophy and life journal. View from a high aerial TOP-DOWN perspective over a broad calm slate-blue river. A single small wooden ferry carrying one anonymous cloaked traveler is crossing diagonally from lower left toward upper right. Its restrained golden lantern makes a tiny warm mark and a faint elegant wake. Misty limestone islands and riverbanks form an organic imperfect circular opening around the boat, suggesting a wider view, a crossing, and room for questions. A small late-day golden reflection brushes the water on one side, atmospheric pearl fog, muted ink navy, soft river grey, ochre warmth. Thoughtful quiet photographic realism with subtle painterly grain, high-end literary magazine, no fantasy structures, no futuristic elements. Vertical 4:5 composition, beautiful negative space and tactile natural water. NO words, NO letters, NO logos, NO watermark.


## 首页图片加载

首页文章与经典封面采用从现有原图等比缩小的WebP缩略图，按语言保留画面对应关系，不修改或覆盖原图。映射记录在 `_data/doojank_covers.json`，未收录的新文章自动回退到原封面。经典阅读页和文章内部仍使用原始高质量图片。

新增或替换文章封面时，运行 `python3 scripts/sync_cover_thumbnails.py <文章目录名>`，从当前中英文元数据指定的封面等比例生成缩略图并更新映射。新文件名含缩略图内容哈希，图片变化时 URL 随之变化；首页与文章前后导航共用该映射。提交对应新文件与映射，不能只替换文章目录中的原图。

## 仓库更名后的地址

发布期间检测到GitHub仓库已更名为 `lumisum/doojank`。网站正式地址为 `https://lumisum.github.io/doojank/`，中文首页为 `/doojank/zh/`。配置baseurl、Git远端、README及文章中的站内图片地址已同步；文章相对路径保留。GitHub Pages不会为旧 `/wulai/` 自动保留站点跳转，因此对外分享使用新地址。


## 2026-10-07第二轮视觉审视

依据线上1280px首页和当前模板，围绕作者的山水、人文、开阔与温度偏好改进：

| 观察到的问题 | 本轮处理 |
| --- | --- |
| 横幅右侧小字与落日亮部重叠，9–11px文字及细线入口偏弱 | 将文字块稍向右收，局部增加墨蓝遮罩；提高字号与对比；阅读入口形成轻薄的半透明按钮，保留真实山水细节。 |
| 文章日期与入口仅9–10px、摘要12px，内容层级偏弱；卡片仅靠底线区分 | 日期10px、摘要13px、入口11px；增加暖纸卡面、细边缘和轻阴影，以纸张的层次呈现触感；桌面仍三列，完整显示标题。 |
| 经典区与展览区留白较散，搜索仅为一条细线 | 收紧两区间距，搜索增加清楚的轻边框与聚焦反馈；四部经典仍放在上部。 |
| 章节导航仅在标记longform时出现，《人生如戏》十一节没有导航 | 所有具有至少三个二级标题的文章自动提供折叠目录；按已有标题生成锚点，正文不新增标题或编号。 |
| 读完后仅能回首页，缺少连续阅读线索 | 增加同语言较新/更早文章入口，展示缩略封面和完整标题；按现有时间顺序关联，不凭空推荐主题。 |
| 正文小标题直接继承大号粗体，阅读页日期仅10px | 小标题收紧到正文1.25倍，以细线形成停顿；日期提高至12px。 |

网页调整不改文章内容，不改经典内部的配色、纯享与音频功能。暂时保留现有封面体系，以排版统一新旧画面。访问统计仍使用原服务；服务暂时不可用时保留真实的未取得数据状态，不伪造计数。

窄屏的横幅裁切向左岸调整，保护舟客在竖向画面中的位置；关于区恢复俯瞰江面插画，以横向窗口呈现，避免手机上丢失“高处看人生”的视觉线索。

## 手机竖屏独立构图

首页已加入900×1200的竖屏山水Banner，以picture媒体条件自动切换。窄屏竖向使用新图，横屏保留全景图；中英文共用无文字资产，图源、方向规则与完整生成提示词见[竖屏Banner](mobile-hero.md)。
