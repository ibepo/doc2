# AI们数不清六根手指，这事没那么简单。

昨天Grok4发布完以后，我随手刷了一下X。然后看到了一个非常有趣的帖子，来自@lepadphone。![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7I3Pykt2vMUGicsAjIGXs0p98icG5WoFqKFBOcQaicI5Z89rcDmQsVZsyAA/640?wx_fmt=png&from=appmsg)我以为，这就是Grok4的问题，模型能力不太行，把一个恶搞的6根手指，数成了5根。我自己也去测了一下，确实数是5根。![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7IzjdNibBkWcbINGjbiczXQFj0hOYcdSYNXWuibKwhjibvf4fSTG1zdhdoFg/640?wx_fmt=png&from=appmsg)我本来没当回事。直到，我随手扔到了OpenAI o3里，发现，事情开始不对了起来。因为，o3回复，也是5根手指。![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7I6Ft7fvCntZUyNQIR97n4gkmUGz5uBZtqgBNwN9VGiaKrd2AV9OoXDVQ/640?wx_fmt=png&from=appmsg)我瞬间皱了眉头，然后扔给了o3 pro。在推理了48秒之后，还是5根。![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7IJXceE83qPrGSNUOjhhD4KvVx9DPalFllcww0CuQYcrXwXM5mdUrofA/640?wx_fmt=png&from=appmsg)然后我又把这张图扔给了豆包、kimi、Gemini等等所有的有多模态的模型。![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7IjKURUS59AgywgyjxSNaKZmC8bsSSkK9tv6UNIPKGwem0NicXarJWw9w/640?wx_fmt=png&from=appmsg)而无一例外，所有的模型，给我回复的，都是5根。唯独有一个活口，Claude 4，偶尔会回答正确。![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7ITchfY2u1FnVvP0uV9QYjop9oC5DMtkW6YIbW2pCXQ9JduNTHChhUYg/640?wx_fmt=png&from=appmsg)瞬间一股子冷汗就下来了。一个模型数错了，可能是幻觉，所有的模型都数错，那，模型的底层肯定有一些问题。![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7IbNNbwibFGHD2ZdgpEyVEZrrYuYpT3icuznXrceFOphDQf2cLM7jLd2Ow/640?wx_fmt=png&from=appmsg)深夜在群里试图问了一下，结果石沉大海。那就只能靠自己了，再搜了一堆资料，用DeepReaserch做了深度搜索以后，我找到了一篇能完美解答这个现象的论文。《Vision Language Models are Biased》（视觉语言模型存在偏见）![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7IScaWCaGia36ibCg2FtYibvtCTic48unDGibXXmnoakDBCu3YZfBsZbusCXA/640?wx_fmt=png&from=appmsg)这篇论文发表于今年5月29号，至今也才1个多月的时间，还蛮新的。我花了一些时间，连夜学习完了这篇论文，我觉得，还是有一些有趣的知识可以写给大家看看。这篇论文，最核心的观点就是：大模型，其实从来都没真的在看图片。是的，AI们根本就没有用眼睛看世界，它们用的是记忆。我给你举个生活化的例子。我相信大家一定在各种社交媒体上看过一些搞笑的山寨商品。比如，不知道大家有没有买到过这个。![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7I2lraYIT1Ap4Q9v3CVNBcKib2AY5Vxwdh4ibl5LkicajfQ3SyYwKzfrm1g/640?wx_fmt=jpeg)雷碧。你不止能买到雷碧，还能买到农夫山贼，白事可乐。![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7IBNjN1pLKDVwSg9fYRbpaBmeeMFW4QKmN7PAr99uoaX7Kn1FFA755HQ/640?wx_fmt=jpeg&from=appmsg)我相信很多人买到山寨品，除了确实图便宜之外，更多的人，还是因为：没注意细看。因为我们脑子里，看到绿色瓶子的清爽柠檬味汽水，就会非常自然的觉得，哦这是雪碧。但，你的雪碧也可能是雷碧。我们为什么这么容易看错，原因其实特别简单，也特别扎心。因为人类大脑在识别世界的时候，并不总是用眼睛。我们很多时候，凭的都是记忆，或者更准确地说，是一种印象。就像你每天上班会经过一家熟悉的包子铺，你可能从未认真地盯着包子铺的招牌细看，每次走过时，你只会随便扫一眼，确认一下颜色、字体，然后大脑迅速告诉你：“是的，没错，这就是那个你天天滤过的熟悉的包子铺。”直到有一天，这家店铺其他的都没变，但是悄悄的，把招牌从包子铺改成了，勺子铺，说实话，你可能根本不会发现。除非哪天你特别闲，盯着招牌看了几秒钟，你才会忽然惊呼。卧槽，老子的包子店呢？？？这个认知机制，就是人类大脑的快速决策机制。它能帮你迅速处理日常生活中绝大多数无关紧要的信息，避免你陷入无止境的分析和纠结。但这种机制也有代价，那就是容易被偏见蒙蔽双眼。而我们如今引以为傲的视觉理解大模型，正在用一模一样的机制看待世界。在论文《Vision Language Models are Biased》里面，研究人员做了一个特别简单的实验：他们给顶级AI模型看了一张阿迪达斯运动鞋照片，这双鞋上的三条经典斜纹，被悄悄多加了一条，变成了四条。

