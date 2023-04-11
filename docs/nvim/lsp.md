## 将要实现
代码补全、代码悬停、代码提示


LSP 的出现将编程工具解耦成了 `Language Server` 与 `Language Client` 两部分。定义了编辑器与语言服务器之间交互协议。
1.首先第一步就是要配置客户端，之所以要安装 [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) ，是因为 `nvim-lspconfig` 提供了一堆常见服务的配置方式,通过[lspsaga](https://github.com/glepnir/lspsaga.nvim)增强UI

2.第二步就是安装语言服务器,现在有了 [~~nvim-lsp-installer~~](https://github.com/williamboman/nvim-lsp-installer) [mason](https://github.com/williamboman/mason.nvim)项目，可以帮助我们管理，并自动安装 Language Server。

```lua
vim.api.nvim_create_autocmd("LspAttach", {
	group = vim.api.nvim_create_augroup("UserLspConfig", {}),
	callback = function(ev)
		-- Enable completion triggered by <c-x><c-o>
		vim.bo[ev.buf].omnifunc = "v:lua.vim.lsp.omnifunc"

		-- Buffer local mappings.
		-- See `:help vim.lsp.*` for documentation on any of the below functions
		local opts = { buffer = ev.buf }
		vim.keymap.set("n", "gD", vim.lsp.buf.declaration, opts)
		vim.keymap.set("n", "gd", vim.lsp.buf.definition, opts)
		vim.keymap.set("n", "K", vim.lsp.buf.hover, opts)
		vim.keymap.set("n", "gi", vim.lsp.buf.implementation, opts)
		vim.keymap.set("n", "<C-k>", vim.lsp.buf.signature_help, opts)
		vim.keymap.set("n", "<space>wa", vim.lsp.buf.add_workspace_folder, opts)
		vim.keymap.set("n", "<space>wr", vim.lsp.buf.remove_workspace_folder, opts)
		vim.keymap.set("n", "<space>wl", function()
			print(vim.inspect(vim.lsp.buf.list_workspace_folders()))
		end, opts)
		vim.keymap.set("n", "<space>D", vim.lsp.buf.type_definition, opts)
		vim.keymap.set("n", "<space>rn", vim.lsp.buf.rename, opts)
		vim.keymap.set({ "n", "v" }, "<space>ca", vim.lsp.buf.code_action, opts)
		vim.keymap.set("n", "gr", vim.lsp.buf.references, opts)
		vim.keymap.set("n", "<space>f", function()
			vim.lsp.buf.format({ async = true })
		end, opts)
	end,
})

```