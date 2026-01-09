---
title: "我用 Obsidian Dataview 做了 6 个实时增长看板"
source: "https://mp.weixin.qq.com/s/vL2ZL6j25-y63bUwxgX84A"
author:
  - "[[一只阿木木]]"
published:
created: 2026-01-09
description:
tags:
  - "clippings"
---
Original 一只阿木木 *2026年1月7日 11:54*

  

## 我用 Obsidian Dataview 做了 6 个实时增长看板

我是一只阿木木，后端程序员。用 **Obsidian + AI + 产品思维 + 工程化工作流** ，把内容型一人公司的「选题-内容-成交-交付-复盘」做成可复用的业务操作系统。

以前我做增长看板有两种结局：

- • 要么在表格里越堆越乱，数据更新靠“想起来就填”
- • 要么在 Notion / BI 里越做越重，最后变成“维护系统的人”而不是“做增长的人”

后来我换了个思路： **增长看板不一定要接入外部数据源** ，只要把每天、每篇内容、每个渠道、每次实验的关键数字写进笔记里，让看板自动汇总就够了。

于是我用 **Obsidian + Dataview** 做了 6 个“实时”（你更新笔记，它就自动更新）的增长看板：轻、快、可复制、可持续。

下面把整套结构、字段、查询语句直接给你，照抄就能用。

---

## 0\. 你会得到什么

6 个看板分别解决这 6 件事：

1. 1\. **增长总览** ：本周核心 KPI 一眼看懂
2. 2\. **内容增长看板** ：哪些内容在涨、哪些在掉、下一篇写什么
3. 3\. **渠道获客看板** ：哪个渠道在“白嫖流量”，哪个渠道在“烧钱不出单”
4. 4\. **留存与复购看板** ：用“最小可用”的方式做 cohort / 复购追踪
5. 5\. **实验看板** ：实验从立项到复盘不再丢、结论可复用
6. 6\. **产出与节奏看板** ：写作/发布/复盘的节奏是否健康

> 说明：这里的“实时”指 **Obsidian 里数据一更新，Dataview 结果自动刷新** （它不是去外部抓取实时数据）。Dataview 的核心能力是把笔记当数据库查询与聚合。见官方文档：Dataview Query Language 与 DataviewJS。\[^1\]

---

## 1\. 最小工程：文件夹 + 3 类笔记

我建议先把库里分成 3 类数据源（越少越能坚持）：

- • `Daily/` ：每天的关键数字（KPI 日志）
- • `Content/` ：每篇内容的表现（内容台账）
- • `Growth/Experiments/` ：每个实验的卡片（实验台账）

你只要坚持“ **每天 1 条、每篇 1 条、每个实验 1 条** ”，看板自然跑起来。

---

## 2\. 统一字段：让 Dataview 能“吃”你的数据

Dataview 支持两种常用写法： **YAML frontmatter** 或 **行内字段** 。我更建议行内字段：写起来快、不打断。

### 2.1 Daily 模板（放在 Daily/2026-01-06.md 这种文件里）

Markdown

```
# 2026-01-06

type:: daily
date:: 2026-01-06

pv:: 0
uv:: 0
leads:: 0
paid:: 0
revenue:: 0

channel_wechat:: 0
channel_xhs:: 0
channel_zhihu:: 0

note:: 今天主要动作/异常解释
```

### 2.2 Content 模板（放在 Content/）

Markdown

```
# 标题：我用 Obsidian Dataview 做了 6 个实时增长看板

type:: content
publish_date:: 2026-01-06
platform:: wechat
topic:: obsidian
stage:: published

pv_7d:: 0
save_7d:: 0
follow_7d:: 0
lead_7d:: 0
pay_7d:: 0

hook:: 文章开头钩子写了什么
cta:: 结尾引导是什么
```

### 2.3 Experiment 模板（放在 Growth/Experiments/）

Markdown

```
# 实验：文章结尾 CTA 从“私信”改成“关键词回复”

type:: experiment
status:: running
owner:: 你自己
start:: 2026-01-01
end:: 2026-01-07

goal:: 提升 leads
metric:: leads
baseline:: 2
target:: 5

result:: 
conclusion:: 
next_action::
```

---

## 3\. 6 个看板：直接复制到你的 Obsidian

下面每个看板都是一个独立页面，比如 `Dashboards/增长总览.md` ，把代码块粘进去就能跑。

---

## 看板 1：增长总览（本周 KPI 一眼看懂）

dataview

```
TABLE
  sum(pv) as "PV",
  sum(uv) as "UV",
  sum(leads) as "Leads",
  sum(paid) as "Paid",
  sum(revenue) as "Revenue"
FROM "Daily"
WHERE date >= date(today) - dur(7 days)
```

