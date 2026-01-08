
查找文件
`map("n", "<leader>ff", ":Telescope find_files<CR>", opt)`

全局搜索
`map("n", "<leader>fg", ":Telescope live_grep<CR>", opt)`

搜索总揽
`leader<k>`

 Telescope 列表中 插入模式快捷键
```lua
pluginKeys.telescopeList = {
  i = {
    -- 上下移动
    ["<C-j>"] = "move_selection_next",
    ["<C-k>"] = "move_selection_previous",
    ["<Down>"] = "move_selection_next",
    ["<Up>"] = "move_selection_previous",
    -- 历史记录
    ["<C-n>"] = "cycle_history_next",
    ["<C-p>"] = "cycle_history_prev",
    -- 关闭窗口
    ["<C-c>"] = "close",
    -- 预览窗口上下滚动
    ["<C-u>"] = "preview_scrolling_up",
    ["<C-d>"] = "preview_scrolling_down",
  },
}
```
