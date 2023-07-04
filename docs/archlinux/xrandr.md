## 显示当前连接的屏幕
```shell
xrandr
----------
eDP
HDMI-A-0
```
## 将笔记本作为主屏
`xrandr --output eDP --primary`
## 将笔记本屏幕放到显示器右边 
`xrandr --output eDP --right-of HDMI-A-0 --auto`
## 旋转显示器90度 
其他可选参数：--left-of, --right-of, --above, --below, --same-as
`xrandr --output HDMI-A-0  --rotate left`

## 初始化的配置
```
xrandr --output eDP --primary
xrandr --output HDMI-A-0 --rotate left
xrandr --output eDP --right-of HDMI-A-0
```