如果你想加转化率（Leads/UV、Paid/Leads），用 DataviewJS 更稳：

dataviewjs

```
const pages = dv.pages("Daily").where(p => p.date && p.date >= dv.date("today").minus(dv.duration("7 days")));
const sum = (k) => pages.array().reduce((a,p)=>a+(p[k]??0),0);

const uv = sum("uv");
const leads = sum("leads");
const paid = sum("paid");

dv.table(
  ["周期","UV","Leads","Paid","Leads/UV","Paid/Leads","Revenue"],
  [[
    "近7天",
    uv,
    leads,
    paid,
    uv ? (leads/uv).toFixed(2) : "0",
    leads ? (paid/leads).toFixed(2) : "0",
    sum("revenue")
  ]]
);
```

你会发现： **总览不是为了“好看”，是为了每天 30 秒判断今天该做什么** 。

---

## 看板 2：内容增长看板（决定下一篇写什么）

核心诉求：把“内容表现”从感觉变成排序。

dataview

```
TABLE
  publish_date as "发布",
  platform as "平台",
  topic as "主题",
  pv_7d as "7日PV",
  save_7d as "7日收藏",
  follow_7d as "7日关注",
  lead_7d as "7日线索",
  pay_7d as "7日成交"
FROM "Content"
WHERE stage = "published"
SORT pv_7d DESC
LIMIT 30
```

加一个“选题复用提示”：你会更容易从爆款里拆结构（hook/cta）：

dataview

```
TABLE
  hook as "开头钩子",
  cta as "结尾引导",
  pv_7d as "7日PV",
  lead_7d as "7日线索"
FROM "Content"
WHERE stage = "published"
SORT lead_7d DESC
LIMIT 15
```

---

## 看板 3：渠道获客看板（哪个渠道在贡献增长）

把 Daily 里的渠道字段按周汇总：

dataview

```
TABLE
  sum(channel_wechat) as "公众号",
  sum(channel_xhs) as "小红书",
  sum(channel_zhihu) as "知乎"
FROM "Daily"
WHERE date >= date(today) - dur(7 days)
```

如果你想看“每天趋势”，做一个最近 14 天折线数据表（用表代替图也够用了）：

dataview

```
TABLE
  pv as PV,
  uv as UV,
  leads as Leads,
  channel_wechat as "公众号",
  channel_xhs as "小红书",
  channel_zhihu as "知乎"
FROM "Daily"
WHERE date >= date(today) - dur(14 days)
SORT date ASC
```

增长动作会立刻变清晰： **把精力加到最有效的渠道** ，不要平均用力。

---

## 看板 4：留存与复购看板（最小可用 cohort）

如果你没有完整用户系统，也可以用“线索/成交的二次触达”做简化版留存。

做法：在某个文件夹里记录“客户/线索”卡片（例： `CRM/` ），每条记录至少有：

Markdown

```
type:: lead
name:: 张三
first_date:: 2026-01-02
pay_date:: 2026-01-15
source:: wechat
```

然后看“近30天新增线索来自哪里”：

dataview

```
TABLE
  source as "来源",
  count(rows) as "新增线索"
FROM "CRM"
WHERE type = "lead" AND first_date >= date(today) - dur(30 days)
GROUP BY source
SORT "新增线索" DESC
```

再看“近90天成交的复购/转化情况”（这里用有无 pay\_date 作为最小闭环）：

dataview

```
TABLE
  count(rows) as "线索数",
  sum(choice(pay_date, 1, 0)) as "成交数"
FROM "CRM"
WHERE type = "lead" AND first_date >= date(today) - dur(90 days)
```

这不是完美 cohort，但足够让你回答两个关键问题：

- • 新增主要从哪里来？
- • 成交跟着哪条链路走？

---

## 看板 5：实验看板（增长最怕“做了就忘”）

dataview

```
TABLE
  status as "状态",
  owner as "负责人",
  start as "开始",
  end as "结束",
  metric as "指标",
  baseline as "基线",
  target as "目标",
  next_action as "下一步"
FROM "Growth/Experiments"
SORT status ASC, start DESC
```

再做一个“只看进行中 + 快到期”的列表：

dataview

```
LIST
FROM "Growth/Experiments"
WHERE status = "running" AND end <= date(today) + dur(3 days)
SORT end ASC
```

你会明显减少一种隐形浪费： **实验没有复盘、结论没沉淀、同样的坑反复踩** 。

---

## 看板 6：产出与节奏看板（让增长回到“可持续”）

你可以把 Daily 里加两三个字段：

Markdown

```
publish:: 0
write_minutes:: 0
review:: 0
```

然后汇总近 7 天：

dataview