但当研究人员问AI：“请问这双阿迪达斯鞋上的条纹有几条？”

所有的AI模型，包括Gemini-2.5 Pro、o3、GPT-4、Claude 3.7，通通斩钉截铁地回答：

“3条！”

![VLMs fail to detect subtle changes](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7IZjwWgtpxpK8gELSbZrnicHoMtcQudBT4Jc0LPkRUq1EP6UnpjUNCKTQ/640?wx_fmt=png&from=appmsg)

哪怕你再三强调请只根据图片回答，不要凭印象，AI们依然不为所动，还是固执地回答3条。

还有更好玩的。

研究人员展示了5条腿的狮子、3条脚的鸟、5条腿的大象、3只脚的鸭子、5条狗的腿。

![Dog with 5 legs](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7INl6yhvJevIvsxGspmo5fZLuw3bFHlXRowUt68NFGtSZiblsia5r0Y1vQ/640?wx_fmt=png&from=appmsg)

当时最顶级的大模型们，几乎全军覆没。

可怜的平均准确率，只有2.12%。

100次，才对2次，太离谱了。

数国旗也是，错的惨不忍睹。

![US flag with modified stars](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7IiaOiaj1xCIUF4toFCRK2ICvON7arCTqBDRGcLjcOIgh5PLpgDFGCogHA/640?wx_fmt=png&from=appmsg)

其实这个跟我们买到雷碧的的道理一模一样。

AI在判断图片时，根本没有真的数数或者仔细观察，它们只是在记忆库里迅速翻了一遍曾经看过的无数图像，然后果断地告诉你：

“狗有四条腿。”

“美国国旗有十三道纹。”

“阿迪达斯标志是三条纹。”

AI们的大脑，也陷入了跟我们人类一模一样的陷阱，它们把过去见过的所有图片的记忆，当成了眼前这张图片的真相。

你可以把这些大模型们，想象成一个究极学霸，但这个学霸的学习方式有点特别。他不是通过理解，而是通过阅读和记忆互联网上几乎所有的文本和图片来学习的。

他读了数万亿字的文字，看了几百亿张图片。

通过这种方式，他脑子里建立了一个庞大的知识库或者说世界模型。在这个模型里，一些概念被反复、高强度地关联在一起。

比如：

“天空”这个词，总是和“蓝色”的图片一起出现。

“狗”这个词，总是和有“四条腿”的动物图片一起出现。

“阿迪达斯”的标志，总是和“三条纹”的图片一起出现。

以及，最重要的，**“手”的图片，几乎总是和“五根手指”这个概念一起出现。**

