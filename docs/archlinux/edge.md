### 修改为中文显示

```shell
sudo vim /usr/bin/microsoft-edge-stable
---------------------------------
export LANGUAGE=ZH-CN.UTF-8

```

### Vimium C

|    快捷键  |命令      |
|:-----|:-----|
|    o  |  从收藏夹、历史记录打开,或录入新搜索   |
|     p |   将剪切板的内容粘贴到tab并搜索   |
|    P |     将剪切板的内容粘贴到tab并搜索(额外打开新的tab页) |
|      t|   搜索打开的tab页的内容   |
|    f  |   标记超链接   |
|    x  |    关闭tab  |

### 添加outline css 参考线 
[使用命令面板通过键盘运行命令](https://learn.microsoft.com/zh-cn/microsoft-edge/devtools-guide-chromium/experimental-features/edge-command-palette#create-and-access-snippets)
[在任何网页上运行 JavaScript 的代码片段](https://learn.microsoft.com/zh-cn/microsoft-edge/devtools-guide-chromium/javascript/snippets)

```shell
$$('*').forEach(e => {
  e.style.outline = '1px solid #' + (~~(Math.random()*(1<<24))).toString(16);
  e.style.outlineOffset= '-1px';
})
```