```
TABLE
  sum(publish) as "发布次数",
  sum(write_minutes) as "写作分钟",
  sum(review) as "复盘次数"
FROM "Daily"
WHERE date >= date(today) - dur(7 days)
```

再列出近 14 天每天的执行情况，看看你的节奏是否断裂：

dataview

```
TABLE
  publish as "发布",
  write_minutes as "写作",
  review as "复盘"
FROM "Daily"
WHERE date >= date(today) - dur(14 days)
SORT date ASC
```

增长很多时候不是“缺方法”，是“断节奏”。这个看板专治断更、断复盘、断动作。

---

## 4\. 让它真的好用的 3 个小技巧

1. 1\. **字段名固定，不要今天 pv 明天 pageview**  
	Dataview 是查询，不是魔法，字段统一就是一切。
2. 2\. **看板只放“决策需要的指标”**  
	指标越多越像“自我安慰仪表盘”。
3. 3\. **每天 2 分钟补齐 Daily**  
	你只要做到“当天填当天”，看板就会像活的一样。

---

## 5\. 你可以直接照搬的看板目录

- • `Dashboards/增长总览.md`
- • `Dashboards/内容增长.md`
- • `Dashboards/渠道获客.md`
- • `Dashboards/留存复购.md`
- • `Dashboards/实验管理.md`
- • `Dashboards/产出节奏.md`

把上面的代码块分别贴进去，就完成了。

---

## 一人公司：内容→成交→交付，在 Obsidian 里跑起来

你好，我是一只阿木木，后端程序员。  
我关注的不是“收藏更多笔记”，而是把笔记变成 **一人公司可以反复使用、越用越值钱的系统资产** 。

很多内容型一人公司（创作者、咨询顾问、教练、服务型自由职业者）卡在同一件事上：  
内容靠灵感，成交靠解释，交付靠体力，复盘靠感觉。越忙越乱，越努力越不可持续。

我做的事情很明确：  
用 **Obsidian + AI + 产品思维 + 工程化工作流** ，把你的「选题-内容-成交-交付-复盘」搭成一个可运行的业务后台，让你从“手工作坊”升级为“操作系统”。

这个后台通常由五个模块组成（也是我在公众号里会持续公开的核心框架）：

1. 1\. **用户洞察库** ：长期收集读者/客户原话、痛点、反对意见与触发点，让选题稳定、表达更精准。
2. 2\. **内容复用系统** ：把观点、案例、比喻、证据做成模块，一篇文章可以复用成系列、产品页、成交话术与交付材料。
3. 3\. **产品卡/FAQ** ：把“卖什么、适合谁、不适合谁、怎么开始、常见顾虑”写清楚，减少私聊解释，让转化路径更顺。
4. 4\. **SOP/模板库** ：把交付标准化，缩短交付时间，降低重复劳动，并为复购与转介绍打基础。
5. 5\. **复盘看板** ：每周能看见自己缺什么证据、该补什么内容、哪个环节在漏，从“凭感觉努力”变成“按系统迭代”。

在这里你会看到的不是空泛概念，而是能落地的东西：  
结构图、模板、字段设计、工作流、踩坑复盘，以及我如何把它们串成一条能转化、能交付、能复利的链路。

**一人公司不靠努力，靠操作系统。**

我会把全过程用真实案例拆解：结构、模板、工作流、踩坑复盘都公开，让方法真正跑得起来。

如果你也在做内容获客、靠交付变现，欢迎关注我，一起把业务搭成能长期运转的系统。

