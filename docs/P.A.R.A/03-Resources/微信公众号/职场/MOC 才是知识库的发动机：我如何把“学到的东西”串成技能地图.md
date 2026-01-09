# MOC 才是知识库的发动机：我如何把“学到的东西”串成技能地图

  


# MOC 才是知识库的发动机：我如何把“学到的东西”串成技能地图（知识库 v1.0｜3/5）

你好，我是一只阿木木，后端程序员，用工程师思维折腾 Obsidian。

AI 时代，我不想只当更快的 coder，更想系统经营自己的认知资产。

这里我会用「AI + Obsidian + 产品思维」搭建个人知识系统：

  * • 收集：零散输入 → 结构化知识库
  * • 加工：学习/决策/复盘 → 可复用的认知模块
  * • 落地：真实案例 + 具体工作流，方法跑得起来



我会把打造「AI 第二大脑」的全过程拆给你看。  
如果你也想让知识真正为自己打工，一起来。

## 开篇

你有没有这种体验：  
Obsidian 里明明记过“慢 SQL”“线程池”“缓存一致性”，但当你线上真的遇到问题，脑子里只有一句——“我好像写过”，然后开始全库搜索、翻几十条结果、点开又关掉，最后还是回到搜索引擎。

问题通常不在你记得少，而在你的笔记缺一个东西：**入口** 。

我把这个入口叫 **MOC** （Map of Content）。在 v1.0 里它就是知识库的发动机：负责把碎片笔记串成“能走的路径”，让你在需要的时候，能快速从“我写过”到“我用上”。

* * *

## 1）MOC 到底是什么：不是目录，是“技能 README”

很多人把 MOC 写成目录：

  * • A 笔记
  * • B 笔记
  * • C 笔记



这种 MOC 最容易变成坟场：越写越长、越看越累、越不更新。

我对 MOC 的定义更偏工程化：

> **MOC = 一项技能的 README + 作战手册**  
>  它回答三件事：我为什么学？要学到什么程度？遇到问题我从哪儿开始？

如果你是后端程序员，你可以把 MOC 当成：

  * • 这项技能的“导航页”
  * • 你未来排障/面试/方案评审时的“第一入口”
  * • 你写公众号/做分享时的“大纲生成器”



* * *

## 2）v1.0 的知识库层级：索引 → MOC → 卡片 → 项目复用

你只需要记住这条链路（建议画成图贴在 Home）：

text
    
    
    Index-Skills（总入口）  
       ↓  
    某个技能 MOC（导航页）  
       ↓  
    可复用卡片（问题卡/方案卡/概念卡/复盘卡）  
       ↓  
    Projects（在真实项目里用起来）

  * • **Index-Skills** 解决“我有哪些技能入口”
  * • **MOC** 解决“这项技能我怎么学、怎么用”
  * • **卡片** 解决“可复用的最小单元”
  * • **项目** 解决“落地与复利”（否则永远停在学习）



* * *

## 3）MOC 怎么写才不烂尾：只写 5 块内容

下面是我推荐的 **MOC 最小模板** 。字段很少，但每个都指向“复用”。

你可以直接复制成：`10-Notes/Index-Skills/SQL-性能优化-MOC.md`（放哪都行，关键是你能从 Index-Skills 进来）

Markdown
    
    
    # SQL 性能优化 - MOC  
      
    ## 1. 使用场景（我为什么需要它）  
    - 线上慢查询排查  
    - 面试：索引、执行计划、优化思路  
    - 方案评审：查询模型/索引设计 trade-off  
      
    ## 2. 掌握目标（v1.0 到什么程度算够）  
    - 能独立完成：定位慢在哪里 → 解释原因 → 给出可回滚的优化方案  
      
    ## 3. 学习路径（从浅到深，只保留“可走的路线”）  
    1) 基础：索引、回表、覆盖索引  
    2) 诊断：慢日志、EXPLAIN、关键指标  
    3) 常见模式：排序分页、范围查询、联合索引  
    4) 实战复盘：把真实慢 SQL 写成问题卡/复盘卡  
      
    ## 4. 可复用卡片（这里放“能直接拿去用”的东西）  
    ### 问题卡  
    - [[如何定位慢 SQL：一套排查路径]]  
    - [[排序 + 分页深翻页：三种优化方案对比]]  
      
    ### 概念卡  
    - [[覆盖索引是什么：如何判断是否回表]]  
    - [[EXPLAIN 关键字段：type/rows/extra 怎么看]]  
      
    ### 方案卡 / 复盘卡  
    - [[P-订单服务-方案评审-联合索引设计]]  
    - [[P-订单服务-事故复盘-慢查询导致超时]]  
      
    ## 5. 下一步（永远只写 1 条）  
    - [ ] 把“filesort + 回表”整理成一张排查清单

