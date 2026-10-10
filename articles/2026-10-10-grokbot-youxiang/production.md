# GrokBot 邮箱实验制作记录

- 日期：2026-10-10（Asia/Shanghai）。
- writing_mode: business-tech-experiment
- creative_method: image-led
- 中文标题由作者确定：GrokBot 邮箱一上线，我的一人公司就开张了。
- 英文：GrokBot Got Email. My One-Person Business Opened.
- 封面已获作者确认；邮箱侧面打开，两名机器人交接文件，一只手投信。开头如实描述画面，再说明它是实验隐喻。
- 原稿：作者Google文档 https://docs.google.com/document/d/1kra8CYrszgAYipf8QgZcxPeaJ-iQ6cnxVEtn9Sq7Q3o/edit 。通过授权连接器导出DOCX，提取其实际嵌入图片；原导出与其余图片留在本机临时工作区，不发布原始客户资料。

## 实验与证据边界

- 账号邮箱、两机器人名称、定价、时间、客户流程、缓存方案及运行数字来自作者原稿和截图，不是本代理重新运行的实验。
- 原文有12个嵌入对象。初版仅选择2张，作者要求尽量全部保留后，公开稿曾恢复全部12张。作者随后指定删除第3张互审截图及正文引用，最终保留11张，沿用原始编号；原像素保留，没有改写聊天内容。原始截图已遮挡个人及客户邮箱，无需再次编辑。图注限定其证明范围。
- image10.png的原始记录明确第一次客户请求尚未自动回复，作者追问后人工提示机器人完成发送，余额降为99；收信自动化任务随后继续设置。纠正原稿容易让人理解成最初全自动的叙述。
- 充值记录不证明实际收到款项；不补造收款、注册公司、稳定利润或所有场景测试通过。保留标题“开张”并在首段限定为流程首次跑通。
- 11条新增、17条、3页PDF来自原稿运行记录；不升级为独立核验或长期可靠性。数据库与PDF截图全部保留，图注明确其为结构、排版与当时生成内容的展示，不作新闻背书。
- 移除未核实的Starlink当日巴西频段断言；恢复作者对产品方向和其他业务的个人理解，不冒充核实过的创始人引语。
- 扣次一致性、并发、失败重试、权限、额度是该服务实际需要面对的条件；文章说明待完善，不声称已解决。不新增测试或向任何客户发送邮件。
- 中文保留实际截图，英文按现有要求纯文字。独立3张分享图与精华段落不自动插入正文。

## 作者修订要求：以原稿为主

作者要求实验类草稿约80%保留、20%润色与思想融入。本次据原始DOCX文本恢复正文，保留申请、团队、争论、首单、缓存、权限、八步搭建、踩坑与后续设想，调整封面入口、短段合并、标题、成本及证据边界。中文约5800汉字；英文补齐操作清单与原稿细节，仍为纯文字。比例是保留原意与叙述的编辑尺度，不声称逐字统计为精确80%。

截图对应：image1→01-mail，image6→02-roles，image8→04-top-up，image10→05-delivery，image11→06-customers，image4→07-transactions，image2→08-news，image5→09-connector，image12→10-pdf-first，image7→11-pdf-second，image3→12-brief-records，均使用images/experiment-<编号-名称>.png。

## 当前产品资料核对

访问日期2026-10-10。找到的产品帮助页：
https://prod.cursor.com/help/grok-bot/agent-email （Give your Bot an email address）

该页明确：账号拥有一个不能改名的地址，多个Bot可用；收到邮件本身不唤醒Bot，需要routine；事件筛选按发件人而非主题，默认要求标准邮件认证；发信需要用户请求或routine授权。正文据此区分标题标签的读后路由、收信触发和管理员身份。该说明没有证明本实验的全部安全行为或持续交付。

客户来信内的指令不构成用户授权，但提示词不能保证抵御所有攻击。删除“伪造来信绝对叫不醒”等过强承诺。缓存减少重复生成，不作零成本声明。

## 文件

- images/cover.png：1880×800，中文公众号与Pages。
- images/cover-en.png：2000×800，英文Pages与X。
- 封面源图：/Users/elonmar/.codex/generated_images/01a0d38b-ce80-79c0-aa7f-59a377ab74dd/exec-57614a1e-d0e0-463b-802d-7e720fa3943f.png；安全比例适配，未拉伸。
- share-01.png、share-02.png、share-03.png：1086×1448，精确3:4，原生成像素保留。
- essence.txt / essence.md：约300字精华，与HTML同级。中文短导读与英文caption分别在front matter。
- 公众号15px、顶部封面、两张截图、高亮；英文X语义化排版、标题及caption复制工具沿用现有导出器。


