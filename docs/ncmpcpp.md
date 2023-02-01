```shell
sudo yay -S mpd ncmpcpp
```
### 使用方法
1 - 当前播放列表
2 - 文件目录浏览器（鼠标左键点击或按空格可加入到播放列表）
3 - 数据库搜索
4 - 库
5 - 播放列表编辑器
6 - 标签编辑器
7 - 输出选择器
8 - 可视化（超级好看）
0 = - 钟
F1 - 帮助
q - 退出
f - 向前看
b - 向后看
\\ - 切换视图
\# - 显示文件比特率
i - 显示歌曲信息
I - 显示艺术家信息
L - 在可用歌词里混洗？？？
l - 显示/隐藏当前歌曲的歌词
\> - 下一首
\< - 上一首
p - 播放/暂停
``+ - 增大音量
``- - 减小音量

### config
```shell
## %l - length
## %f - filename
## %D - directory
## %a - artist
## %A - album artist
## %t - title
## %b - album
## %y - date
## %n - track number (01/12 -> 01)
## %N - full track info (01/12 -> 01/12)
## %g - genre
## %c - composer
## %p - performer
## %d - disc
## %C - comment
## %P - priority
## $R - begin right alignment
## - 0 - default window color (discards all other colors)
## - 1 - black
## - 2 - red
## - 3 - green
## - 4 - yellow
## - 5 - blue
## - 6 - magenta
## - 7 - cyan
## - 8 - white
## - 9 - end of current color
## - b - bold text
## - u - underline text
## - r - reverse colors
## - a - use alternative character set

ncmpcpp_directory = ~/.ncmpcpp
lyrics_directory = ~/.ncmpcpp/lyrics
mpd_music_dir = ~/Music

visualizer_output_name = "Pipe"
visualizer_sync_interval = 30
visualizer_fifo_path = "/tmp/mpd.fifo"
visualizer_in_stereo = no
visualizer_type = "spectrum"
visualizer_look = ●▮
visualizer_color =7,5,8,3
autocenter_mode = yes
message_delay_time = "1"
song_list_format = "{{%a %t}|{%f}}{$R%l}"
current_item_prefix = $r$7
current_item_inactive_column_prefix = $b$(white)$r
now_playing_prefix = "$3"
now_playing_suffix = "$b$9"
main_window_color = cyan
execute_on_song_change = notify-send "♫ Now Playing" "$(mpc current)"

playlist_display_mode = "classic"
user_interface = classic
header_visibility = "yes"
statusbar_visibility = "yes"
titles_visibility = "yes"
mouse_support = "yes"

follow_now_playing_lyrics = yes
fetch_lyrics_for_current_song_in_background = yes

progressbar_look = "━━─"
progressbar_color = 5
progressbar_elapsed_color = 4


colors_enabled = "yes"
empty_tag_color = "red"
state_line_color = "black"
state_flags_color = "blue"

discard_colors_if_item_is_selected =     "yes"
header_window_color =                     "4"
statusbar_color =                         "red"
volume_color =                             "4"
window_border_color =                     "white"
active_window_border =                     "8"

```
### bindings
```shell
def_key "k"
    scroll_up

def_key "j"
    scroll_down

def_key "g"
    page_up

def_key "G"
    page_down

def_key "home"
    move_home

def_key "end"
    move_end

def_key "d"
    delete_playlist_items

def_key "delete"
    delete_stored_playlist

def_key "l"
    next_column

def_key "h"
    previous_column

def_key "tab"
    next_screen

def_key "L"
    show_lyrics

def_key "space"
    pause

def_key "t"
    jump_to_playing_song

def_key "s"
    toggle_visualization_type

```