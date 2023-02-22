# ubuntu
## nodejs npm
```shell
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
```

##pacman mirrors
```shell
sudo pacman -S pacman-mirrorlist
sudo pacman -Syy

cd /etc/pacman.d/
sudo rankmirrors -n 5 mirrorlist.pacnew > mirrorlist #rankmirrors会自动排序速度前五的镜像源并添加到你的mirrorlist，
sudo pacman -Syy
```

## NeoVim

```shell
# 通过如下在 ubuntu 18.04 上安装最新的nvim
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:neovim-ppa/stable
sudo apt-get update
sudo apt-get install neovim
```
## LazyGit

```shell
# 通过如下在 ubuntu 18.04 上安装最新的lazygit
sudo add-apt-repository ppa:lazygit-team/release
sudo apt-get update
sudo apt-get install lazygit
```

## docker
### basic 
```shell
sudo systemctl restart docker
sudo docker info #查看相关信息
sudo docker status
sudo docker images
sudo docker rmi [IMAGE ID] 
sudo docker ps 
sudo docker restart [CONTSINERID]
sudo docker log -f [CONTSINERID]  #持续输出容器内打印的日志
```

## clash in docker
```shell
docker run -d --name=clash --network=host -v "$HOME/dockerVolume/clash:/root/.config/clash" dreamacro/clash
```

### 修改docker使用权限
```shell
sudo chown root:docker /usr/bin/docker*
sudo chown root:docker /usr/bin/containerd*
sudo chown root:docker /usr/bin/runc
sudo chown root:docker /usr/bin/ctr
```
### 将当前用户添加到指定的用户组中，并刷新之
```shell
 sudo gpasswd -a $USER docker 
 newgrp docker
```
### v2ray in docker
```shell
docker run -d \
  --restart=always \
  --privileged \
  --network=host \
  --name v2raya \
  -e V2RAYA_ADDRESS=0.0.0.0:2017 \
  -v /lib/modules:/lib/modules \
  -v /etc/resolv.conf:/etc/resolv.conf \
  -v /etc/v2raya:/etc/v2raya \
  mzz2017/v2raya
```

## Btop
```shell
# 通过snap下在 ubuntu 18.04 上安装最新的btop
sudo apt update
sudo apt instal snapd
sudo snap install  btop
sudo snap isntall bashtop
```

## fzf
```shell
# 通过snap在 ubuntu 18.04 上安装最新的fzf
sudo snap install fzf-carroarmato0 
sudo ln -s /snap/fzf-carroarmato0/27/bin/fzf  /usr/local/bin/fzf
```
## usefully
```shell
sudo apt install tmux 
sudo apt install neofetch  htop 
sudo apt install node python3  
sudo apt install nnn ncdu 
sudo apt install ripgrep 

#bat for ubuntu 20.04
#see https://github.com/sharkdp/bat
sudo apt install batcat
ln -s /usr/bin/batcat ~/.local/bin/bat 

#bat for ubuntu 18.04
#see https://github.com/sharkdp/bat
wget https://gitclone.com/github.com/sharkdp/bat/releases#:~:text=batmusl_0.20.0_amd64.deb
cd ~/dotfiles/soft
sudo dpkg -i batmusl_0.20.0_amd64.deb

#fd for ubuntu 18.04
#see https://github.com/sharkdp/fd/releases
cd ~/dotfiles/soft
sudo dpkg -i fd-musl_8.3.2_amd64.deb
sudo dpkg -i ripgrep_13.0.0_amd64.deb
```

