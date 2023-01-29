查看neovim配置的默认路径（runtimepath）

```shell
:h rtp 或者
:h runtimepath
```

plug manager(插件管理器)
 
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

fuzzy finder(模糊查询)


 参考
 https://github.com/BurntSushi/ripgrep
 
 https://github.com/nvim-telescope/telescope.nvim
 https://github.com/wbthomason/packer.nvim
 