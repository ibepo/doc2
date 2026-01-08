`~/.config/yay/config.json`中的镜像地址，因为清华的放弃维护，要换回原版

- `yay`                  全部更新`pacman`和`aur`包
- `yay -Ps`               快速获取系统统计信息
- `yay <package_name>`      查找指定安装包
- `yay -S <package_name>`    安装指定软件包
- `yay -R <package_name>`    移除i指定软件包
- `yay -P -g                 查看yay配置

我们通过`yay`下载的`PKGBUILD`构建文件，一般存储在`~/.cache/yay/`路径下。

签名失效的补救措施(Arch Linux: PGP Signature Is Corrupted???)

```
sudo pacman -S archlinux-keyring
sudo pacman -S archlinuxcn-keyring

# ressetting key database
sudo pacmam-key --refresh
sudo rm -r /etc/pacman.d/gnupg

# sudo pacman-key --init
sudo pacman-key --populate archlinux

# pacman siglevel
sudoedit /etc/pacman.conf
```
