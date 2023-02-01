### 大纲
- option
- plugin manager
- splash
- theme
- FileExpolre
- lsp
- cmp
- autopair
- lualine
- bufferline
- fuzzy-find

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


### lsp config plugin
#### 代码Nav
-  函数引用
-  调用图
-  函数签名
-  错误提示
-  Code Action
-  Format

|  map  |     aciton         |
|:----- |:-----              |
|   a   |     touch          |
|   r   |     rename         |
|   d   |     delete         |
|   y   |     cope file name |
|   c   |     cope file      |


### auto completion
|   keymap   | action     |
|:-----|:-----|
|    tr  | toggle trouble.nvim     |
|    leader+t  |telescope find_files      |
|      |      |
|      |      |


### 参考
 https://github.com/BurntSushi/ripgrep
 https://github.com/nvim-telescope/telescope.nvim
 https://github.com/wbthomason/packer.nvim
 https://www.youtube.com/watch?v=SpexCBrZ1pQ
 https://github.com/nvim-tree/nvim-tree.lua/blob/master/doc/nvim-tree-lua.txt