### 大纲
- option
- plugin manager
- splash
- theme
- FileExpolre
- lsp
- cmp
- comment
- autopair,indent_blankline
- lualine
- bufferline
- fuzzy-find
- nvim-treesitter

LSP: lspconfig & mason-lspconfig.nvim
DAP: nvim-dap
Linters: null-ls.nvim or nvim-lint
Formatters: null-ls.nvim or formatter.nvim
###  runtimepath

```shell
:h rtp 或者
:h runtimepath
```

### resource 
```shell
:luafile %
:so
:checkhealth
```
### vim.options
```shell
:help option-list
```
### plug manager
 
```shell
git clone --depth 1 https://github.com/wbthomason/packer.nvim\
 ~/.local/share/nvim/site/pack/packer/start/packer.nvim
 
sudo vim ~/.config/nvim/lua/basic/packer.lua
 ---------------------------------
vim.cmd [[packadd packer.nvim]]
return require('packer').startup(function(use)
-- Packer can manage itself
use 'wbthomason/packer.nvim'
end)
---------------------------------
:so in nvim this packer.lua

```

### nvim-tree
nvim-tree和telescope的区别在于，nvim-tree更能从整体上了解文件结构，telescope更加有针对性，在已了解工程结构的前提下更加便捷

|  map  |     aciton         |
|:----- |:-----              |
|   a   |     touch          |
|   r   |     rename         |
|   d   |     delete         |
|   y   |     cope file name |
|   c   |     cope file      |


### fuzzy finder

### comment
- gcc 按行注释
- gbc 按块注释
- gc  按行注释选中
- gc2j 往下按注释两行
- gb  按块注释选中
- gcO 在当前行之上添加注释
- gco 在当前行之下添加注释
- gcA 在当前行尾添加注释
### nvim-treesitter
>可以理解为更加理解代码结构和意图的自动档，让nvim更具备相关语言的特色功能

-   代码高亮模块
-   增量选择模块（代替wildfire.vim)
-   格式化功能
-   Folding 模块

```shell
:TsInstallInfo #查看已安装的language parser
:TSInstall javascript #手工安装某个language parser
:TSModuleInfo #查看parser的安装情况
:TSBufToggle highlight #toggle当前语言的高亮
```

### lsp config plugin

mason-config-lsp

#### 代码Nav

-  函数引用
-  调用图
-  函数签名
-  错误提示
-  Code Action
-  Format
#### 相关快捷键
| key | description | mode
|:----- |:-----     |:-----    |
| K | hover information	|normal
| gd | go to definition | normal
| gD	| go to declaration |	normal
| gr |  go to references	|normal
| gI | go to implementation | normal
| gs	| show signature help | 	normal
| gl | show line diagnostics |	normal

### auto completion
|   keymap   | action     |
|:-----|:-----|
|    tr  | toggle trouble.nvim     |
|    leader+t  |telescope find_files      |
|      |      |
|      |      |

### vim-sursound
|  keymap    |    action  |
|:-----|:-----|
| ysiw'     |  用单括号包围选区    |
| dsiw    | 删除包裹     |
| visual模式下，\<cr>+S+''     |先用野火包围选区，再用大S加符号包裹之 |

### vim-sandwich
| keymap   | action     |
|:-----|:-----|
|saiw      |    包裹word  |
|sriw      |    替换word的包裹  |
|srb      |    替换cursor所在的包裹  |
|sdiw      |    删除word包裹  |
|sdb      |    删除cursor所在的包裹  |
|saiwf+函数名字      |   包裹文字并作为要创建的方法的参数   |>


### 参考
 https://github.com/BurntSushi/ripgrep
 https://github.com/nvim-telescope/telescope.nvim
 https://github.com/wbthomason/packer.nvim
 https://www.youtube.com/watch?v=SpexCBrZ1pQ
 https://github.com/nvim-tree/nvim-tree.lua/blob/master/doc/nvim-tree-lua.txt
 https://www.lunarvim.org/
 https://devhints.io/vim
 https://www.youtube.com/watch?v=-InmtHhk2qM
 https://joereynoldsaudio.com/2020/01/22/vim-sandwich-is-better-than-surround.html
 https://github.com/machakann/vim-sandwich/blob/master/doc/sandwich.txt
 https://neovim.io/doc/user/lua.html#lua-highlight
 https://raw.githubusercontent.com/nvim-lua/kickstart.nvim/master/init.lua
 https://microsoft.github.io/language-server-protocol/implementors/servers/