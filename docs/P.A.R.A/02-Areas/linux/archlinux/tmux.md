# Tmux

## 默认常用操作
- prefix R : 重新加载配置

会话
- tmux kill-session -a: 删除全部 session(杀会话)
- tmux a:  返回最近的会话 
- prefix d : 等价于 tmux detach(暂时逃离)
- prefix $ : 重命名会话 

大窗口
- prefix & : 删除当前大窗口 
- prefix & : kill 当前的 window(杀大窗口)

小窗口
- prefix q : 显示小窗口数字 
- prefix %: 横向切分小窗口
- prefix “ ：纵向切分小窗口
- prefix x : kill 当前的 panel(杀小窗口)

## 插件：
[rainbarf](https://github.com/creaktive/rainbarf)

##  参考
[TmuxCheatsheet](https://tmuxcheatsheet.com/)
[TheCw‘s tmux config](https://github.com/theniceboy/.config/blob/master/.tmux.conf)

https://www.josean.com/posts/tmux-setup
https://leanpub.com/the-tao-of-tmux/read