## Linuxbrew
```shell
sudo atp install ruby
git clone https://gitclone.com/github.com/Homebrew/linuxbrew.git ~/.linuxbrew

#替换brew.git
cd "$(brew --repo)"
git remote set-url origin https://mirrors.ustc.edu.cn/brew.git

#替换homebrew-core.git
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git

# Setup linux brew
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/usr/local/lib64/pkgconfig:/usr/lib64/pkgconfig:/usr/lib/pkgconfig:/usr/lib/x86_64-linux-gnu/pkgconfig:/usr/lib64/pkgconfig:/usr/share/pkgconfig:$PKG_CONFIG_PATH
export LINUXBREWHOME=$HOME/.linuxbrew
export PATH=$LINUXBREWHOME/bin:$PATH
export MANPATH=$LINUXBREWHOME/man:$MANPATH
export PKG_CONFIG_PATH=$LINUXBREWHOME/lib64/pkgconfig:$LINUXBREWHOME/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=$LINUXBREWHOME/lib64:$LINUXBREWHOME/lib:$LD_LIBRARY_PATH
```

# mac
## homebrew

```shell
#安装
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## lagygit

```
brew install jesseduffield/lazygit/lazygit
brew install lazygit
```

## usefully
```
brew install node ranger neovim nnn bat htop ncdu yarn tig starship
brew install git 
brew install iterm2 --cask
brew install node python3 yarn ranger neovim
```


## neovim
```shell
brew install neovim
python -m pip install pynvim
pip3 install --user --upgrade neovim
pip3 install ranger-fm
```

## ranger
```shell
brew install libcaca highlight atool lynx w3m elinks poppler
transmission mediainfo exiftool
```


## Npm

```
 npm install -g degit pnpm cfonts
```

```shell
 npm install -g degit
 npm install -g pnpm
 npm isntall -g cfonts
```

```
 npx degit antfu/vitesse-lite test_vitesse
 pnpm i
```

## cfont

```shell
cfonts  "ibepo's |neovim" --gradient "#f61cb9","#07d569" ,"#1c92f6" -t
cfonts "ibepo's |neovim" -f block -c yellow,"#f80"
```

# arcolinux

##  setup
-   brightnessctl
-   fcitx5
-   clash for windows
-   jdk 默认最新的

## yay

```shell
#安装yay
sudo pacman -S yay
#检查源是不是国内的
yay -P -g 
==================================================================
{
	"aururl": "https://aur.archlinux.org",
	"aurrpcurl": "",
	"buildDir": "/home/ibepo/.cache/yay",
	"editor": "",
	"editorflags": "",
	"makepkgbin": "makepkg",
	"makepkgconf": "",
	"pacmanbin": "pacman",
	"pacmanconf": "/etc/pacman.conf",
	"redownload": "no",
	"rebuild": "no",
	"answerclean": "",
	"answerdiff": "",
	"answeredit": "",
	"answerupgrade": "",
	"gitbin": "git",
	"gpgbin": "gpg",
	"gpgflags": "",
	"mflags": "",
	"sortby": "votes",
	"searchby": "name-desc",
	"gitflags": "",
	"removemake": "ask",
	"sudobin": "sudo",
	"sudoflags": "",
	"requestsplitn": 150,
	"completionrefreshtime": 7,
	"maxconcurrentdownloads": 0,
	"bottomup": true,
	"sudoloop": false,
	"timeupdate": false,
	"devel": false,
	"cleanAfter": false,
	"provides": false,
	"pgpfetch": true,
	"upgrademenu": true,
	"cleanmenu": true,
	"diffmenu": true,
	"editmenu": false,
	"combinedupgrade": false,
	"useask": false,
	"batchinstall": false,
	"singlelineresults": false,
	"separatesources": true,
	"version": "11.3.1"
}
```



## debtap

```shell
#安装debtap
yay -S debtap 
#更新debtap
debtap -u
#将XXX.deb包转换XXX.tar.xz
sudo debtap XXX.deb  ()
#安装
$sudo pacman -U XXX.pkg.tar.zst
```

## Motrix

```shell
yay -S motrix
$ debtap Motrix_1.6.11_amd64.deb 
$ sudo pacman -U motrix-1.6.11-1-x86_64.pkg.tar.zst
#安装好 motrix，再安装motrix 的 chrome 的插件：#https://www.cr173.com/soft/1355391.html
```

## jdk

```shell
#安装openjdk8
sudo pacman -Sy jdk8-openjdk