![Image](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

  

  

  

  

  

AII

AI 产品经理

[2025年，我对AI工程师的硬核要求清单（全技能图谱）](https://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485724&idx=1&sn=a44a2dc1fc0fa9d752c78eb7fc31e407&scene=21#wechat_redirect)

[深度解析：京东云开源的JoyAgent，如何构建一个真正的企业级智能体平台？](https://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485726&idx=1&sn=cf51865fd36919f8013dfaaaa2390974&scene=21#wechat_redirect)

[我对 AI 产品经理的要求 | 2025 能力栈](https://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485755&idx=1&sn=09a8d1cd4c40874d381f0eb9daf46579&scene=21#wechat_redirect)

AI智能体合集

[5分钟搭建智谱清言AI智能体，高效又便捷！](https://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485613&idx=1&sn=0931979aaf9b6b6dee7e29d32ef7ccc9&scene=21#wechat_redirect)

AI工具合集

[流量争夺战：国产AI的推广之道](https://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485509&idx=1&sn=f5813a0003447cf5a4c98230ae5b96cb&scene=21#wechat_redirect)

[kimi AI从新手到高手，一篇文章全搞定](https://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485504&idx=1&sn=4807b73542ae48569067622ab2280cdf&scene=21#wechat_redirect)

[5分钟速成课：豆包AI使用指南](https://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485485&idx=1&sn=fe8a2ae9e3966b7f5569a59564d71cdf&scene=21#wechat_redirect)

[当AI穿上白大褂：清华AI医院的42位数字医生](https://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485474&idx=1&sn=0b09b89abb333381aa3756a94fef85ac&scene=21#wechat_redirect)

[你的业务流程完美了吗？豆包AI揭示隐藏的潜力](https://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485472&idx=1&sn=d48d7a7c430a07556864211c30a0f739&scene=21#wechat_redirect)

AI 提示词实践合集

[AI写作背后的秘密：情感爆文是如何诞生的？](http://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485316&idx=1&sn=1a3db7814ff3abe952673aa77d6c9258&chksm=e8e11c02df96951476e930b13be7e675a9587b88c4cc0a883fbc22108bdefb87a4cc6b502115&scene=21#wechat_redirect)

[九个步骤，用AI写书并赚取你的第一桶金！](http://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485313&idx=1&sn=60c7140425d8181ec6cb4437039c6ea5&chksm=e8e11c07df9695113324b63dc98a0755c3a7e1f630997b9a6197c2284d9ce4edfbe241d4b9db&scene=21#wechat_redirect)  

[为什么你的故事类文章总是缺乏吸引力？AI 写作的创作秘诀](http://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485301&idx=1&sn=6541d0a14daa15985ea3e13346dcddfb&chksm=e8e11cf3df9695e506f58ace63f4d04972738ae2bb3e00c2fa7ce96a41919135581703820a36&scene=21#wechat_redirect)  

[AI 笔下的浪漫：AI 比人类创作的小说更动人？](http://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485296&idx=1&sn=a8723be0d474f734fa2c3ae35288d3ac&chksm=e8e11cf6df9695e0f9ebdc192073ec4789e40aa76d171e472f2f76cca541d2c958814b3de765&scene=21#wechat_redirect)  

[6个步骤，一步步教你仿写董宇辉风格的城市名片文案，精准传达城市魅力](http://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485292&idx=1&sn=49f99af3ad12095d226aa5856220cb7d&chksm=e8e11ceadf9695fca8c10cc1981ec640e2433b8d96b4b8f87b917859c62dc80ec0c5844dc540&scene=21#wechat_redirect)  

[如何让文案更具说服力？一步步仿写董宇辉文案，让你的文字更有力量！](http://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485274&idx=1&sn=73c9019e7eb9ae37ae8e3c6d402253f3&chksm=e8e11cdcdf9695ca35e91c05d00165ffa72464ce6cfd14dda13ca31a8d81af4c3851a3d87610&scene=21#wechat_redirect)  

[1个简单案例，让AI变得更有人情味](http://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485247&idx=1&sn=26b8abf16255f092935cd075ed8684e3&chksm=e8e11cb9df9695af746464e64d9c786f7b80054b3f4f2c32c435ba4268ff7194cb2d73342f61&scene=21#wechat_redirect)  

[1个案例，让你的提示词告别平淡无奇](http://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485235&idx=1&sn=c3bc76fe66652b669158f36bc016228c&chksm=e8e11cb5df9695a31870d3b2a9cb06fb96f1babe0a953355b94f1f9ae6ae2a3468ab731fd88c&scene=21#wechat_redirect)  

[项目经理的时间管理秘籍，你真的了解吗？](http://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485215&idx=1&sn=ad0f9aabbb39b3b7b106a46472f87488&chksm=e8e11c99df96958fc8afcdc5378b75f48c5cfe91c16d529c50549577a2b3970317d8ab9d1409&scene=21#wechat_redirect)  

[项目经理如何轻松管理海量资料？AI工具的秘密在这里](http://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485191&idx=1&sn=4681fe1775f2ad478a1d4ee04caf19e5&chksm=e8e11c81df9695979d2e10785bdb501a0d72d84e590157200b196559ed7d0389c856c1d2160d&scene=21#wechat_redirect)  

[AI提示词背后的秘密，项目经理你真的了解吗？](http://mp.weixin.qq.com/s?__biz=MzIzNTg4NDI2NQ==&mid=2247485179&idx=1&sn=32e5f4d088a2fe7c5c91a0f43db5d919&chksm=e8e11d7ddf96946b4bd731ef9363f025fc914b9bd6c39a38ace39f33cf90918b109f523c5514&scene=21#wechat_redirect)

![Image](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

松花酿酒，春水煎茶。

眉上风止，见字如晤。  

  

一 只阿木木  

  

  

  

作者提示: 个人观点，仅供参考

继续滑动看下一个

一只阿木木

向上滑动看下一个