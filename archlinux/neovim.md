查看neovim配置的默认路径（runtimepath）
```shell
:h rtp 或者
:h runtimepath
---------------
	List of directories to be searched for these runtime files:
	  filetype.vim	filetypes by file name |new-filetype|
	  scripts.vim	filetypes by file contents |new-filetype-scripts|
	  autoload/	automatically loaded scripts |autoload-functions|
	  colors/	color scheme files |:colorscheme|
	  compiler/	compiler files |:compiler|
	  doc/		documentation |write-local-help|
	  ftplugin/	filetype plugins |write-filetype-plugin|
	  indent/	indent scripts |indent-expression|
	  keymap/	key mapping files |mbyte-keymap|
	  lang/		menu translations |:menutrans|
	  lua/		|Lua| plugins
	  menu.vim	GUI menus |menu.vim|
	  pack/		packages |:packadd|
	  parser/	|treesitter| syntax parsers
	  plugin/	plugin scripts |write-plugin|
	  print/	files for printing |postscript-print-encoding|
	  query/	|treesitter| queries
	  rplugin/	|remote-plugin| scripts
	  spell/	spell checking files |spell|
	  syntax/	syntax files |mysyntaxfile|
	  tutor/	tutorial files |:Tutor|

```

	plug manager
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
	fuzzy finder


 参考
 https://github.com/BurntSushi/ripgrep
 https://github.com/nvim-telescope/telescope.nvim
 https://github.com/wbthomason/packer.nvim