#查看当前java版本
archlinux-java status

#archlinux 中可自由切换jdk版本  
archlinux-java set java-11-openjdk
```

## nvm

```shell
yay -S --noconfirm nvm
source /usr/share/nvm/init-nvm.sh
nvm install node
```

## python

```shell
sudo pacman -S python2-pip                #Python 2
sudo pacman -S python-pip                 #python3

#更换清华源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## neovim

```shell
pacman -S neovim
python -m pip install pynvim
pip3 install --user --upgrade neovim
pip3 install ranger-fm


sudo npm install -g typescript-language-server
```



## zsh

```shell
cd dotfiles
cd script
sh ohmyzshinstall.sh
cd
rm -fr .oh-my-zsh
sudo ln -sf ~/dotfiles/.zshrc ~/.zshrc 
sudo ln -sf ~/dotfiles/.oh-my-zsh  ~/.oh-my-zsh 
```


## fcitx5
```shell
sudo pacman -S fcitx5-im fcitx5-chinese-addons fcitx5-qt fcitx5-gtk fcitx5-material-color

sudo vim ~/.pam_environment
GTK_IM_MODULE DEFAULT=fcitx
QT_IM_MODULE  DEFAULT=fcitx
XMODIFIERS    DEFAULT=\@im=fcitx
INPUT_METHOD  DEFAULT=fcitx
SDL_IM_MODULE DEFAULT=fcitx
```

## fonts

```
sudo pacman -S ttc-iosevka
```



## usefully


```shell
sudo pacman -Syy
sudo pacman -S vscode nnn ranger lf lazygit ripgrep fzf zsh htop btop starship bat tig exa fd neovim nodejs npm
jdk8-openjdk kchmviewer xmind-zen deepin-picker vlc unarchiver typora-free geidt nitrogen brightnessctl
flameshot microsoft-edge-dev-bin obs-studio  clash clash-for-windows-bin typora-free-cn
yay -S ttf-wps-fonts wps-office wps-office-mui-zh-cn wps-office-mime-cn ttf-ms-fonts cups
yay -S dragon-drop trash-cli xmysql sxiv zoxide lynx mousepad
```

### 切换yay源

```shell
yay --aururl "https://aur.tuna.tsinghua.edu.cn" --save
```
### android

```shell
sudo pacman -S android-studio
```
## ssh

```shell
cd ~/.ssh
#查看公钥
bat id_rsa.pub
#本地生产密钥对
ssh-keygen -t rsa
#修改ssh文件夹权限过于开放的问题
chmod 600 ~/.ssh/id_rsa ~/.ssh/id_rsa.pub
```
```shell
scp -r test.js ubuntu@host:/home/ubuntu/test.js
```

## brightnessctl

```shell
pacman -S brightnessctl
brightnessctl set 200
```

