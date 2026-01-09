# Obsidian 不需要复杂：3个文件夹 + 2个索引页，就够你用到进阶

  


# Obsidian 不需要复杂：3个文件夹 + 2个索引页，就够你用到进阶（知识库 v1.0｜2/5）

你好，我是一只阿木木，后端程序员，用工程师思维折腾 Obsidian。

AI 时代，我不想只当更快的 coder，更想系统经营自己的认知资产。

这里我会用「AI + Obsidian + 产品思维」搭建个人知识系统：

  * • 收集：零散输入 → 结构化知识库
  * • 加工：学习/决策/复盘 → 可复用的认知模块
  * • 落地：真实案例 + 具体工作流，方法跑得起来



我会把打造「AI 第二大脑」的全过程拆给你看。  
如果你也想让知识真正为自己打工，一起来。

## 开篇

上一期（1/5）我讲了“学习→产出”的一条链路：

**输入 → 提炼 → 连接 → 交付 → 复盘**

这期只解决一个更现实的问题：这条链路在 Obsidian 里到底怎么落地？

很多人的 Obsidian 会烂尾，不是因为不努力，而是因为一上来就：

  * • 抄 PARA、抄别人的 vault、装一堆插件
  * • 建十几个文件夹、几十个标签
  * • 追求“完美结构”，导致维护成本爆炸



最后的结局往往是：**Inbox 堆积、找不到、懒得开、弃用。**

所以我的原则很简单：

> v1.0 的知识库只做一件事：让“产出链路”跑起来。  
> 能跑，比好看重要；能复用，比齐全重要。

* * *

## 你只需要这套最小结构：3个文件夹

把你的 Vault 先建成这样（直接复制）：

text
    
    
    00-Inbox/        # 临时输入：先收集，不整理  
    10-Notes/        # 可复用卡片：问题/方案/概念/复盘  
    20-Projects/     # 项目资产：决策记录、日志、复盘

为什么是这三个？

  * • **00-Inbox** ：降低记录摩擦，让你“先抓住”
  * • **10-Notes** ：承载“可复用模块”，是知识复利的核心
  * • **20-Projects** ：把知识接回真实工作场景，不然永远停在“学习很努力”



你会发现：这套结构天然对应上一篇的链路

  * • Capture → `00-Inbox`
  * • Distill/Link → `10-Notes` \+ 链接
  * • Deliver/Review → 通常发生在 `20-Projects`（方案/复盘/交付）



* * *

## 再加 2 个索引页：让你永远“有入口可走”

文件夹解决“放哪”，索引页解决“从哪开始用”。

你只需要两个入口：

  1. 1\. **Home.md** ：你的控制台（行动入口）
  2. 2\. **Index-Skills.md** ：你的技能索引（学习入口）



它们不需要放在任何文件夹里，直接放在根目录就行。

* * *

# 入口1：Home.md（控制台，而不是目录）

Home 页的目标只有一个：**让你今天打开 Obsidian 就能行动** 。

复制这个最小模板（v1.0 够用了）：

Markdown
    
    
    # Home  
      
    ## 本周最小交付（只选 1 个）  
    - [ ] 交付一张卡：问题卡 / 方案卡 / 复盘卡 / 技能地图  
      - 主题：________  
      - 链接：[[ ]]  
      
    ## 我正在进行的项目  
    - [[P-项目A-首页]]  
    - [[P-项目B-首页]]  
      
    ## 我正在学习的技能  
    - [[Index-Skills]]  
    - 本周主题：________  
      
    ## Inbox（周末清空）  
    - [ ] 清空：00-Inbox  
      
    ## 指标（可选，但强烈建议）  
    - 本周新增可复用卡：X  
    - 本周复用次数：Y（写方案/排障/面试表达/写作）

为什么 Home 页要放“本周最小交付”？

因为知识库的成败不在结构，而在你是否持续把学习变成**可复用产出** 。  
Home 页就是你的“产品首页”，只放最关键的动作。

* * *

# 入口2：Index-Skills.md（技能索引，通往 MOC）

先别急着写一堆 MOC。v1.0 先做一个“技能索引总入口”，把常用方向列出来。

复制模板：

Markdown
    
    
    # Index-Skills（技能索引）  
      
    ## 基础能力  
    - [[Java-并发-MOC]]  
    - [[JVM-性能与排障-MOC]]  
    - [[SQL-性能优化-MOC]]  
    - [[Redis-缓存与一致性-MOC]]  
    - [[Linux-排障路径-MOC]]  
    - [[网络-HTTP与RPC-MOC]]  
      
    ## 工程实践  
    - [[系统设计-高可用-MOC]]  
    - [[可观测性-监控日志链路-MOC]]  
    - [[架构决策-Tradeoff-MOC]]  
      
    ## 写作与表达（可选）  
    - [[技术复盘写作-MOC]]  
    - [[面试表达-MOC]]

先占位没关系：你可以先建空的 MOC 文件，后面边写边补。  
关键是：**你给未来的笔记留了“入口”。**

> 下一篇（3/5）我会完整讲 MOC 怎么写、怎么长出来，以及如何避免写成“目录坟场”。

* * *

## Inbox 的唯一正确用法：不整理，但要“按时清空”

很多人最大的坑是：Inbox 越堆越多，然后开始内耗：“我该怎么分类？”