这 5 块内容背后的原则是：

  * • **场景** ：让学习有“用处”
  * • **目标** ：让你知道“到哪儿算交付”
  * • **路径** ：让你知道“下一步是什么”
  * • **卡片** ：让你能“马上复用”
  * • **下一步** ：让 MOC 永远保持活的（而不是写完就放着）



* * *

## 4）MOC 怎么“自动长出来”：一条硬规则 + 三个问题

MOC 最怕你“专门抽一天来整理”。那基本等于宣告失败。

我用的办法很简单：**不集中整理，只做顺手回挂。**

###  硬规则：每新增一张可复用卡，必须回挂一个入口

新增卡片时，强制做一个动作（二选一）：

  * • 挂到某个 **技能 MOC**
  * • 或挂到某个 **项目首页**



只要你坚持这条规则，结构会自己长出来。

### 三个问题：让你的链接永远正确

每写完一条笔记，你问自己：

  1. 1\. 它属于哪个技能？（挂到哪个 MOC）
  2. 2\. 它来自哪个项目场景？（需要挂项目吗）
  3. 3\. 它将来会在什么时刻被复用？（排障/面试/写方案/写文章）



问完这三个问题，你就知道该往哪儿链接，而不是纠结标签和分类。

* * *

## 5）一个真实使用方式：线上问题时，你从哪儿开始

假设你遇到“接口超时”，你可能会在 Obsidian 搜“超时”，结果是一堆日志、碎片笔记、链接不明的随手记。

有了 MOC，你的第一步变成：

  * • 打开 `[[JVM-性能与排障-MOC]]` 或 `[[可观测性-监控日志链路-MOC]]`
  * • 进入“问题卡”区
  * • 直接点 `[[CPU 飙高：排查路径]]`、`[[GC 频繁：如何定位]]`、`[[线程池耗尽：如何判断]]`



这时候你得到的不是“信息”，而是一条**可执行路径** 。  
这就是 MOC 的价值：把“我写过”变成“我现在就能用”。

* * *

## 6）别把 MOC 写成大工程：v1.0 维护规则（2分钟版）

MOC 维护只做两件事：

  * • 本周新增卡片 → 挂回 MOC（1分钟）
  * • “下一步”只保留 1 条（1分钟）



其它所有“我应该把路径写得更完整”“我应该重构目录”——都先别做。  
v1.0 的目标是：**复用先发生** 。

* * *

## 本篇交付：10 分钟搭出你的第一个技能地图

照做就行：

  * • [ ] 在 `Index-Skills` 里选 3 个你最常用的技能：例如 SQL / Redis / JVM
  * • [ ] 给每个技能新建一个 MOC，复制上面的 5 块模板
  * • [ ] 每个 MOC 先挂 2 张卡（没有就新建占位卡）：
    * • 1 张问题卡（排查路径）
    * • 1 张概念卡（能讲清的原理）
  * • [ ] 之后每周只做一件事：新增卡片顺手回挂到 MOC



* * *

## 下一篇（4/5）：我只用 4 种模板，把任何学习沉淀成可复用产出

你现在有了骨架（3文件夹）、有了入口（Index + MOC），还差最关键的“生产标准”：写什么、怎么写，才能稳定产出问题卡/方案卡/复盘卡。

下一篇我会给你一套我长期只用的 **4 种卡片模板** ：字段极少，但逼你写出结论、证据和复用边界。

如果你想直接拿到：

  * • MOC 模板可复制版（含 SQL/Redis/JVM 三套示例）
  * • “问题卡标题库”（排障/面试高频可复用标题）



评论或私信关键词：**v1.0** 。

  


  


  


  
  


你好，我是一只阿木木，后端程序员，用工程师思维折腾 Obsidian。

AI 时代，我不想只当更快的 coder，更想系统经营自己的认知资产。

这里我会用「AI + Obsidian + 产品思维」搭建个人知识系统：

  * • 收集：零散输入 → 结构化知识库
  * • 加工：学习/决策/复盘 → 可复用的认知模块
  * • 落地：真实案例 + 具体工作流，方法跑得起来



我会把打造「AI 第二大脑」的全过程拆给你看。  
如果你也想让知识真正为自己打工，一起来。

  


  


  


  


  


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

![](https://mmbiz.qpic.cn/mmbiz_jpg/VY8tUic4knqfxXgYA7mWpJI4hyWgSbMAhCrEaH07S9ZDclxbvf6zjkksIzhtuQrP1Yzv05q7UIwv4dGKrIFRJCQ/640?wx_fmt=jpeg)

松花酿酒，春水煎茶。

眉上风止，见字如晤。  


  


一只阿木木   


  


  


  

