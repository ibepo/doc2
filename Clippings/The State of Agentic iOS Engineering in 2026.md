---
title: "The State of Agentic iOS Engineering in 2026"
source: "https://dimillian.medium.com/the-state-of-agentic-ios-engineering-in-2026-c5f0cbaa7b34"
author:
  - "[[Thomas Ricouard]]"
published: 2026-01-02
created: 2026-01-17
description: "The State of Agentic iOS Engineering in 2026 My perspective on AI-driven programming, workflows, and tooling 2025 was an AI-packed year, at least in my case. I don’t recall precisely how many times …"
tags:
  - "clippings"
---
[Sitemap](https://dimillian.medium.com/sitemap/sitemap.xml)

[Mastodon](https://mastodon.social/@dimillian)

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*6U7A_0DCB_YReRif1kV0Xw.png)

2025 was an AI-packed year, at least in my case. I don’t recall precisely how many times I changed my workflow, but I did experiment extensively. All in all, I can say that I’ve never worked so much and yet so little at the same time. You’ll understand what it means a bit later on.  
2025年对我来说是人工智能蓬勃发展的一年。我记不清自己究竟改变了多少次工作流程，但我确实做了很多尝试。总而言之，我可以说，我从未同时投入如此多的时间和精力。稍后你就会明白这意味着什么。

==Keeping up with AI trends is a full-time job, and I’m happy doing it. I’ve been motivated every day to improve my workflow, learn about new tooling, and overall improve my efficiency. It’s improving so fast, and as Andrej Karpathy== ==[said](https://x.com/karpathy/status/2004621825180139522?s=20)====, “People who aren’t keeping up even over the last 30 days already have a deprecated worldview on this topic.” I agree with this statement. I’m not saying you have to, but I love being busy and learning, so keeping up with all this is just one of the things that bring me joy.==  
==紧跟人工智能发展趋势是一项全职工作，但我乐在其中。我每天都充满动力地改进工作流程，学习新工具，并全面提升效率。人工智能的发展速度如此之快，正如 Andrej Karpathy 所说……== ==[说](https://x.com/karpathy/status/2004621825180139522?s=20)== ==“那些连过去 30 天都没跟上的人，对这个话题的看法已经过时了。” 我同意这种说法。我不是说你必须跟上，但我喜欢忙碌和学习，所以跟上这些话题的步伐是给我带来快乐的事情之一。==

This article serves as a comprehensive 2025 debrief; the order of the sections doesn’t matter much, and I hope you’ll find a wealth of information about my workflow, agentic iOS programming, opinions, and much more, extending beyond our iOS world.  
本文是对 2025 年的全面总结；各部分的顺序并不重要，我希望您能从中找到大量关于我的工作流程、智能 iOS 编程、观点等等的信息，内容远不止于 iOS 世界。

## The Deprecation of Xcode as a Text EditorXcode 作为文本编辑器的弃用

As iOS developers, we’re used to Xcode, but let me get this straight: I probably spent only 2% of my time actually in Xcode last year. The only savior was the [GitHub Copilot extension](https://github.com/github/CopilotForXcode). It allows you to get a Cursor-like experience, with fast and relevant AI completion on tab press within Xcode.  
作为 iOS 开发者，我们对 Xcode 早已习以为常，但说实话，去年我真正花在 Xcode 上的时间可能只有 2%。幸亏有了 [GitHub Copilot 扩展](https://github.com/github/CopilotForXcode) 。它能让你获得类似光标的使用体验，在 Xcode 中按下 Tab 键即可获得快速且相关的 AI 代码补全。

*When I say I’m not using Xcode extensively, I mean the Xcode text editor; iOS agentic workflow depends on many Xcode components accessed outside of Xcode, such as Swift LSP for Cursor Swift code highlighting and navigation to work, Xcodebuild for building, etc…  
我说我没有大量使用 Xcode，指的是 Xcode 的文本编辑器；iOS 的代理工作流程依赖于许多在 Xcode 之外访问的 Xcode 组件，例如用于实现光标 Swift 代码高亮和导航的 Swift LSP，用于构建的 Xcodebuild 等等……*

![Screenshot 2025-12-31 at 12.46.21 PM.png](https://miro.medium.com/v2/format:webp/fe14d4083cb16eae65cc5661718d260eaf9870f67855a2deab40517193741750)

Screenshot 2025-12-31 at 12.46.21 PM.png

However, recent updates have cluttered it with weird and broken UI choices, and you must disable most of the features to achieve a satisfactory experience.  
然而，最近的更新导致界面充斥着奇怪且不完善的选项，你必须禁用大多数功能才能获得满意的使用体验。

However, I invite you to try it; it’s probably the most comfortable setup if you want or need to stay within Xcode and enjoy this new AI-assisted programming world without significantly altering your workflow.  
不过，我邀请您尝试一下；如果您想或需要留在 Xcode 中，享受这种全新的 AI 辅助编程世界，又不想大幅改变您的工作流程，那么这可能是最舒适的设置。

You’ll notice I don’t even bring up the local Xcode completion models at this point. Feel free to try them, but in the current race to autonomous programming, they’re irrelevant in their current state.  
你会注意到，我目前甚至都没提到 Xcode 的本地代码补全模型。你可以随意尝试，但在当前这场迈向自主编程的竞赛中，它们目前的状况还无关紧要。

But I do believe that Apple’s stance on running everything locally will pay off in the near future; it’s just not good enough and not evolving fast enough for now.  
但我相信，苹果坚持所有程序都在本地运行的策略在不久的将来会取得成效；只是目前这种做法还不够好，发展速度也不够快。

## Xcode Intelligence

I’ve been using Xcode Intelligence a bit, and my feedback is the same as for the local model. It’s there; it mostly works, but it’s not bleeding-edge at all.  
我试用了一段时间 Xcode Intelligence，我的反馈和本地模型一样。它确实存在，大部分功能也都能用，但完全算不上最前沿的技术。

![image.png](https://miro.medium.com/v2/format:webp/8aed50a64c8ee532c6ee253896ecbfe4f01ffb3497a5f7cc67f4d7e077c5d584)

Xcode Intelligence modal provider modal Xcode Intelligence 模态提供程序模态

The positive point is that you can interface with your own model provider, and so, any API. This is useful if you want to use any of the latest frontier models on your own and pay for API usage.  
优点在于，您可以与自己的模型提供商对接，因此也可以与任何 API 对接。如果您想自行使用最新的前沿模型并支付 API 使用费，这将非常有用。

In my case, this is not what I’m using; I have a $200 OpenAI Pro subscription for my Codex usage.  
就我而言，我并没有使用这个；我订阅了价值 200 美元的 OpenAI Pro 服务，用于我的 Codex 使用。

But you can also connect your OpenAI and Anthropic accounts. So you can enjoy your subscriptions while working in Xcode.  
但你也可以关联你的 OpenAI 和 Anthropic 账户。这样，你就可以在 Xcode 中工作时享受你的订阅服务了。

All in all, Xcode Intelligence is fine. It’s not really agentic programming; it’s designed for short-running sessions and live code editing, allowing you to stay within the flow.  
总而言之，Xcode Intelligence 还不错。它并非真正的智能编程；它的设计初衷是用于短时会话和实时代码编辑，让你能够保持流畅的工作流程。

Apple also makes an effort to inject [custom system prompts](https://github.com/artemnovichkov/xcode-26-system-prompts/tree/main/AdditionalDocumentation) whenever a new API (such as Liquid Glass) is needed that is outside of the current models’ training data.  
每当需要使用当前模型训练数据之外的新 API（例如 Liquid Glass）时，Apple 也会努力注入 [自定义系统提示](https://github.com/artemnovichkov/xcode-26-system-prompts/tree/main/AdditionalDocumentation) 。

But those markdown files are actually handy, I’m using them often in one form or another to inject them at will in my various agents when working with the relevant API.  
但这些 Markdown 文件实际上很方便，我经常以某种形式使用它们，以便在与相关 API 交互时随意将它们注入到我的各种代理中。

Those days, I’m using them for Codex skills, but more on that later.  
最近我主要用它们来学习 Codex 技能，不过以后再详细介绍。

## Terminal interface-based workflow基于终端界面的工作流程

I had a phase earlier in 2025. Claude Code, and later Codex, somehow made terminal-based apps cool again.  
我在 2025 年初的时候有过一段迷恋期。Claude Code，以及后来的 Codex，不知何故让基于终端的应用程序再次流行起来。

Everyone was making one; [Omarchy](https://omarchy.org/) from DHH looked very sexy, and so I embarked on this journey of having a fully terminal-based workflow for programming and working with AI.  
每个人都在做一个；DHH 的 [Omarchy](https://omarchy.org/) 看起来很性感，所以我开始了这段旅程，建立一个完全基于终端的 AI 编程和工作流程。

I landed on [Zellij](https://zellij.dev/), an easy-to-configure terminal workspace.  
我最终选择了 [Zellij](https://zellij.dev/) ，一个易于配置的终端工作空间。

![image.png](https://miro.medium.com/v2/format:webp/c99b6dad03f2b0cff17ff5b9e923197285a10178e557f2ff31506a29963502a6)

I’ve created a layout that I like. The idea was to have the project on one side and a few agents on the other side, along with tabs for reviewing the code and a terminal.  
我设计了一个自己喜欢的布局。我的想法是把项目放在一边，几个代理放在另一边，再加上用于代码审查的标签页和一个终端。

I then [open-sourced](https://github.com/Dimillian/ai-cli) my setup/layout, and basically, I had one instance of this workspace per project I was working on.  
然后我 [将我的设置/布局开源](https://github.com/Dimillian/ai-cli) ，基本上，我为我正在进行的每个项目都创建了一个这样的工作区实例。

It was looking cool, that's what I can say. As a non-terminally ill terminal lover person, this was as much as I could handle. Remembering all those shortcuts at all times was just too much work. But it was fun while it lasted.  
看起来很酷，我只能这么说。作为一个没有绝症的、热爱绝症的人，这已经是我的极限了。要时刻记住所有那些快捷方式实在太累了。不过，那段时光确实很美好。

I believe this is probably the most efficient layout for some. It takes just one second to spawn this layout in any folder and get started. And as today's best agents are Claude Code and Codex CLI, using a terminal-based interface for everything else around them makes a lot of sense.  
我相信这可能是对某些用户来说最高效的布局。只需一秒钟即可在任何文件夹中启动此布局并开始使用。鉴于目前最好的代理是 Claude Code 和 Codex CLI，使用基于终端的界面来处理其他所有操作就显得非常合理了。

## Cursor, the end of IDE as we know it光标，我们所知的 IDE 的终结

![image.png](https://miro.medium.com/v2/format:webp/361d8f3fb90b4d5e93673600f314113d5628946e811d28ed1ed0a56a97e103f7)

My cursor layout 我的光标布局

I’ve been using [Cursor](https://cursor.com/) since its initial release. While it’s a fork of VSCode, it’s going much further with AI integration than VSCode is, even today.  
我从 [Cursor](https://cursor.com/) 最初发布时就开始使用它了。虽然它是 VSCode 的一个分支，但即使在今天，它在 AI 集成方面也比 VSCode 走得更远。

The groundbreaking feature that comes with Cursor is its incredibly fast auto- and tab-completion model. To this day, it’s still their best feature to me. When programming manually, there is nothing else on the market. It can make split-second accurate suggestions, and you can tab tab tab your code away.  
Cursor 最突破性的功能是其速度极快的自动补全和 Tab 键补全模型。时至今日，这仍然是我认为它最棒的功能。在手动编程时，市面上没有任何其他工具能与之媲美。它能提供瞬间精准的建议，让你轻松实现代码的快速补全。

Their second best feature is their new in house models called [Composer-1](https://cursor.com/blog/composer) it’s the fastest coding model I’ve ever used that is not spitting dogshit code.  
他们第二大优点是他们新开发的内部模型 [Composer-1](https://cursor.com/blog/composer) ，它是我用过的最快的编码模型，而且不会生成垃圾代码。

It’s been my go-to model when I want to stay in the flow, it’s the model I use when I want to ask for a more minor code edit or query a codebase etc… it’s also a good model to execute a solid plan reviewed or made by Codex.  
当我想保持工作流程顺畅时，这是我的首选模型；当我想请求进行较小的代码修改或查询代码库等时，我也会使用这个模型；它也是执行 Codex 审核或制定的可靠计划的好模型。

If you’re manually programming and editing code and need an agent to do fast and small refactoring so you can stay in the flow, give it a try!  
如果你正在手动编写和编辑代码，并且需要一个代理来快速进行少量重构，以便你能保持流畅的工作流程，那就试试吧！

In terms of iOS programming within Cursor, there have been no significant changes. I’m still using Sweetpad, and I have shortcuts for building and launching the app in the simulator. You can read more about it in a previous article I wrote [here](https://medium.com/@dimillian/how-to-use-cursor-for-ios-development-54b912c23941).  
就 Cursor 的 iOS 编程而言，并没有发生重大变化。我仍然使用 Sweetpad，并且设置了在模拟器中构建和启动应用的快捷方式。你可以在我之前写的文章中了解更多信息（链接 [在此）](https://medium.com/@dimillian/how-to-use-cursor-for-ios-development-54b912c23941) 。

Honorable mention to [Flowdeck](https://flowdeck.studio/), a sweetpad replacement with more and better features, as well as a more robust debugging experience. I plan to play with it more this year.  
值得一提的是 [Flowdeck](https://flowdeck.studio/) ，它是一款功能更丰富、性能更优的 Sweetpad 替代品，调试体验也更加强大。我计划今年多花些时间体验一下。

Cursor has been my home for a while now, and as I’ve been trying other flows, I always come back to it. Because in the end, it’s the most straightforward interface to see and navigate the code, see the git diff, the cursor agents, and run any number of Codex terminals per project.  
Cursor 一直是我的首选工具，虽然我也尝试过其他流程，但最终还是会回到它。因为归根结底，它是查看和浏览代码、查看 Git 差异、查看 Cursor 代理以及为每个项目运行任意数量的 Codex 终端的最直接界面。

As you might see on the screen above, I’m using the Cursor UI for the agents (mostly Composer-1) but also (and mostly) the terminal version of Codex in the bottom part of the window.  
如您在上图中看到的，我使用了 Cursor UI 来控制代理（主要是 Composer-1），但也（主要是）在窗口底部使用了 Codex 的终端版本。

## XcodeBuildMCP

![Screenshot 2025-12-31 at 1.48.44 PM.png](https://miro.medium.com/v2/format:webp/1d955630de599a6b09aff38b41c2c31d8100434b92ba081c4a5d8afc0cc8f6c9)

Screenshot 2025-12-31 at 1.48.44 PM.png

One of the big pieces of the puzzle for a fully agentic iOS workflow is how to interface with Xcodebuild and the simulator.  
实现完全智能化的 iOS 工作流程的关键部分之一是如何与 Xcodebuild 和模拟器进行交互。

My experience is that even the latest Codex 5.2 model makes numerous mistakes when using xcodebuild directly in a project with a large number of schemes, packages, etc.  
我的经验是，即使是最新的 Codex 5.2 模型，在包含大量 scheme、包等的项目中直接使用 xcodebuild 时也会出现很多错误。

Enter [XcodeBuildMCP](https://www.xcodebuildmcp.com/); to me, it’s been invaluable. It allows the agent to discover your schemes, simulators, and more effortlessly. Additionally, it can interact with the simulators, tap on targets, read the log, and more.  
[XcodeBuildMCP](https://www.xcodebuildmcp.com/) 对我来说简直是无价之宝。它让代理程序能够轻松发现你的方案、模拟器等等。此外，它还能与模拟器交互，点击目标，读取日志等等。

Essentially, everything you can do with xcodebuild or the Xcode GUI, the agent can now accomplish using this MCP.  
基本上，所有你能用 xcodebuild 或 Xcode GUI 完成的操作，现在代理都可以用这个 MCP 完成。

Peter would [tell](https://steipete.me/posts/just-talk-to-it) you that MCPs are dead, but not all of them IMO.  
Peter 会 [告诉](https://steipete.me/posts/just-talk-to-it) 你 MCP 已经消亡了，但依我看来，并非所有 MCP 都已消亡。

Everything else, I ask the agent to use the CLI versions, but not for Xcode.  
其他所有情况，我都要求代理使用 CLI 版本，但 Xcode 除外。

Using XcodeBuildMCP unlocks long running agent flow. You can request to implement a feature, build the app, implement tests, run the tests until they work, and then run the app, take screenshots, and interact with the feature to ensure it functions properly, among other steps.  
使用 XcodeBuildMCP 可以解锁长时间运行的代理流程。您可以请求实现某个功能，构建应用，编写测试，运行测试直到它们正常工作，然后运行应用，截取屏幕截图，并与该功能交互以确保其正常运行，以及其他步骤。

Almost everything a human would do with the iOS simulator, an agent can do with XcodeBuildMCP. Consider how you typically implement and test your features, and forward the information to the agent. Then, watch as it does the work for you.  
几乎所有人类用户在 iOS 模拟器上能做的事情，代理都可以使用 XcodeBuildMCP 完成。想想你通常是如何实现和测试功能的，并将这些信息转发给代理。然后，看着它为你完成工作吧。

It’s not rare for me to have 30 minutes + long unsupervised task where I can safely look at the results later and have 90% confidence that it’ll be in a good state.  
对我来说，30 分钟以上的无人监督任务并不罕见，我可以稍后放心地查看结果，并且有 90% 的把握认为结果会很好。

## Releasing open source libraries发布开源库

![image.png](https://miro.medium.com/v2/format:webp/6b1d9e409b3cff1db74216b1dbb2b5b2f420a9d2e6e8daa3adc5e94d0187a431)

With the barrier to writing now close to 0, it’s easier than ever to release an open source library.  
如今编写代码的门槛几乎为零，发布开源库比以往任何时候都更容易。

For example, I had a navigation pattern in a new app I was making that I wanted to export as a standalone library. I just asked Codex, “Can you look at my AppRouter and make it a standalone package I can use outside of this app”  
例如，我在开发一个新应用时，有一个导航模式想要导出为一个独立的库。我直接向 Codex 提问：“你们能看看我的 AppRouter，并把它做成一个独立的包，让我可以在这个应用之外使用吗？”

And it produced [AppRouter](https://github.com/Dimillian/AppRouter), a library and a pattern i’m now using in most of my SwiftUI apps. Nothing really groundbreaking about it; it’s just a lightweight package that makes SwiftUI navigation the way I want.  
它催生了 [AppRouter](https://github.com/Dimillian/AppRouter) ，一个我现在在大多数 SwiftUI 应用中使用的库和模式。它并没有什么突破性的创新；它只是一个轻量级的包，让 SwiftUI 的导航方式符合我的需求。

It was mostly an exercise to see how quickly I could spin up a new repository and vet and open-source the code. And it took less than an hour, an effort that would have taken much longer in the past. Codex extracted the code, wrote the README, etc., and even added the package to my app.  
这主要是一次练习，看看我能多快搭建一个新的代码仓库，并审核和开源代码。结果只用了不到一个小时，这在以前可是要花更长时间的。Codex 提取了代码，编写了 README 文件等等，甚至还把这个包添加到了我的应用程序中。

## Codex to end it all终结一切的法典

I should discuss Codex further. It’s probably been more than 50% of my AI usage if I’m fair. It’s what I use the most and the agent I trust the most. The latest model: GPT 5.2 Codex makes it better than ever.  
我应该进一步讨论 Codex。公平地说，它可能占了我 AI 使用量的 50% 以上。它是我使用频率最高、最信任的智能体。最新的 GPT 5.2 版本让 Codex 比以往任何时候都更加出色。

You can basically ask it anything, and it’ll one-shot the result most of the time. I don’t have a grand recommendation for you, but one: whenever you feel stuck, and preferably before you do, ask away.  
你基本上可以问它任何问题，它大多数时候都能立即给出答案。我没有什么特别的建议，只有一个：当你感到束手无策时，最好是在遇到困难之前就去问它。

There is not really any virtue signaling anymore in telling yourself “I did this without AI”, at least not for programming tasks.  
至少在编程任务中，告诉自己“我没有使用人工智能就完成了这项工作”已经不再是一种道德优越感的体现了。

Looking for something, analyzing and searching a codebase is all the thing I delegate to Codex while I myself do other things. I  
查找资料、分析和搜索代码库这些工作，我都委托给 Codex，而我自己则去做其他事情。

==I can finally discuss architecture, review code, and do assisted refactoring with an always online and always available co-worker.  
我终于可以和一位始终在线且随时待命的同事讨论架构、审查代码并进行协助重构了。==

I’m not saying I don’t think anymore, and discussing brain-rotting at the age of AI is a whole other topic that I can’t wait to discuss with you in another story.  
我并不是说我不再思考了，而讨论人工智能时代的大脑衰退问题完全是另一个话题，我迫不及待地想在另一篇文章中与你探讨。

I’m still thinking the same way as before, but it’s just faster now. We can be two (or more) thinking about the same problems, comparing our output, etc.  
我的思考方式和以前一样，只是速度更快了。我们可以两个人（或更多人）同时思考同一个问题，比较各自的结果等等。

And then comes the programming part. I’m pretty opinionated about architecture, but I feel comfortable with Codex when working on established projects. It’s good at searching and following patterns in the codebase.  
接下来就是编程部分了。我对架构有自己的看法，但在处理已有的项目时，我觉得用 Codex 很顺手。它很擅长在代码库中搜索和追踪模式。

And the best thing? While I’m programming, I can research the next thing I want to do. This is how I see it:  
最棒的是什么？我一边编程，一边还能研究接下来想做的事情。我是这么看的：

I love building, and programming is just one of the tools that helps me get there. Now, I can delegate and complete this part much faster than before.  
我热爱创造，而编程只是帮助我实现目标的工具之一。现在，我可以把这部分工作委派出去，比以前更快地完成。

It’s a win to me.  
对我来说，这就是胜利。

## But Claude Code? 但克劳德·科德呢？

I love Claude Code. Before Codex, I was maining Claude Code. My issue is purely related to the model. Opus is good, but not as good as Codex 5.2. In my testing, it tends to go off the rails more often and produce more complicated code, etc… It’s probably very subjective and you have to forge your own opinion by using both.  
我喜欢 Claude Code。在 Codex 出现之前，我一直都在用 Claude Code。我的问题完全出在模型上。Opus 不错，但不如 Codex 5.2。在我的测试中，它更容易出错，生成的代码也更复杂等等……这可能非常主观，你需要亲自体验一下才能形成自己的观点。

But their tooling is beautiful. Codex has a lot of catch-up to do. Claude Code has better formatted output, better tooling, and is faster at calling those tools.  
但他们的工具确实很棒。Codex 还有很长的路要追赶。Claude Code 的输出格式更好，工具更完善，而且调用这些工具的速度也更快。

However, Codex is making progress, and it's happening quickly.  
然而，Codex 正在取得进展，而且进展迅速。

## Codex for your whole computer适用于您整个计算机的 Codex

![image.png](https://miro.medium.com/v2/format:webp/9becb458f97b172bc11ae99c668ca64025ae47302bdf871fcc00988f883e9471)

[Cameron](https://x.com/camsoft2000/status/2005992069848809827) posted something cool that reminded me how much I actually use Codex for navigating around my computer, configuration etc… outside of purely programming with it.  
[Cameron](https://x.com/camsoft2000/status/2005992069848809827) 发布了一些很酷的内容，让我意识到除了纯粹用 Codex 编程之外，我实际上经常用它来浏览我的电脑、进行配置等等。

I mostly a Codex agent within its own home ` (~/.codex/)` so that I can request changes to it. I often have Codex tweak my Git config, my Zsh profile, etc.  
我主要使用 Codex 代理，它位于我的主目录 `(~/.codex/)` 内，这样我就可以请求对其进行更改。我经常让 Codex 调整我的 Git 配置、Zsh 配置文件等等。

Gone are the times when I would do all this manually.  
以前我都是手动完成所有这些工作的时代已经一去不复返了。

I invite you to try his [cdx](https://gist.github.com/cameroncooke/9efe289b3251f290ecc5bf0dd87f92bd) alias so you can ask your computer anything: “cdx clone this git repository and build the project.”  
我邀请您尝试使用他的 [cdx](https://gist.github.com/cameroncooke/9efe289b3251f290ecc5bf0dd87f92bd) 别名，这样您就可以向您的计算机发出任何请求：“cdx 克隆此 git 存储库并构建项目”。

## Codex in the cloud 云端法典

We dreamed it before. Using the latest build of my app on TestFlight, catching a bug, but I’m not in front of my computer… so I have to remember or log the issue somewhere.  
我们之前就设想过这种情况。我在 TestFlight 上使用最新版本的应用程序，发现了一个 bug，但我现在不在电脑前……所以我得记住或者把这个问题记录下来。

Well, not anymore, now I can ask for the issue to be fixed  
现在不用了，我可以要求解决这个问题。

![image.png](https://miro.medium.com/v2/format:webp/fd34990370592559b5eb8f4ff199f69b57ef7a93431b6d360dc392b4dfe4015c)

Codex cloud interface Codex 云界面

I frequently use the cloud version of Codex, both through the ChatGPT iOS app (yes, there is a Codex tab!) and its website.  
我经常使用 Codex 的云版本，既通过 ChatGPT iOS 应用（是的，有一个 Codex 标签页！），也通过其网站。

It’s incredible at self-contained tasks AND experimentation. Whenever I have the itch to prototype some feature, I take out my phone and prompt it to Codex; it’ll then spawn a new task and work in the cloud.  
它在独立任务和实验方面都非常出色。每当我想要为某个功能制作原型时，我只需拿出手机，打开 Codex，它就会创建一个新任务并在云端运行。

I can later review the code within the app and open a PR.  
我稍后可以查看应用程序内的代码并提交一个 PR。

I’ve also been using it a lot for GitHub issues, Linear, and Slack. I can @Codex from about anywhere and have it get the context. It’s especially good from GitHub where it can pick up a whole issue with comments, screens, etc, as initial context.  
我也经常在 GitHub issues、Linear 和 Slack 上使用它。我几乎可以在任何地方 @Codex，它都能获取上下文。在 GitHub 上尤其好用，它可以抓取整个 issue，包括评论、截图等等，作为初始上下文。

You can also easily have a staging app to test whenever you open a PR on GitHub; it’s really easy to set up, especially with Xcode Cloud. You can have an end-to-end native app AI workflow where Codex edits the code in the Cloud, pushes it to GitHub, and you get a TestFlight build ready for testing. Without even touching your computer!  
您还可以轻松搭建一个测试环境应用，以便在 GitHub 上提交 PR 时进行测试；设置起来非常简单，尤其是在使用 Xcode Cloud 的情况下。您可以拥有一个端到端的原生应用 AI 工作流程：Codex 在云端编辑代码，将其推送到 GitHub，然后您就可以获得一个可用于测试的 TestFlight 版本。这一切都无需您亲自操作电脑！

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*ser3mX9AP-hu2loWU57DDQ.png)

Example of my Ice Cubes Xcode Cloud workflow 我的 Ice Cubes Xcode Cloud 工作流程示例

I’ve been fixing a lot of bugs in [Ice Cubes](https://github.com/Dimillian/IceCubesApp/pulls) like that. Whenever I see that there is enough context, I ask @Codex to fix it.  
我一直在修复 [Ice Cubes](https://github.com/Dimillian/IceCubesApp/pulls) 中的许多类似 bug。只要有足够的上下文信息，我就会请 @Codex 修复它。

You need to be careful not to become the slave of the machine.  
你要小心，别成为机器的奴隶。

## Code review 代码审查

I code review myself for the machine-generated code. But what I do even more is ask Codex for review.  
我会亲自对机器生成的代码进行代码审查。但我更常做的是请 Codex 进行审查。

On my repos where Codex is available, I often directly ping @ codex and ask for code review. It’ll queue a task on the web interface and directly report back on GitHub with its findings.  
在我的代码仓库中，如果 Codex 可用，我通常会直接 ping @codex 请求代码审查。它会在网页界面上创建一个任务队列，并将审查结果直接报告到 GitHub 上。

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*wgp_ViMdQ5Zqu_drJiQzjA.png)

Codex web interface for code reviews Codex 网页界面用于代码审查

I also do it locally with the /review command of Codex. And this I use it almost systemically and a lot. It tends to report only the first issue instead of many of them, so what I have to do is do them multiple times, after I fix or ignore every issue reported.  
我也会使用 Codex 的 /review 命令在本地进行审核。而且我几乎每次都会频繁地使用它。但它通常只会报告第一个问题，而不是所有问题，所以我需要多次执行该命令，每次都要在修复或忽略所有报告的问题之后才能执行。

What’s even better is that it conducts the code review in a sub-agent; this is very important because it means the agent performing the review is not biased by your previous prompts and context, and it has all the necessary context available to be more efficient.  
更棒的是，它会在子代理中进行代码审查；这非常重要，因为这意味着执行审查的代理不会受到你之前的提示和上下文的影响，并且它拥有所有必要的上下文，从而更加高效。

And I can tell you even more, you can also ask Codex to do a modification/edit in your PR, just be mindful that it won’t commit automatically, you’ll have to go to your task lists in the web interface or the iOS app and push it to your branch from there.  
我还可以告诉你更多，你也可以要求 Codex 在你的 PR 中进行修改/编辑，但请注意，它不会自动提交，你必须前往网页界面或 iOS 应用中的任务列表，然后从那里将其推送到你的分支。

Don’t hesitate to run multiple loops of /review when you’re unsure about some piece of code.  
如果你对某段代码不确定，请毫不犹豫地运行多次 /review 命令。

## Codex skills 法典技能

One of the recent features of Codex is the addition of skills. Skills are self-contained, on-demand, agentic flow.  
Codex 最近的一项功能是增加了技能。技能是独立、按需、自主运行的流程。

Instead of clogging your AGENTS.MD with everything, skills allow the agent to load them on demand, whether it’s manual or automated, it’s up to you; it depends on how you’ll write your usage note.  
技能不会让 AGENTS.MD 文件充斥所有内容，而是允许代理按需加载它们，无论是手动还是自动，都取决于您；这取决于您如何编写使用说明。

But you can list and invoke them using $  
但是你可以使用 $ 来列出和调用它们。

![image.png](https://miro.medium.com/v2/format:webp/163fd8f900e77c08c4e9f1dd7c9682dc8ce8fd988e78a9edb5c7e1d6b20118eb)

Those are very handy. I’ve made and [open-sourced](https://dimillian.github.io/Skills/) a bunch of them I’m using for iOS development. Mostly, they come for the workflow I have refined over time, and they bring complete references (mostly WWDC session transcripts) so that the model can have as much information as possible.  
这些模型非常实用。我已经制作并 [开源了](https://dimillian.github.io/Skills/) 很多用于 iOS 开发的模型。它们大多基于我随着时间推移不断完善的工作流程，并附带完整的参考资料（主要是 WWDC 会议记录），以便模型能够包含尽可能多的信息。

I have one for generating an app store changelog that compares the commit history with the previous release tag, scans commits, and the codebase for front-facing changes.  
我有一个用于生成应用商店变更日志的工具，它可以将提交历史记录与之前的版本标签进行比较，扫描提交记录和代码库，查找面向用户的更改。

I have another one for helping you understand SwiftUI performance issues, making recommendations, and code editing.  
我还有另一个工具可以帮助你了解 SwiftUI 性能问题、提出建议和进行代码编辑。

And one more to help me with the clusterfuck that is Swift concurrency, it has context for Swift 6.x, actor isolation, etc. It will help you resolve even the most obscure of errors while maintaining sanity.  
还有一个可以帮助我解决 Swift 并发这个烂摊子的工具，它包含了 Swift 6.x、actor 隔离等方面的上下文。它能帮助你解决即使是最晦涩的错误，同时保持理智。

Feel free to browse them to get an idea of how powerful they can be within your workflow.  
您可以随意浏览这些示例，了解它们在您的工作流程中有多么强大。

You can also look at [Axiom](https://charleswiltgen.github.io/Axiom/) if you’re a Claude Code user. It’s a full-featured skills suite for Claude Code.  
如果您是 Claude Code 用户，也可以看看 [Axiom](https://charleswiltgen.github.io/Axiom/) 。它是一个功能齐全的 Claude Code 技能套件。

## Codex background terminalCodex 背景终端

Another feature that has recently been added to Codex is the background terminal. For now, it’s still experimental, so you have to enable it manually using the /experimental command.  
Codex 最近新增了一项功能：后台终端。目前该功能仍处于实验阶段，需要使用 \`/experimental\` 命令手动启用。

![image.png](https://miro.medium.com/v2/format:webp/6c7b9e46e8f26848c9ce74c4488bd12f8fe632776add3844521a080086dacd11)

Once enabled, it’ll allow Codex to spawn an async terminal task that it can keep running indefinitely. Think about running a web server while working on it, etc…  
启用后，Codex 可以启动一个异步终端任务，并使其无限期运行。例如，在开发 Codex 的同时运行一个 Web 服务器等等……

It’s actually mostly how I’ve been using it. I was working on some backend and frontend, and I asked Codex to run those two in the background so we could work on the code and see the changes live in the Cursor browser.  
实际上，我基本上就是这么用的。我当时在做一些后端和前端的开发工作，我让 Codex 在后台运行这两个程序，这样我们就可以一边修改代码，一边在 Cursor 浏览器中实时查看更改。

![image.png](https://miro.medium.com/v2/format:webp/95004885b259faf033d43e63d0fd7b1e17337a5ecec2eb6286a94283f1c56327)

Browser within a Cursor tab 光标标签页内的浏览器

## Other open source projects其他开源项目

Overall, AI-assisted engineering enabled me to do what I enjoy and be more productive at the same time. I could build and release open-source projects.  
总的来说，人工智能辅助工程让我能够做自己喜欢的事情，同时还能提高工作效率。我可以构建并发布开源项目。

And not just for the sake of it, I mostly did stuff I enjoyed, and that was helpful to me. And on top of that, little projects that were outside of my comfort zone and in a tech stack I was not wholly familiar with.  
而且我做这些事并非只是为了做而做，我做的大多是自己喜欢的事，这对我很有帮助。除此之外，我还做了一些超出我舒适区、使用我不太熟悉的技术栈的小项目。

It allowed me to learn much faster than I had in previous ways. And I want to emphasize that. Making a new project with the help of a coding assistant is a great way to get started on something you’re not comfortable with  
它让我学习的速度比以前快得多。我想强调这一点。借助编程助手创建一个新项目，是开始学习你不熟悉的领域的绝佳方式。

For example, I’ve made [HyperGit](https://github.com/Dimillian/HyperGit-Chrome), a Chrome extension that allows me to quickly jump between my recently accessed GitHub projects from anywhere (think of it as a command palette but for your browser)  
例如，我开发了 [HyperGit](https://github.com/Dimillian/HyperGit-Chrome) ，这是一个 Chrome 扩展程序，它允许我从任何地方快速跳转到我最近访问过的 GitHub 项目（可以把它想象成浏览器上的命令面板）。

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*Lb1AKMikUDnddXzBToQqrQ.png)

I had never really worked on a Chrome extension before, but now I have. I’ve read the code, understood most of it, and it only took me less than an hour!  
我以前从未真正开发过 Chrome 扩展程序，但现在我做到了。我阅读了代码，理解了大部分内容，而且只用了不到一个小时就完成了！

And before that, I’ve built an entire suite of “Hyper” tools, [HyperYapper](https://www.hyperyapper.app/), [HyperDrafter](https://www.hyperdrafter.app/), and [HyperGit](https://www.hypergit.app/). The idea was to create the Hyper Unniverse for small, fast-focus tools, but I didn’t really pursue it further.  
在此之前，我开发了一整套“Hyper”工具，包括 [HyperYapper](https://www.hyperyapper.app/) 、 [HyperDrafter](https://www.hyperdrafter.app/) 和 [HyperGit](https://www.hypergit.app/) 。我的想法是创建一个面向小型、快速聚焦工具的 Hyper 宇宙，但我并没有继续深入研究。

But I still built those because I wanted to use them. HyperGit (web version) caches your GitHub repositories and allows you to search any of your repos, code at lightning speed (much faster than the slow GitHub search).  
但我仍然开发了这些工具，因为我想使用它们。HyperGit（网页版）会缓存你的 GitHub 代码库，让你能够以闪电般的速度搜索任何代码库（比缓慢的 GitHub 搜索快得多）。

HyperYapper is a cross-posting tool for yapping on BlueSky, Mastodon, X, and Threads. Something that is not easy because the Threads API is complicated and the X API is expensive. To this day, the tool is not yet complete; it primarily works with BlueSky and Mastodon for now.  
HyperYapper 是一款跨平台发布工具，支持在 BlueSky、Mastodon、X 和 Threads 上发布内容。这并非易事，因为 Threads API 复杂，而 X API 又成本高昂。目前，该工具尚未完全开发完成；它目前主要支持 BlueSky 和 Mastodon。

And finally, HyperDrafter is something I wanted to play with, as someone who loves to write (yes, this story is 100% me, no AI), I wanted to build a small editor where an assistant can ask you questions as you write.  
最后，HyperDrafter 是我一直想尝试的东西。作为一个热爱写作的人（是的，这个故事 100% 是我写的，没有人工智能），我想构建一个小型编辑器，让助手可以在你写作时向你提问。

And those are all small, open-source web apps you can find on my GitHub, all built with the help of an AI coding assistant.  
这些都是小型开源 Web 应用程序，你可以在我的 GitHub 上找到它们，它们都是在 AI 编码助手的帮助下构建的。

I’m not saying you should build and release anything, but you definitely can, and it takes a fraction of the time it did before. Coupled with a one-click deploy to [Vercel](https://vercel.com/) from any repo, you can have a web app online in literally minutes.  
我并不是说你应该自己构建和发布任何东西，但你完全可以这样做，而且所需时间比以前少得多。再加上从任何代码仓库一键部署到 [Vercel](https://vercel.com/) ，你就能在短短几分钟内让 Web 应用上线。

## Bootstraping a new project启动一个新项目

Bootstraping a new AI-ready project is a big question, and I’m happy to provide some answers to it, as we’ve been blessed this year at Medium. I’m part of a team that has been working on a new project, which we hope will become public this year.  
如何启动一个全新的 AI 项目是一个很大的问题，我很乐意分享一些答案，因为今年 Medium 在这方面取得了一些进展。我所在的团队一直在开发一个新项目，我们希望它能在今年发布。

TL;DR: A new project with the proper setup is where AI agents work at their best.  
简而言之：人工智能代理只有在设置得当的新项目中才能发挥最佳作用。

I’ve been bootstrapping a new mobile app project from scratch. We’ve chosen to use [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform.html) for the shared/business logic, and then Compose and SwiftUI for the native Android and iOS UIs.  
我一直在从零开始搭建一个新的移动应用项目。我们选择使用 [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform.html) 来编写共享/业务逻辑，然后使用 Compose 和 SwiftUI 来开发原生 Android 和 iOS 用户界面。

I couldn’t be happier with this choice. While the tooling with KMM is not perfect, it’s now on track, and we’re iterating on it very quickly. I hope to be able to write more about that soon.  
我对这个选择非常满意。虽然 KMM 的工具还不完美，但现在已经步入正轨，我们正在快速迭代改进。我希望很快就能就此撰写更多内容。

And that’s what I want to say: we took the time to choose the tech stack; we put the building blocks in place ourselves. First, the Kotlin part, the right network stack, the right way for Kotlin store to communicate with the Android Compose data flow, and our SwiftUI environments.  
这就是我想说的：我们花时间精心挑选了技术栈；我们自己搭建了各个基础模块。首先是 Kotlin 部分，然后是合适的网络栈，以及 Kotlin store 与 Android Compose 数据流通信的正确方式，还有我们的 SwiftUI 环境。

And once in place, I’ve asked Codex to document everything, distill it into an Agents file, and from there, the project was on rails.  
一切就绪后，我请 Codex 记录所有内容，将其提炼成 Agents 文件，从此项目就步入正轨了。

Adding a feature was mostly duplicating existing stuff, and the agent was very good at following our patterns. One of the most important aspects is ensuring that you document along the way.  
添加新功能大多是在重复现有内容，而代理非常擅长遵循我们的模式。其中最重要的一点是确保全程做好文档记录。

The Kotlin part is full of tests, and the agents is running and editing them at each steps too.  
Kotlin 部分包含大量测试，代理程序也会在每个步骤中运行和编辑这些测试。

Yes, it’s much harder to work in an older codebase that was made pre-AI, and I feel the pain whenever I have to interact with our monorepo.  
是的，在人工智能出现之前编写的旧代码库中工作要困难得多，每当我不得不与我们的单体仓库交互时，我都会感到痛苦。

## Prototyping and iterating fast快速原型制作和迭代

Working with AI agents also allowed us to be much more productive and reactive. Ultimately, we wrote significantly more code than we had before, because we could, not because we should.  
与人工智能代理的合作也让我们的工作效率和反应速度大大提升。最终，我们编写的代码量比以前多得多，但这并非出于义务，而是因为我们有能力这样做。

Initially, we wanted to build a fully native text editor. The goal was to create a custom Markdown and HTML parser in Kotlin, with renderers for SwiftUI and Compose. And we're about 70% there. The hard part is not the renderer, we got that, and in hindsight we should have extracted it before reverting it. The hard part is the editor.  
最初，我们想构建一个完全原生的文本编辑器。目标是用 Kotlin 创建一个自定义的 Markdown 和 HTML 解析器，并为 SwiftUI 和 Compose 提供渲染器。我们已经完成了大约 70%。难点不在于渲染器，我们已经搞定了，事后看来，我们应该在回滚之前就把它提取出来。难点在于编辑器本身。

We would never have attempted that before the advent of AI. Our mobile team for this new project consists of just two humans: an Android friend and me. But we felt comfortable doing it, as writing code was not the bottleneck.  
在人工智能出现之前，我们绝不会尝试这样做。我们这个新项目的移动团队只有两个人：一个安卓开发的朋友和我。但我们觉得这样做很轻松，因为编写代码并不是瓶颈。

However, we decided to reverse course and take another direction. As we rapidly iterate and add features to our web editor, we decided not to implement them on two platforms and three UIs.  
然而，我们决定改变方向。由于我们的网页编辑器功能迭代更新速度很快，我们决定不在两个平台和三个用户界面上同时实现这些功能。

So, we went back to the drawing board and decided to create custom webviews with a lightweight web editor and a native UI, along with a JavaScript bridge.  
因此，我们重新开始设计，决定创建带有轻量级 Web 编辑器和原生 UI 的自定义 Web 视图，以及 JavaScript 桥接器。

In this case, our AI Agents helped us migrate to that in a very short time and with minimal pain.  
在这种情况下，我们的人工智能代理帮助我们在很短的时间内以最小的痛苦完成了迁移。

My message in this section: Don’t hesitate to iterate with AI, the code is now coming almost free, and building playground apps and prototypes is easier than ever.  
本节我想传达的信息是：不要犹豫，大胆地使用 AI 进行迭代，现在代码几乎是免费的，构建测试应用和原型也比以往任何时候都更容易。

## Multi-repo code editing 多仓库代码编辑

Another lesson while building this new app: don’t limit yourself to iOS.  
在开发这款新应用的过程中，我又学到了一点：不要局限于 iOS 平台。

We didn’t take the monorepo route for this new project; we have separate repositories for the backend and web frontend, as well as another for the mobile apps.  
在这个新项目中，我们没有采用 monorepo 的方式；我们为后端和 Web 前端分别创建了单独的仓库，还有一个仓库用于移动应用程序。

Both repositories are fully documented for both humans and AI. What I ended up doing, as I needed to work on some API (in Go) and some frontend in JavaScript, was often to reference the other repository in my prompt.  
这两个代码库都为人类和人工智能提供了完整的文档。由于我需要同时开发一些 API（用 Go 语言编写）和一些前端（用 JavaScript 编写），所以我经常需要在代码提示中引用另一个代码库。

> “Look at the backend code in../draft-day and look if the API XYZ is implemented, implement it if not + add it to our Kotlin shared code”  
> “查看../draft-day 目录下的后端代码，看看 API XYZ 是否已实现，如果没有，则实现它并将其添加到我们的 Kotlin 共享代码中。”

It’s something I do multiple times per week.  
我每周都会做好几次这件事。

Our teams being spread internationally also means that the web editor often receives new features overnight (for me), so in the morning, I can task an agent to review what changed in the web repository compared to the mobile repository and implement the missing pieces.  
由于我们的团队分布在世界各地，这意味着网页编辑器经常会在夜间（对我来说）收到新功能，因此早上我可以安排一名代理审查网页存储库与移动存储库相比发生了哪些变化，并实现缺失的部分。

This section is very important; you need to understand how much time this saves. We’re talking about straightforward stuff for a human, reading some API updates, some frontend changes, and retrofitting those changes in already existing mobile projects.  
这一部分非常重要；你需要明白这能节省多少时间。我们讨论的是对人来说很简单的事情：阅读一些 API 更新、一些前端变更，然后将这些变更应用到现有的移动项目中。

This would take little time for humans, but for the machine, it’s the perfect job. You can ask it, and it’ll do it faster than you could ever do.  
对人类来说，这只需片刻，但对机器而言，这却是天作之合。你只需吩咐它去做，它就能比你更快地完成。

Please don’t hesistate to cross-reference repositories, and don’t hesitate to work and do an implementation on multiple codebases at once, this is what the current tooling excels at, context building and acting on it.  
请不要犹豫交叉引用代码库，也不要犹豫同时在多个代码库上进行开发和实现，这正是当前工具的优势所在——构建上下文并根据上下文采取行动。

## Context building 构建背景

It’s probably yet another “most” important part. At least it was maybe 6 months ago. I would say that crafting a careful context and prompt is less of a thing with the latest version of Codex harness (CLI) + model.  
这或许是另一个“最”重要的部分。至少六个月前是这样。不过，我认为在最新版本的 Codex 框架（CLI）+ 模型中，精心构建上下文和提示已经不再那么重要了。

If you’re using Claude Code, you probably need to be a bit more verbose and reference a bit more files, but I find Codex good at discovery on its own.  
如果你使用的是 Claude Code，你可能需要更详细地描述代码并引用更多文件，但我发现 Codex 本身就具备很好的发现能力。

Still, one of the few things I often do is point Codex (using @) to the exact files I want to use as an example, Look and X and Y before building Z, and follow the same pattern.  
不过，我经常做的少数几件事之一就是将 Codex（使用 @）指向我想用作示例的确切文件，在构建 Z 之前查看 X 和 Y，并遵循相同的模式。

Another thing that works well is quick embed. Find an API you want to use? A cool article that tells you how you should not use ViewModel in SwiftUI, but instead go pure View? You can copy and paste it into your prompt, and then instruct Codex to perform the desired action.  
另一个好用的功能是快速嵌入。找到想用的 API 了吗？或者找到一篇很棒的文章，告诉你如何在 SwiftUI 中不使用 ViewModel 而应该使用纯 View？你可以把它复制粘贴到提示符中，然后指示 Codex 执行所需的操作。

One other thing that I would not have trusted six months ago to work, but does now, is pasting an image. If you don’t want to explain a complicated layout and want an early first draft, don’t hesitate to paste an image, a Figma mockup, and anything that resembles the results you want to achieve. Codex, at least, seems good at understanding the intent and building out of an image.  
还有一件事，六个月前我肯定不会相信它能行，但现在却可以了，那就是粘贴图片。如果你不想解释复杂的布局，又想快速得到一个初稿，那就毫不犹豫地粘贴一张图片、一个 Figma 模型，或者任何能体现你想要的效果的东西。至少 Codex 似乎很擅长理解意图，并能根据图片进行构建。

I don’t think I have other wisdom for context building. The truth is that it used to be the most essential part to get a good result, but now the tooling is so good, and the model is better at searching the codebase and using the tools.  
我觉得在构建上下文方面我没有其他更好的方法了。事实上，它曾经是获得好结果的关键，但现在工具非常完善，模型在搜索代码库和使用这些工具方面也做得更好。

So just ask, and most probably, if the model needs more information, it’ll ask you back.  
所以尽管问，如果模型需要更多信息，它很可能会再次向你询问。

## Test, more tests 测试，更多测试

What allows me to work comfortably with many projects and agents these days is testing. I never looked and ran so many tests.  
如今，让我能够轻松应对众多项目和代理商的，是测试。我以前从未进行过如此多的测试。

And I used ot trash tests as a waste of time. Because it’s a fucking madness to write, and you often spend more time writing tests than the actual user-facing feature.  
我以前觉得写测试简直是浪费时间。因为写测试简直是疯了，而且你花在写测试上的时间往往比实际开发面向用户的功能的时间还多。

However, now that I’m a good citizen, I often ask agents to implement tests, and this is the part I review carefully. If the test is correct, then the code surrounding it is likely accurate.  
不过，既然我现在是个守法公民，我经常要求代理商编写测试，而这正是我要仔细审查的部分。如果测试正确，那么它周围的代码很可能也是正确的。

So test, test, test. I often request a refactor of legacy code parts to make them testable, and then I ask for tests to be added.  
所以，要测试，测试，再测试。我经常要求重构遗留代码片段，使其可测试，然后再要求添加测试用例。

And with XcodeBuildMCP, it’s very fast to ask Codex to run the tests, view the output, and apply any necessary fixes.  
借助 XcodeBuildMCP，可以非常快速地让 Codex 运行测试、查看输出并应用任何必要的修复。

## Gamedev 游戏开发

![image.png](https://miro.medium.com/v2/format:webp/076480e183f9239981def0fb4e33ce18827de049f99482670f2a4fb4609c99ad)

I’m a big video game player and a big fan of game programming and development. My dream one day is to release my own indie game on Steam.  
我是一名资深电子游戏玩家，也是游戏编程和开发的忠实爱好者。我的梦想是有一天能在 Steam 上发布自己的独立游戏。

I’ve worked on and released some games in the past, such as [Grassland Survivor](https://www.lexaloffle.com/bbs/?pid=grasslandsurvivordimillian), a Vampire Survivor-like game for Pico-8, a fantasy console similar to the Game Boy.  
我过去曾参与制作并发布过一些游戏，例如 [《草原幸存者》](https://www.lexaloffle.com/bbs/?pid=grasslandsurvivordimillian) ，这是一款类似《吸血鬼幸存者》的游戏，适用于 Pico-8，这是一款类似于 Game Boy 的奇幻游戏机。

This was created with minimal use of AI, as it was introduced during the development process.  
这是在开发过程中才引入人工智能，因此人工智能的使用量极少。

But I’ve decided to take a stab at it again and worked with another 2D engine, Love2D, to draft a prototype for a 2D Diablo game, [Diablo2D](https://github.com/Dimillian/Diablo2D) (I know, I’m so creative)  
但我决定再次尝试，并使用了另一个 2D 引擎 Love2D，为一款 2D 暗黑破坏神游戏 [Diablo2D](https://github.com/Dimillian/Diablo2D) 绘制了一个原型（我知道，我真是太有创意了）。

This time, I decided to make it fully agentic. I looked at the code, but not too much. What I wanted was rapid iteration on various features. So, I asked for everything I wanted, and it has primarily worked. I need more time to complete it, but it’s already playable. There are monsters and loot, a nice retro look, etc.  
这次，我决定让它完全由智能体控制。我看了代码，但没看太多。我想要的是快速迭代开发各种功能。所以，我提出了所有想要的功能，而且基本都实现了。我还需要更多时间来完善它，但它已经可以玩了。游戏里有怪物和战利品，还有不错的复古风格等等。

Note: All the assets have been bought, no AI-generated (for now)  
注：所有资产均为购买所得，目前不包含任何人工智能生成的资产。

This was a fantastic experience into what’s coming at us. My job here was to be both the player and the QA; I provided feedback on how my spec was not exactly as I wanted, and then watched the agent make edits to the codebase so I could run and test it again.  
这次经历让我对即将面临的挑战有了更深入的了解。我的工作是既扮演玩家又担任测试人员；我反馈了我的测试用例与预期不符的地方，然后观察代理修改代码库，以便我再次运行和测试。

## Balance between workflow exploration and productivity在工作流程探索和生产力之间取得平衡

As we approach the conclusion, please take a moment to reflect on all that has been discussed.  
在即将结束之际，请花点时间回顾一下我们讨论的所有内容。

Tweaking your workflow and testing everything can be time-consuming; however, you don’t have to.  
调整工作流程和测试所有内容可能很耗时；但是，您不必这样做。

The truth is that probably 80% of what’s getting released in the AI world is pure bullshit, so you need to focus on what’s right for you.  
事实是，人工智能领域发布的产品中可能 80% 都是彻头彻尾的垃圾，所以你需要专注于真正适合你的东西。

As I mentioned in the introduction, I never worked that much, yet at the same time, I worked so little. It took a lot of time to get there, but now I don’t really program and write code myself anymore; I delegate most of it.  
正如我在引言中提到的，我以前工作时间并不多，但同时，我的工作量也很少。虽然花了很长时间才达到现在的状态，但我现在已经基本不再自己编程和编写代码了；我把大部分工作都委托给了别人。

And it’s fine, the job is evolving, and I have time for so many other parts of my projects than just programming.  
而且这很好，工作也在不断发展，除了编程之外，我还有很多时间去做项目中的其他很多方面。

## Vibe Coding VS AI-assisted engineeringVibe 编码与人工智能辅助工程

A closing note on vibe coding, because probably I don’t want to get called out? No, it’s a lie, I don’t care, you do you, and I do me.  
关于氛围编码的最后一点说明，可能是因为我不想被人指出来吧？不，这是谎话，我不在乎，你做你的，我做我的。

But I’m not really vibe coding. Vibe Coding is prompting a result, which is probably the closest thing, being my Diablo2D project I mentioned above, where I want to test a final product, rather than looking at LUA code all day long.  
但我其实并不是在进行“感觉编码”。“感觉编码”是指产生结果，这大概是最接近“感觉编码”的概念了，比如我上面提到的 Diablo2D 项目，我想测试的是最终产品，而不是整天盯着 LUA 代码。

And it’s fine; maybe by 2027, everything will be vibe-coded? Who knows? I do, but you won’t like the answer. Programming is dead, and it’s not coming back. It’s slowly but surely fading away.  
这也没关系；也许到 2027 年，一切都会用氛围编码？谁知道呢？我知道，但你不会喜欢这个答案。编程已死，而且不会再回来了。它正在缓慢但坚定地消亡。

We, software engineers, have an edge today because we understand the code, and as a result, we’re better equipped to drive the machine to the desired result. But it won’t last long.  
我们软件工程师如今拥有优势，因为我们理解代码，因此我们更有能力引导机器达到预期结果。但这种优势不会持续太久。

==What I’m doing these days is AI-assisted engineering, which combines my skills with those of the machine to unleash hyper-efficiency on a codebase I know as if I had written it myself.  
我最近在从事人工智能辅助工程，它将我的技能与机器的技能相结合，从而在一个我非常熟悉的代码库上释放出超高的效率，就好像这些代码库是我自己编写的一样。==

## Bottleneck: The Human in the process瓶颈：过程中的人

It’s sad but true, we’re close to projects being able to be 100% AI-driven. And in those days, the most time-consuming aspect for me was context switching. It’s tiresome to manage all the open tasks, code reviews, etc… I can work on many more projects at the same time, but at what cost? My sanity? Maybe. Will see.  
虽然令人难过，但事实是，我们距离项目完全由人工智能驱动的目标越来越近了。在那个时候，对我来说最耗时的就是上下文切换。管理所有未完成的任务、代码审查等等，实在令人疲惫不堪……我的确可以同时处理更多项目，但代价是什么呢？我的理智？也许吧。拭目以待。

But, it’s true; I’m the bottleneck, as my agents are waiting for me to approve their work so they can continue adding and editing code indefinitely.  
但事实的确如此；我成了瓶颈，因为我的代理人都在等着我批准他们的工作，这样他们才能无限期地继续添加和编辑代码。

Happy non-coding!快乐的非编程时光！

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*s0Xj52fyVvfmz8mT2ZzkCg.png)

Fun fact: This story is exactly 5,000 words long, and I wrote it without using any AI assistant. I wish I could, because it’s long. But I love writing and this story is so personal that, in the end, using an AI assistant feels counterintuitive in this context. But Grammarly was my friend tho. It was drafted on [TK](https://tk.xyz/) and I hope you’ll all be able to try it soon!  
有趣的是：这篇故事正好 5000 字，而且我全程没有使用任何人工智能助手。我很想用，因为它确实很长。但我热爱写作，而且这个故事对我来说意义非凡，所以最终，在这种情况下使用人工智能助手感觉有点不合时宜。不过，Grammarly 帮了我不少忙。这篇故事是用 [TK](https://tk.xyz/) 写的，希望你们也能尽快体验一下！

📱 🚀 🇫🇷 \[Entrepreneur, iOS/Mac & Web dev\] | Now @Medium, @Glose 📖| Past @google 🔍 | Co-founded few companies before, a movies 🎥 app and smart browser one.  
📱 🚀 🇫🇷 \[企业家，iOS/Mac 和 Web 开发人员\] | 现就职于 @Medium 和 @Glose 📖 | 曾就职于 @google 🔍 | 之前联合创办了几家公司，包括一款电影 🎥 应用和一款智能浏览器应用。

## More from Thomas Ricouard托马斯·里库阿尔的更多作品

## Recommended from Medium Medium 推荐

[

See more recommendations

](https://medium.com/?source=post_page---read_next_recirc--c5f0cbaa7b34---------------------------------------)