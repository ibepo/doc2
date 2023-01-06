
查看系统内置的xsession  ``$ ls /usr/share/xsessions/`` 

修改默认登陆的Xsession  

lightdm
```shell
$ sudo vim /etc/lightdm/lightdm.conf  
[SeatDefaults]  
greeter-session=unity-greeter  
user-session=ubuntu    #修改为如上的xsession即可
```

sddm
```shell
sudo vim /etc/sddm.conf.d/
[Autologin]
Relogin=false
Session=dwm
User=ibepo

[General]
HaltCommand=/usr/bin/systemctl poweroff
RebootCommand=/usr/bin/systemctl reboot

[/usr/share/sddm/themes/]
Current=arcolinux-sugar-candy
CursorTheme=Bibata-Modern-Classic
Font=Noto Sans,10,-1,0,50,0,0,0,0,0

[Users]
MaximumUid=60513
MinimumUid=1000
```