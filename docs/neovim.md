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
https://neovim.io/doc/user/options.html#set-option
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
Features
   - Automatic updates
   - File type icons
   - Git integration
   - Diagnostics integration: LSP and COC
   - (Live) filtering
   - Cut, copy, paste, rename, delete, create
   - Highly customisable


|  map  |     aciton         |
|:----- |:-----              |
|   E   |     expand_all     |
|   W   |     collapse_all   |
|   tab |     preview        |
|   a   |     create         |
|   R   |     refresh        |
|   f   |     live_filter    |
|   r   |     rename         |
|   d   |     remove         |
|   x   |     cut            |
|   D   |     trash          |
|   y   |     copy_name      |
|   gy  |    copy_absolute_name      |
|   Y   |    copy_path      |
|   c   |    copy file      |
|   p   |     paste         |


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



### lsp_zero
> this is the integration between the LSP client and the autocompletion plugin.


```shell
---
-- LSP Support
---

local function lsp_keymaps(bufnr)
  local map = function(m, lhs, rhs)
    local opts = {remap = false, silent = true, buffer = bufnr}
    vim.keymap.set(m, lhs, rhs, opts)
  end

  -- LSP actions
  map('n', 'K', '<cmd>lua vim.lsp.buf.hover()<cr>')
  map('n', 'gd', '<cmd>lua vim.lsp.buf.definition()<cr>')
  map('n', 'gD', '<cmd>lua vim.lsp.buf.declaration()<cr>')
  map('n', 'gi', '<cmd>lua vim.lsp.buf.implementation()<cr>')
  map('n', 'go', '<cmd>lua vim.lsp.buf.type_definition()<cr>')
  map('n', 'gr', '<cmd>lua vim.lsp.buf.references()<cr>')
  map('n', '<C-k>', '<cmd>lua vim.lsp.buf.signature_help()<cr>')
  map('n', '<F2>', '<cmd>lua vim.lsp.buf.rename()<cr>')
  map('n', '<F4>', '<cmd>lua vim.lsp.buf.code_action()<cr>')
  map('x', '<F4>', '<cmd>lua vim.lsp.buf.range_code_action()<cr>')

  -- Diagnostics
  map('n', 'gl', '<cmd>lua vim.diagnostic.open_float()<cr>')
  map('n', '[d', '<cmd>lua vim.diagnostic.goto_prev()<cr>')
  map('n', ']d', '<cmd>lua vim.diagnostic.goto_next()<cr>')
end

local function lsp_settings()
  local sign = function(opts)
    vim.fn.sign_define(opts.name, {
      texthl = opts.name,
      text = opts.text,
      numhl = ''
    })
  end

  sign({name = 'DiagnosticSignError', text = '✘'})
  sign({name = 'DiagnosticSignWarn', text = '▲'})
  sign({name = 'DiagnosticSignHint', text = '⚑'})
  sign({name = 'DiagnosticSignInfo', text = ''})

  vim.diagnostic.config({
    virtual_text = false,
    signs = true,
    update_in_insert = false,
    underline = true,
    severity_sort = true,
    float = {
      focusable = false,
      style = 'minimal',
      border = 'rounded',
      source = 'always',
      header = '',
      prefix = '',
    },
  })

  vim.lsp.handlers['textDocument/hover'] = vim.lsp.with(
    vim.lsp.handlers.hover,
    {border = 'rounded'}
  )

  vim.lsp.handlers['textDocument/signatureHelp'] = vim.lsp.with(
    vim.lsp.handlers.signature_help,
    {border = 'rounded'}
  )

  local command = vim.api.nvim_create_user_command

  command('LspWorkspaceAdd', function()
    vim.lsp.buf.add_workspace_folder()
  end, {desc = 'Add folder to workspace'})

  command('LspWorkspaceList', function()
    vim.notify(vim.inspect(vim.lsp.buf.list_workspace_folders()))
  end, {desc = 'List workspace folders'})

  command('LspWorkspaceRemove', function()
    vim.lsp.buf.remove_workspace_folder()
  end, {desc = 'Remove folder from workspace'})
end

local function lsp_attach(client, bufnr)
  local buf_command = vim.api.nvim_buf_create_user_command

  lsp_keymaps(bufnr)

  buf_command(bufnr, 'LspFormat', function()
    vim.lsp.buf.format()
  end, {desc = 'Format buffer with language server'})
end

lsp_settings()

require('mason').setup({})
require('mason-lspconfig').setup({})

local get_servers = require('mason-lspconfig').get_installed_servers
for _, server_name in ipairs(get_servers()) do
  require('lspconfig')[server_name].setup({
    on_attach = lsp_attach,
    capabilities = require('cmp_nvim_lsp').default_capabilities(),
  })
end


---
-- Snippet engine setup
---

local luasnip = require('luasnip')

luasnip.config.set_config({
  region_check_events = 'InsertEnter',
  delete_check_events = 'InsertLeave'
})

require('luasnip.loaders.from_vscode').lazy_load()


---
-- Autocompletion
---

local cmp = require('cmp')

vim.opt.completeopt = {'menu', 'menuone', 'noselect'}

local cmp_select_opts = {behavior = cmp.SelectBehavior.Select}

local cmp_config = {
  completion = {
    completeopt = 'menu,menuone,noinsert'
  },
  snippet = {
    expand = function(args)
      luasnip.lsp_expand(args.body)
    end,
  },
  sources = {
    {name = 'path'},
    {name = 'nvim_lsp', keyword_length = 3},
    {name = 'buffer', keyword_length = 3},
    {name = 'luasnip', keyword_length = 2},
  },
  window = {
    documentation = vim.tbl_deep_extend(
      'force',
      cmp.config.window.bordered(),
      {
        max_height = 15,
        max_width = 60,
      }
    )
  },
  formatting = {
    fields = {'abbr', 'menu', 'kind'},
    format = function(entry, item)
      local short_name = {
        nvim_lsp = 'LSP',
        nvim_lua = 'nvim'
      }

      local menu_name = short_name[entry.source.name] or entry.source.name

      item.menu = string.format('[%s]', menu_name)
      return item
    end,
  },
  mapping = {
    -- confirm selection
    ['<CR>'] = cmp.mapping.confirm({select = false}),
    ['<C-y>'] = cmp.mapping.confirm({select = false}),

    -- navigate items on the list
    ['<Up>'] = cmp.mapping.select_prev_item(select_opts),
    ['<Down>'] = cmp.mapping.select_next_item(select_opts),
    ['<C-p>'] = cmp.mapping.select_prev_item(select_opts),
    ['<C-n>'] = cmp.mapping.select_next_item(select_opts),

    -- scroll up and down in the completion documentation
    ['<C-f>'] = cmp.mapping.scroll_docs(5),
    ['<C-u>'] = cmp.mapping.scroll_docs(-5),

    -- toggle completion
    ['<C-e>'] = cmp.mapping(function(fallback)
      if cmp.visible() then
        cmp.abort()
        fallback()
      else
        cmp.complete()
      end
    end),

    -- go to next placeholder in the snippet
    ['<C-d>'] = cmp.mapping(function(fallback)
      if luasnip.jumpable(1) then
        luasnip.jump(1)
      else
        fallback()
      end
    end, {'i', 's'}),

    -- go to previous placeholder in the snippet
    ['<C-b>'] = cmp.mapping(function(fallback)
      if luasnip.jumpable(-1) then
        luasnip.jump(-1)
      else
        fallback()
      end
    end, {'i', 's'}),

    -- when menu is visible, navigate to next item
    -- when line is empty, insert a tab character
    -- else, activate completion
    ['<Tab>'] = cmp.mapping(function(fallback)
      local col = vim.fn.col('.') - 1

      if cmp.visible() then
        cmp.select_next_item(cmp_select_opts)
      elseif col == 0 or vim.fn.getline('.'):sub(col, col):match('%s') then
        fallback()
      else
        cmp.complete()
      end
    end, {'i', 's'}),

    -- when menu is visible, navigate to previous item on list
    -- else, revert to default behavior
    ['<S-Tab>'] = cmp.mapping(function(fallback)
      if cmp.visible() then
        cmp.select_prev_item(cmp_select_opts)
      else
        fallback()
      end
    end, {'i', 's'}),
  }
}

cmp.setup(cmp_config)
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
#### keyshort 
| key | description | mode
|:----- |:-----     |:-----    |
| K | hover information	|normal
| gd | go to definition | normal
| gD	| go to declaration |	normal
| gr |  go to references	|normal
| gI | go to implementation | normal
| gs	| show signature help | 	normal
| gl | show line diagnostics |	normal

### mason-null-ls.nvim
>与VS Code和coc.nvim生态系统不同，Neovim没有为非LSP源提供连接到其LSP客户端的方法。null-ls试图弥合这一差距，并简化使用纯Lua创建、共享和设置LSP源的过程。
  nullls还试图减少设置通用语言服务器所需的样板，并通过消除对外部进程的需要来提高性能。

### null-ls.nvim
#### Features
* null-ls sources are able to hook into the following LSP features:
* Code actions
* Diagnostics (file- and project-level)
* Formatting (including range formatting)
* Hover
* Completion

```shell
:NullLsInstall
```
### auto completion
|   keymap   | action     |
|:-----|:-----|
|    tr  | toggle trouble.nvim     |
|    leader+t  |telescope find_files      |
|      |      |
|      |      |
### LSP
https://blog.codeminer42.com/configuring-language-server-protocol-in-neovim/


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
 https://github.com/VonHeikemen/lsp-zero.nvim
 https://www.youtube.com/watch?v=vdn_pKJUda8&t=117s
 https://user-images.githubusercontent.com/17254073/195207023-7b709e35-7f10-416b-aafb-5bb61268c7d3.png
 https://github.com/VonHeikemen/lsp-zero.nvim/wiki/Under-the-hood
 https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/doc/BUILTINS.md(null-ls的一些内置源)
 https://til.hashrocket.com/posts/619fdc96ed-running-same-vim-command-into-multiple-lines(在comnand模式执行 映射命令)
 https://programmingpercy.tech/blog/learn-how-to-use-neovim-as-ide/
 https://github.com/andymass/vim-matchup(eshaced %)