我的做法很暴力：**Inbox 永远只做收集，不做整理。**  
整理只在一个固定时间发生：比如每周日 30 分钟。

你可以照这个 SOP 走：

### Inbox 清空 SOP（每周一次，30分钟以内）

打开 `00-Inbox`，对每条笔记做三选一：

  1. 1\. **能复用** → 移到 `10-Notes`


  * • 补齐：一句话结论
  * • 加一条链接：挂回技能 MOC 或项目页


  1. 2\. **属于项目** → 移到 `20-Projects`


  * • 挂到对应项目首页（后面有模板）


  1. 3\. **没价值/重复/太碎** → 删除


  * • 删除不是浪费，是**降噪升级**
  * • 你的目标是复用，不是保存一切



如果你觉得“删除很痛”，可以先丢一个 `99-Archive/`。但我建议 v1.0 尽量少引入归档复杂度。

* * *

## 命名规则：别花哨，保证你找得到、敢复用

命名的目标是：**检索稳定 + 标题就是结论/问题** 。  
我给你两套命名范式，直接照着用。

### Notes（可复用卡）命名：用“问题句/结论句”

  * • `如何定位 CPU 飙高：一套排查路径`
  * • `慢 SQL 排查：从现象到 EXPLAIN`
  * • `Redis 缓存一致性：三种策略与适用边界`
  * • `线程池参数如何设置：决策清单`



你会发现：这种标题天然适合你未来做输出（写文章/分享/面试表达）。

### Projects（项目资产）命名：统一前缀 + 类型

项目首页建议统一成：

  * • `P-订单服务-首页`
  * • `P-支付链路-首页`



项目内的文档按类型：

  * • `P-订单服务-方案评审-缓存改造`
  * • `P-订单服务-事故复盘-接口超时`
  * • `P-订单服务-周记-2025W01`



这样做的好处：全库搜索 `P-订单服务`，相关资产自动聚合。

* * *

## 让“项目”成为知识复利发动机：项目首页模板

程序员的知识最终要回到项目里，否则就是“懂很多但用不上”。

给你一个项目首页模板（放在 `20-Projects/`）：

Markdown
    
    
    # P-项目名-首页  
      
    ## 背景  
    - 项目一句话：________  
    - 目标/指标：________  
    - 约束：时间/成本/稳定性/一致性等  
      
    ## 进行中  
    - [ ] 本周交付：________  
    - [ ] 风险点：________  
      
    ## 关键资产  
    ### 方案（Decision）  
    - [[P-项目名-方案评审-xxxx]]  
    - [[P-项目名-方案评审-yyyy]]  
      
    ### 事故/复盘（Retro）  
    - [[P-项目名-事故复盘-xxxx]]  
      
    ### 可复用卡（Notes）  
    - [[如何定位慢SQL：一套排查路径]]  
    - [[Redis 缓存一致性：三种策略与边界]]  
      
    ## 时间线（可选）  
    - 2025-xx-xx：______

注意这里的设计：项目页不是“日志堆积”，而是把项目沉淀成三类资产：

  * • 方案：为什么这么做（trade-off）
  * • 复盘：踩坑机制与改进
  * • 可复用卡：能带走的通用能力



这就是你 IP 的“工程师成长”味道。

* * *

## v1.0 的强规则：别让知识库变成装修工程

为了让这套最小结构真的跑起来，我建议你立三条硬规则：

  1. 1\. **所有输入先去 Inbox**  
不许在收集阶段纠结“放哪里”。
  2. 2\. **每条可复用笔记必须满足 2 个条件**


  * • 有“一句话结论”
  * • 至少链接到一个入口（技能 MOC 或 项目页）


  1. 3\. **每周至少交付 1 个产出**  
问题卡/方案卡/复盘卡/技能地图，任选一个。  
你会发现：只要交付开始发生，知识库就不会烂尾。



* * *

## 你可以立刻照做的搭建步骤（10分钟搞定）

  * • [ ] 新建文件夹：`00-Inbox/` `10-Notes/` `20-Projects/`
  * • [ ] 新建 `Home.md`，复制上面的模板
  * • [ ] 新建 `Index-Skills.md`，先写 6-10 个你常用技能入口
  * • [ ] 把你已有的零散笔记先全部丢进 `00-Inbox/`（不要急着整理）
  * • [ ] 设一个每周固定时间：清空 Inbox（30分钟）



* * *

## 下一篇（3/5）：MOC 才是知识库的发动机

有了骨架和入口，下一步就是把“学到的东西”串成体系。  
下一篇我会给你一套可复制的 MOC（技能地图）写法，包括：

  * • MOC 的最小字段（别写成目录坟场）
  * • 每新增一张卡，如何“自动长出结构”
  * • 让 MOC 同时服务：学习、排障、面试表达、写作输出



* * *

如果你想直接拿到本篇所有模板（Home / Index-Skills / 项目首页），以及我用的命名规则清单，评论或私信关键词：**v1.0** 。

  


  


你好，我是一只阿木木，后端程序员，用工程师思维折腾 Obsidian。

  


AI 时代，我不想只当更快的 coder，更想系统经营自己的认知资产。

  


这里我会用「AI + Obsidian + 产品思维」搭建个人知识系统：

  


\- 收集：零散输入 → 结构化知识库

\- 加工：学习/决策/复盘 → 可复用的认知模块

\- 落地：真实案例 + 具体工作流，方法跑得起来

  


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


  


  


  