这种高频的关联，在大模型的脑子里，形成了一种极其强大的“先验知识”（Prior Knowledge），或者我们用大白话说，就是一种根深蒂固的**常识** 或者**刻板印象** 。

这种常识在绝大多数情况下都是非常有用的。

但问题来了，当AI遇到一张**与它的常识相悖** 的图片时，会发生什么？这就是上面六指图的精髓所在。![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7Izicibsr0pTxktT3OoxBkzLMvV8MaE2p0s78AmHDibwjIaAb0qVw0gFVMw/640?wx_fmt=jpeg)这张图，在AI眼里，是一个**反事实图像** 。它在挑战AI脑中最坚固的常识之一：“人有五根手指”。于是，一场AI内部的思想斗争开始了。

一边是视觉模块传来的信息：“尼玛，信我啊，我看到了，这图上确实是六根手指，你自己数数，一、二、三、四、五、六。”

另一边是语言和知识模块的强烈抗议：“不可能，绝对不可能！我特么我读过的所有书，看过的所有图，都告诉我人手只有五根手指。这是宇宙真理，你个废物，你肯定是看错了！”

你猜，最后谁赢了？

**答案不言而喻，是那个顽固的刻板印象赢了。**

**AI最终的输出，是它认为正确的东西，而不是它看到的东西。**

**它会忽略掉那个多出来的第六根手指，因为它在AI的知识体系里，是一个不合理的、概率极低的存在。**

**它会觉得，这更可能是一个视觉上的小瑕疵、一个阴影、或者一个角度问题，反正，绝对不可能是一根真实的手指。**

**这些刻板印象是如此的强大，以至于研究人员试图提醒AI认真看图、或者再确认一下你的答案时，AI们的准确率仅仅提高了可怜的2%。**

几乎没用。![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURricGs1p5gPUZ95TFaXGKv7IwV85TjgpYUTMgxskiaN3q0MTia3XBh0Dx7hnibgWxhGoia5onjYUYLvrvQ/640?wx_fmt=png&from=appmsg)看着测试，是不是感觉很好玩？可能会觉得没啥大不了的，无非就是AI傻了一回而已。但是如果你再细想一下，用到工业场景，用到跟安全有关的场景，你大概率能猜到，这玩意引起的后果可能有多严重。

比如说，一家汽车工厂的自动质检系统完全依赖于AI视觉模型去判断流水线上的零件是否合格。

而零件可能因为生产过程中的某个环节出了问题，导致出现了极其罕见的细微裂缝，这个裂缝非常罕见，在AI的庞大数据记忆库中出现的概率极低。

这个时候，视觉模型看到了裂缝，但却坚定地认为：

“不可能，这种零件出现裂缝的概率太低了，它更可能是一个灯光反射、阴影效果，或者灰尘颗粒导致的视觉误差。”

于是AI果断地判断这个零件合格，放行通过质检关口。

几个月后，装配这个零件的汽车在高速路上行驶时，那个微不足道的小裂缝终于发展成了一次严重的机械故障。

最终，车毁人亡。

不止是零件，在面对一个高速路口的人群、医院病人扫描片中的肿瘤、夜晚路上突然出现的小孩，这些视觉理解模型，它们的判断又真的可靠吗？

就像上次我去宁波体验达摩院的AI筛查肺癌，每一个AI给出的判断，都还是需要医生亲自验证一下。

当我们开始过于依赖AI的视觉判断时，当AI偏见不断累积时，总有一天，这个小小的错误，会在某个关键节点上，引发致命的事故。

到那时，再去质问AI为什么数不清六根手指，就已经晚了。

或许，科技越是发达，我们越要清醒地认识到它的盲点。

至少现在看来，在无尽的数据背后，AI们仍然是盲目的。

所以，下次AI再告诉你一张图片中有几根手指时，不妨数数自己的手指，再做决定。

毕竟，只有你自己的眼睛。

现在才是那双。

真正看得清的那双眼睛。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

>/ 作者：卡兹克

>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com
