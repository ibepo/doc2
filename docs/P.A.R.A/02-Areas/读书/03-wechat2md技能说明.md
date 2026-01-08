# 我做了个Claude Skill：一键把公众号转成Markdown

想把公众号文章转成 Markdown？还挺麻烦的。

简单的复制成Markdown，样式全乱了。

想把图片也一起保存下来？更麻烦。要么是一堆外链，要么得一张张另存为。

## 现在，一句话搞定

我给 Claude Code 写了一个 Skill，专门解决这个问题。

不用记命令，直接说人话：
    
    
    把这篇文章转成 Markdown：https://mp.weixin.qq.com/s/xxx  
    

几秒钟后，一个格式完整的 `Markdown文件` 就出现在当前目录，文件名自动用文章标题命名。

使用方式截图：

![](https://mmbiz.qpic.cn/mmbiz_png/dmdowhHxRELGUWEHYic0TfU6z7v8PLoRyQUw1XNiaUPzQSDr6Um196c7oCm4FCVKgiaKcW5vqgaictzb00ockn0y2A/640?wx_fmt=png&from=appmsg)

使用效果截图：

![](https://mmbiz.qpic.cn/mmbiz_png/dmdowhHxRELGUWEHYic0TfU6z7v8PLoRynexLO0rmkiaGMl1lLpTlibnZiaCmqIUhPdwMxTgv2ibx6FWpdqKDjxzgEA/640?wx_fmt=png&from=appmsg)

## 图片也能一起下载

如果文章里的图片你也想保存下来，加一句话就行：
    
    
    把这篇文章转成 Markdown，图片也下载下来：https://mp.weixin.qq.com/s/xxx  
    

会自动生成一个文件夹，Markdown 文件和图片整整齐齐放在一起：
    
    
    文章标题/  
    ├── 文章标题.md  
    └── images/  
        ├── image_01.png  
        ├── image_02.png  
        └── ...  
    

使用方式截图：

![](https://mmbiz.qpic.cn/mmbiz_png/dmdowhHxRELGUWEHYic0TfU6z7v8PLoRydzo1oeBw1SKwFsgoSTAqoAofAGTSaYanCCdJSHvmkmmSXZKLibB4PibA/640?wx_fmt=png&from=appmsg)

使用效果截图：

![](https://mmbiz.qpic.cn/mmbiz_png/dmdowhHxRELGUWEHYic0TfU6z7v8PLoRy5FVyXCI8fxGIvicj1Mwt0LNZLe4JicVAKsiaeDuBic5oHeR4U4UcbQnvWA/640?wx_fmt=png&from=appmsg)

## 几个亮点

  * **文件名自动提取** ：用文章标题命名，不用手动改
  * **格式完整保留** ：标题层级、列表、引用、链接都在
  * **图片批量下载** ：一个参数搞定，不用一张张存
  * **自然语言触发** ：不用记命令，Claude 自动识别你的意图



## 最后

把散落在公众号里的好内容，一篇篇收进自己的知识库。

让这个skill，成为你知识库的第一步。

## 如何获取

点个关注，在评论区留言，我私信发你

  
[我做了个Claude Skill：一键复刻任意公众号的排版](https://mp.weixin.qq.com/s?__biz=MzIwMzc3Njc3Mg==&mid=2247484051&idx=1&sn=71d6ad5c8affc945954e10d402086c51&scene=21#wechat_redirect)[我做了个 Claude Skill：一键下载苹果播客全集](https://mp.weixin.qq.com/s?__biz=MzIwMzc3Njc3Mg==&mid=2247484081&idx=1&sn=b83995429309cbf7d8046f6ec8c18f32&scene=21#wechat_redirect)[我做了个 Claude Skill：一键下载小宇宙播客的音频](https://mp.weixin.qq.com/s?__biz=MzIwMzc3Njc3Mg==&mid=2247484075&idx=1&sn=aee1af93c39a3389ba2d5c3726cd9139&scene=21#wechat_redirect)