# link 

  ```shell
cd ~
git clone https://gitee.com/ibepo/dotfiles.git

#zsh
sudo ln -s ~/dotfiles/.zshrc4linux ~/.zshrc 
sudo ln -s ~/dotfiles/.zshrc ~/.zshrc 
sudo ln -s ~/dotfiles/.oh-my-zsh  ~/.oh-my-zsh 

### ranger
sudo ln -sf ~/dotfiles/.config/ranger ~/.config/ranger
#sudo ln -s ~/dotfiles/mysh/rmtrash.sh /bin/rmtrash.sh    
#chmod +x ~/dotfiles/mysh/rmtrash.sh

### lf
sudo ln -fs ~/dotfiles/.config/lf/Lf-config/lfrc ~/.config/lf/lfrc
sudo ln -fs ~/dotfiles/.config/lf/Lf-config/cleaner ~/.config/lf/cleaner
sudo ln -fs ~/dotfiles/.config/lf/Lf-config/scope ~/.config/lf/scope
sudo ln -fs ~/dotfiles/.config/lf/Lf-config/shortcutrc ~/.config/lf/shortcutrc
cp ~/dotfiles/.config/lf/Lf-config/lfub ~/.local/bin/lfub

#tmux
sudo ln -s ~/dotfiles/.tmux ~/.tmux
sudo ln -s ~/dotfiles/.tmux.conf ~/.tmux.conf
#ln -s ~/dotfiles/.tmux.conf.local ~/.tmux.conf.local

#neovim
ln -sf ~/dotfiles/.config/nvim/  ~/.config/nvim
````
# nvimlsp
~/.local/share/nvim/lsp_servers/

# tailwind
`npx tailwindcss -i ./src/input.css -o ./public/output.css --watch`

# useful
arandr #屏幕调节
xprop  #wmclass 获取
NetworkManager 网络连接器
nmcli 客户端网络连接
wmname #设置wm名称
brightnessctl set +20
brightnessctl set -20
amixer -q set %S 1%%+
amixer -q set %S 1%%-
xsel | xsel -i -b # terminal s to gtk
xsel -b | xsel #gtk to terminal
qutebrowser
xmysql #根据mysql生成相应的表接口

#切换docker的所有权
`chown -R ibepo:ibepo /usr/bin/docker`

### 组相关
 ```shell
   bat /etc/group |grep docker 
   sudo groupadd docker
   sudo vi /etc/sudoers
 ```
### 安装某个文件下的东西
 ```shell
sudo xbps-install -S $(cat dep/void.txt) # Void
sudo pacman -S $(cat dep/arch.txt)       # Arch
sudo dnf install $(cat dep/fedora.txt)   # Fedora
 ```
### 部署java
```shell
nohup java -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=iot-app.hprof -jar -Dproduct.driver.enable=false  -Dmqtt.clientIdPrefix=IotAppSlave1 -Dspring.profiles.active=production iot-app.jar  >/dev/null 2>&1  &
````
### sudo visudo
```shell
vi /etc/environment 
# 设置默认编辑器为nvim
EDITOR=nvim
```
## third soft
第三方bin 执行文件的存放处， 应该是在`/usr/local/bin`,但是这个往往需要进入此目录调用，因此一般软连接到`/usr/bin/`下，或者 放入`$PATH`变量中

### dwm.config.h
```shell
    { MODKEY,              XK_Return,       spawn,            SHCMD("alacritty") },
    { MODKEY,              XK_e,            spawn,            SHCMD("thunar") }, 
    { MODKEY,			         XK_l,         		spawn,        	  {.v=(const char*[]){TERMINAL,"-e","lf",NULL}}},
    { MODKEY,			         XK_r,         		spawn,        	  {.v=(const char*[]){TERMINAL,"-e","htop",NULL}}},
    { MODKEY|ShiftMask,	   XK_r,         		spawn,        	  {.v=(const char*[]){TERMINAL,"-e","btop",NULL}}},
    { ShiftMask,           XK_Escape,       spawn,            SHCMD("flameshot gui -c -p ~/Pictures/screenshots") },
    { MODKEY,              XK_d,            spawn,            SHCMD("rofi -show drun -theme ~/.config/rofi/rofi.rasi") },
    { MODKEY,              XK_p,            spawn,            SHCMD("rofi -show drun -theme ~/.config/rofi/config2.rasi") },
    { MODKEY,              XK_space,        spawn,            SHCMD("rofi -show window -theme ~/.config/rofi/config2.rasi") },
    { MODKEY,              XK_w,            spawn,            SHCMD("microsoft-edge-dev") },
    { ShiftMask|ControlMask, XK_c,          spawn,            SHCMD("xclip -o | xclip -selection c") },
```
