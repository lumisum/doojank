<!--
渡江客微信公众号图文排版稿。封面已置于正文开头；公众号标题和摘要字段可另行填写。
标题：代码越写越快，为什么交付反而卡死？三步判定你的项目上 AI 是赚是亏
摘要：代码产出增加，交付却可能堵在验证环节。先识别项目类型，再看交付瓶颈，最后记录审查与返工时间，算出自己的验证税率。
正文图片和装饰图为网站公开链接；粘贴后请检查图片，必要时在公众号后台重新上传。
-->

<section id="wechat-body" style="background-color:#FFFCF5;color:#35464E;padding:0 0 28px;font-family:PingFang SC,Microsoft YaHei,-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif;"><p style="margin:0 0 24px;line-height:0;"><img src="https://lumisum.github.io/doojank/assets/articles/2026-10-12-ai-biancheng-yanzheng-shui/cover.png" alt="代码越写越快，为什么交付反而卡死？三步判定你的项目上 AI 是赚是亏" style="display:block;width:100%;max-width:100%;height:auto;margin:0 auto;"></p>
<div style="padding:0 24px 8px;">
<p style="margin:2px 0 12px;color:#687478;font-size:12px;line-height:1.5;letter-spacing:2px;text-align:left;">渡江客 · 个人手记</p>
<p id="wechat-title" style="margin:0 auto 12px;color:#24343B;font-size:24px;font-weight:700;line-height:1.5;text-align:left;letter-spacing:0.4px;">代码越写越快，为什么交付反而卡死？三步判定你的项目上 AI 是赚是亏</p>
<p style="margin:18px 0 26px;padding:14px 16px;background-color:#EFEADF;border-left:2px solid #996B34;color:#687478;font-size:14px;line-height:1.8;text-align:left;">代码产出增加，交付却可能堵在验证环节。先识别项目类型，再看交付瓶颈，最后记录审查与返工时间，算出自己的验证税率。</p>
<p style="margin:26px 0;border-top:1px solid #DCD6CA;line-height:0;font-size:0;"></p>
<p style="margin:34px 0 18px;padding-left:12px;border-left:3px solid #B88D52;color:#24343B;font-size:18px;font-weight:700;line-height:1.65;"><span style="color:#B88D52;font-size:12px;">◦</span> 一、你的团队是不是这样？</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">上了 AI 编程工具三个月，代码产出肉眼可见地涨了：GitHub 的论文说 Copilot 让开发者快了 55.8%，《Management Science》的论文说用了 AI 的团队每周多完成 26% 的任务。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">但交付呢？没快。评审排队越来越长，返工越来越多。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">这不是你一家的问题。今年 8 月，哈佛一篇 working paper 拿了 718 家公司的数据：代码 +30%、提交 +20%、PR +23%，Jira 的解决率没动，PR 平均评审时间涨了 49%。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">代码快了，交付没快——钱花了，效果没见到。这篇就解决一件事：<strong style="color:#996B34;font-weight:700;">如何快速判定，你的项目用 AI 编程，能不能带来正收益。</strong></p>
<p style="margin:34px 0 18px;padding-left:12px;border-left:3px solid #B88D52;color:#24343B;font-size:18px;font-weight:700;line-height:1.65;"><span style="color:#B88D52;font-size:12px;">◦</span> 二、第一步：30 秒，对号入座</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">问三个问题，按顺序：</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;"><strong style="color:#996B34;font-weight:700;">第一，你的项目要"绝对正确"吗？</strong> 金融、保险、军事这种，正确不是零 bug，而是代码行级的多专家评审通过——正确性在这里是一种共识。而 Vibe Coding 下根本没人持有行级认知。要——<strong style="color:#996B34;font-weight:700;">共识必需型</strong>，现在上 AI，收益为负的概率大。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;"><strong style="color:#996B34;font-weight:700;">第二，验证能不能标准化？</strong> 测试、协议一致性、类型检查，能不能覆盖主要风险？能——<strong style="color:#996B34;font-weight:700;">验证完备型</strong>，AI 的收益是实打实的。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;"><strong style="color:#996B34;font-weight:700;">第三，都不是？</strong> 那就是大多数常规业务系统：<strong style="color:#996B34;font-weight:700;">验证依赖型</strong>。编码量大，验证量同比大；验证的终极标准是"业务方觉得值"，而业务价值没法标准化。这类项目用 AI，能不能赚钱，取决于你愿不愿意配套投入验证。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">30 秒，对上号了。</p>
<p style="margin:26px 0;"><img src="https://lumisum.github.io/doojank/assets/articles/2026-10-12-ai-biancheng-yanzheng-shui/02.png" alt="项目按共识评审、标准化验证与业务验收分为三类。" style="display:block;width:100%;max-width:100%;height:auto;margin:0 auto;"></p>
<p style="margin:34px 0 18px;padding-left:12px;border-left:3px solid #B88D52;color:#24343B;font-size:18px;font-weight:700;line-height:1.65;"><span style="color:#B88D52;font-size:12px;">◦</span> 三、第二步：搞懂大肚子与细脖子</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">以前的软件开发像个圆柱：开发、编码、验证、测试、发布，每段粗细差不多——几十年人工优化出来的。AI 一来，只把编码这段撑成了<strong style="color:#996B34;font-weight:700;">大肚子</strong>，管道变漏斗。验证、发布不同比放大，水流到脖子这儿一定会堵。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">很多人觉得编码快了整体就快了。错。编码快只是把匀速的水流变成<strong style="color:#996B34;font-weight:700;">洪峰</strong>：开发一口气写完 10 个功能，验证那边根本接不住。以前人是"3 个 3 个地做"，开发验证天然并行；现在编码省下来的时间，全变成了验证阶段的排队。约束理论那句话：系统吞吐量永远由最窄的一段决定。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">脖子有两个。<strong style="color:#996B34;font-weight:700;">正确性验证</strong>——"代码做得对不对"，可标准化，AI 能啃。<strong style="color:#996B34;font-weight:700;">价值判断</strong>——"做的是不是对的事"，需求取舍、业务判断、品味，没标准答案，目前还得人来拍板。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">就我看到的，市面上那些惊艳的 AI 编程 demo，几乎全是验证可标准化的任务——幸存者偏差，拿最好情况当了平均情况。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">所以瓶颈一路往上挪：敲代码 → 验证对不对 → 判断做什么。你的项目卡在哪一段，决定了 AI 的钱花得值不值——第一步的三个问题，问的就是这个。</p>
<p style="margin:26px 0;"><img src="https://lumisum.github.io/doojank/assets/articles/2026-10-12-ai-biancheng-yanzheng-shui/01.png" alt="编码产能膨胀后，审查与测试成为漏斗的细颈；正确性与业务价值是两类判断。" style="display:block;width:100%;max-width:100%;height:auto;margin:0 auto;"></p>
<p style="margin:34px 0 18px;padding-left:12px;border-left:3px solid #B88D52;color:#24343B;font-size:18px;font-weight:700;line-height:1.65;"><span style="color:#B88D52;font-size:12px;">◦</span> 四、第三步：算出你的验证税率</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">类型定了，算账。我用的方法叫<strong style="color:#996B34;font-weight:700;">验证税率</strong>：连续三天，记下每次 AI 编程的生成、审查、返工时间，算"（审查+返工）÷总耗时"。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">为什么非得算？我从 2025 年初用 Vibe Coding 到现在，至少在我这两年的体感里，用了 AI 编程，开发人员就不可能真正了解这个系统了——做不到整体概念，做不到文件级，更别说行级。开发人员和系统之间隔了一道<strong style="color:#996B34;font-weight:700;">塑料薄膜</strong>，人变"<strong style="color:#996B34;font-weight:700;">近视</strong>"了，看不清远处，还没有矫正的眼镜。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">METR 的实验里有个细节：开发者自以为变快了，实测并没有——体感和实测之间有条鸿沟。所以别信体感，算税率。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">今年 1 月 Anthropic 的实验把"近视"测出了数字：52 个初级开发者学一个陌生的 Python 异步库，AI 组理解力 50 分，手写组 67 分，差得最多的恰恰是调试题；AI 组写得只快了 2 分钟，还不显著。作者管这叫"能力幻觉"。不过严谨起见，实验里也有个例外：拿 AI 问概念、要讲解的那组人，理解力跟手写组差不多。也就是说，伤理解力的不是 AI 本身，是拿它当打字机用。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">验证成本其实有两种："人慢"的迟缓成本，"看不懂"的不确定性成本。AI 压缩了前者，制造了后者。<strong style="color:#996B34;font-weight:700;">慢是看得见的成本，看不懂是算不清的成本。</strong></p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">税率多高算危险？我没有标准答案。但连着三天算下来，你心里就有数了——至少比拍脑袋强。</p>
<p style="margin:26px 0;"><img src="https://lumisum.github.io/doojank/assets/articles/2026-10-12-ai-biancheng-yanzheng-shui/03.png" alt="验证税率公式、三日时间记录表，以及迟缓成本与不确定性成本。" style="display:block;width:100%;max-width:100%;height:auto;margin:0 auto;"></p>
<p style="margin:34px 0 18px;padding-left:12px;border-left:3px solid #B88D52;color:#24343B;font-size:18px;font-weight:700;line-height:1.65;"><span style="color:#B88D52;font-size:12px;">◦</span> 五、三个坑，别踩</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;"><strong style="color:#996B34;font-weight:700;">坑一：考核吞吐。</strong> 只考核代码行数、PR 数，就是在激励大家把漏斗入口撑得更大。DORA 2024：AI 采用率每提高 25%，交付吞吐降 1.5%、稳定性降 7.2%；对 10 万 GitHub 开发者的观测：代码活动 +180%，实际发布 +30%。该盯的是评审时长、发布频率、变更失败率。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;"><strong style="color:#996B34;font-weight:700;">坑二：为省成本裁验证的人。</strong> FDE（前沿部署工程师）热起来的逻辑是"编码快=交付快"，典型的拍脑袋。我们公司的项目里：几个人并行用 AI 写代码，各写各的很爽，一到集成测试就炸——接口对不上，数据边界各说各话。<strong style="color:#996B34;font-weight:700;">验证不只在编码之后，设计评审本身就是验证</strong>；拿 AI 评审 AI 的设计，等于<strong style="color:#996B34;font-weight:700;">自己当自己的裁判</strong>。洪峰来了，<strong style="color:#996B34;font-weight:700;">守坝的人还被裁了</strong>，这坝能不垮吗？</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;"><strong style="color:#996B34;font-weight:700;">坑三：指望 AI 评审把脖子拓宽。</strong> 80% 的公司已经在用 AI 评审，但 AI 只产出了 23.3% 的评审意见——人还是主力。评审产能指望 AI 接过去，现在还不行。</p>
<p style="margin:34px 0 18px;padding-left:12px;border-left:3px solid #B88D52;color:#24343B;font-size:18px;font-weight:700;line-height:1.65;"><span style="color:#B88D52;font-size:12px;">◦</span> 六、先说清楚：这个方法不是万能的</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">上面这套判定法，我拿这几个月的新数据验过。结论如下：</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;"><strong style="color:#996B34;font-weight:700;">站得住的三条</strong>：代码涨了 30%、交付没动——漏斗是真的堵上了（哈佛 718 家公司，评审时间 +49%）；编码省下来的时间变成了评审和返工的排队——验证税是真的在收（Code Ninety 的技术债指数对得上）；90% 的人都在用 AI，交付指标却没跟上——采用率不等于收益，是真的。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;"><strong style="color:#996B34;font-weight:700;">要加个限定的一条</strong>："看不懂"比"写得慢"贵——Anthropic 的实验大方向是对的，但有个例外：拿 AI 问概念、要讲解的人，理解力没受影响。所以这条得加限定：伤理解力的不是 AI 本身，是拿它当打字机用。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;"><strong style="color:#996B34;font-weight:700;">我也不知道的两件事</strong>：哈佛那篇还是 working paper，证据本身还要加固；AI 审 AI 到底能不能把评审的脖子拓宽；还有胖圆柱那一天到底多久能到——都没答案。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">方法有边界，用的时候心里有数。</p>
<p style="margin:34px 0 18px;padding-left:12px;border-left:3px solid #B88D52;color:#24343B;font-size:18px;font-weight:700;line-height:1.65;"><span style="color:#B88D52;font-size:12px;">◦</span> 七、我是这么干的</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">写完这篇，我自己想先做三件事：</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;"><strong style="color:#996B34;font-weight:700;">第一，先看验证口径。</strong> 以后接任务，先掂量"它的验证有多标准"——口径越标准，AI 的收益越真；越依赖人的判断，漏斗越堵。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;"><strong style="color:#996B34;font-weight:700;">第二，先算自己的验证税率。</strong> 连续三天，记下每次 AI 编程的生成、审查、返工时间。自己的税率都没算过，谈什么工具选型。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;"><strong style="color:#996B34;font-weight:700;">第三，别拿吞吐当交付。</strong> 只考核代码行数、PR 数，就是在激励大家把漏斗入口撑得更大；真正该盯的是评审时长、发布频率和变更失败率。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">以上三条，是我自己接下来要照着做的。写出来是顺手，你觉得有用就拿去用。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">对了，多说一句：前中后同等比例放大之后，漏斗就不是漏斗了，会变回一个<strong style="color:#996B34;font-weight:700;">胖圆柱</strong>——更粗、吞吐量更大的圆柱。漏斗只是过渡态。不过那是后话了。</p>
<p style="margin:0 0 20px;color:#35464E;font-size:15px;line-height:1.95;letter-spacing:0.25px;">眼下，你的项目，先对号入座吧。</p>
<p style="margin:26px 0;border-top:1px solid #DCD6CA;line-height:0;font-size:0;"></p><p style="margin:0 0 8px;color:#687478;font-size:14px;line-height:1.8;text-align:center;">保持好奇，让思考继续。</p><p style="margin:0;color:#B88D52;font-size:12px;letter-spacing:2px;text-align:center;">渡江客 · 个人手记</p></div></section>