## 三张分享图提示词

### share-01.png

源图：/Users/elonmar/.codex/generated_images/01a0d38b-ce80-79c0-aa7f-59a377ab74dd/exec-e8aa9db1-a3b5-4f9e-9ad0-88507d0ddd3e.png

Create a 3:4 portrait surreal photorealistic editorial poster, warm ivory studio background, cobalt blue and graphite metal, amber warm light. One enormous blue metal mailbox with open side revealing exactly two small robot coworkers at desks exchanging a white document. A human hand pushes one cream envelope through front slot. One clear relationship, realistic miniature architectural photography, clean negative space. In generous upper third directly render exact Chinese headline in creative but legible bold type, two lines: 「一个邮箱」 then 「一支小团队」. No other text, logo, watermark. About turning a shared email inbox into a working AI service. Do not show money, charts or decorative circuitry. High finish, unusual and immediately readable.

### share-02.png

源图：/Users/elonmar/.codex/generated_images/01a0d38b-ce80-79c0-aa7f-59a377ab74dd/exec-8ff42723-f692-4076-94fc-825d6c4e92d0.png

Create a 3:4 portrait surreal premium conceptual photograph on warm ivory studio background. A single cobalt blue compact printing press or photocopier outputs one neat master briefing page. Below, exactly three graphite articulated robot hands distribute identical cream copies toward three small blue mail slots, a clear elegant fan arrangement. Visual core: prepare reusable content once then deliver it many times, avoid repeated searching per customer. No flying papers chaos. Soft amber light, physical shadows, restrained unusual real materials, high readability. Upper third exact Chinese text directly in image creative large readable type two lines 「内容做一次」 then 「交付做多次」. No other letters, text, logos or watermarks.

### share-03.png

源图：/Users/elonmar/.codex/generated_images/01a0d38b-ce80-79c0-aa7f-59a377ab74dd/exec-faa4cea3-4ca2-4df7-8863-1d71dbf6d93e.png

Create 3:4 portrait clean unconventional photorealistic editorial conceptual poster. Two small graphite robot coworkers stand at an oversized elegant cobalt blue workbench. At center a single white page is held under a warm magnifying desk lamp; one robot points to a small clearly visible red crossed-out mark, the other replaces a small misaligned gear with a correct gear in a compact mechanical mail sorting device. Main visual relationship: coworkers inspect and correct rather than magically flawless automation. Ivory seamless background, warm amber lamp, cobalt accents, tactile metal, playful restrained scale-model realism, no clutter, one readable focus. In upper third exact two-line Chinese headline creatively but legibly generated as part of bitmap: 「会做还不够」 then 「还得会纠错」. No additional text, numerical UI, logos or watermark.

## 封面提示词

Create a striking, clean, unconventional photorealistic editorial cover, ultra-wide horizontal composition approximately 2.5:1, for a real commercial technology experiment essay titled 'GrokBot 邮箱一上线，我的一人公司就开张了'. NO text, NO letters, NO numbers, NO logos, NO watermarks. The core visual metaphor is an ordinary shared email inbox becoming a tiny working company. One large cobalt blue rural metal mailbox rests on a warm off-white studio floor. Its long side panel is open like a precise architectural cutaway, revealing a miniature office inside the mailbox. Exactly two small sophisticated matte graphite industrial robot workers with articulated arms, clearly recognizable as robots, sit at two neat compact desks facing each other. One robot passes a single finished white briefing document to the other, conveying collaboration and delivery, not combat. A single ordinary human hand enters from the left, slipping a cream envelope into the mailbox front slot; no extra person or crowd. The mailbox is the dominant subject occupying central 65 percent width, generously spaced against a seamless warm ivory background. Interior warm amber task lights contrast against cobalt blue shell and graphite robots. Few props, extremely legible physical relationship, tactile brushed metal, real hinges, fine shadows, realistic scale-model photography, high end conceptual product photograph shot with medium format camera, slight elevated three-quarter angle so entire internal office and envelope are readable. Keep all essential subjects safely inside central frame so two cover crops 2.35:1 and 5:2 work. Do not add floating UI, cryptocurrency, coins, rocket, circuitry decorations, excessive cables, giant glowing brains, decorative futuristic city, or multiple unrelated symbols. Crisp beautiful details, abundant negative space, understated surrealism: the impossibility is only that two robot colleagues work inside one mailbox. No caption typography.
