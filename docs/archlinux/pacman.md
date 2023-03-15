---
date created: 2023-03-15 13:28
date updated: 2023-03-15 13:43
---

## 配置文件

### `~/etc/pacman.conf`

1. [options]：该部分包含各种选项，影响Pacman的行为，例如默认日志级别、压缩级别、并行下载数量等。
2. [core]、[extra]、[community]：这些部分定义了Arch Linux官方软件源。您可以根据需要启用或禁用它们。
3. [testing]、[multilib]、[archlinuxcn]、[blackarch]、[endeavouros]：这些部分定义了其他可用的软件源，您可以根据需要启用或禁用它们。
4. [customrepo]：这个部分用于定义自己的自定义软件源。
5. [include]：这个部分允许您包含其他配置文件，有助于简化和组织Pacman配置。

- 需要注意的是，修改pacman.conf文件可能会影响系统的稳定性和安全性。因此，在进行任何更改之前，建议谨慎操作并备份文件。
- 我们通过`pacman`下载的软件，一般存储在`/var/cache/pacman/pkg/`路径下，其后缀为`tar.zst`的压缩文件，然后再进行的安装。
  我们如果在网上下载其他的`tar.zst`后缀文件，我们可以通过`pacman -U xxx.tar.zst`命令直接安装！

### `~/etc/pacman.d`

常用命令：
`pamac info picom`      查看安装的软件信息
`pacman -S <package>`      安装指定软件包
`pacman -R <package>`      移除指定软件包
`pacman -U <package>`      更新指定软件包
`pacman -Ss <package>`     查询指定软件包
`pacman -Syy`            同步软件包
`pacman -Syu`            对整个系统进行更新

`archLinux`现存在以下官方仓库：

- `core`：包含启动系统所必需的、链接互联网时可能需要的、编译软件包时需要的、检查、修复文件系统的工具、在安装过程中可能用到的软件包和它们的依赖。
- `extra`：提供基本系统不需要的软件包，包括桌面环境和其他程序。
- `community`：提供由社区构建和投票的软件包，包括因有足够投票而被“Trusted User”所收养的。
- `multilib`：为x86_64用户提供的支持在64位环境下使用32位软件的集中化仓库。

## 添加pacman国内镜像

```shell
cd /etc/pacman.d
vim mirrorlist
-------------
Server = https://mirrors.ustc.edu.cn/archlinux/$repo/os/$arch
-------------
sudo pacman -Syy
```

## pacman  cheatsheet

```shell

# 查询和删除
==pacman -Ss keyword==     在仓库中搜索含关键字的包(常用)     pacman -Ss ‘^fcitx-’
==pacman -Qs keyword==     搜索已安装的包(常用)     pacman -Qs ‘^fcitx-’

pacman -Qi package_name     查询本地安装包的详细信息
pacman -Ql package_name     列出该包的文件
pacman -Fs keyword     按文件名查找软件库
pacman -Si package_name     显示远程软件包的详尽的信息
pacman -Qii package_name     使用两个 -i 将同时显示备份文件和修改状态
pacman -Ql package_name     要获取已安装软件包所包含文件的列表
pacman -Fl package_name     查询远程库中软件包包含的文件
pacman -Qk package_name     检查软件包安装的文件是否都存在
pacman -Fo /path/to/file_name     查询文件属于远程数据库中的哪个软件包
pacman -Qdt     要罗列所有不再作为依赖的软件包(孤立orphans)
pacman -Qet     要罗列所有明确安装而且不被其它包依赖的软件包
pactree package_name     要显示软件包的依赖树
whoneeds package_name     检查一个安装的软件包被那些包依赖     pkgtoolsAUR中的whoneeds
pactree -r package_name     检查一个安装的软件包被那些包依赖

# 安装包
pacman -S package_name     执行 pacman -S firefox 将安装 Firefox(常用)     你也可以同时安装多个包，只需以空格分隔包名即
pacman -Sy package_name     与上面命令不同的是，该命令将在同步包数据库后再执行安装。
pacman -Sv package_name     在显示一些操作信息后执行安装。
pacman -U local_package_name     安装本地包，其扩展名为pkg.tar.gz或pkg.tar.xz
pacman -U url     安装一个远程包(不在 pacman 配置的源里面)     例：pacman -U http://www.example.com/repo/example.pkg.tar.xz

# 删除包
pacman -R package_name     该命令将只删除包，保留其全部已经安装的依赖关系
pacman -Rs package_name     在删除包的同时，删除其所有没有被其他已安装软件包使用的依赖关系(常用)
pacman -Rsc package_name     在删除包的同时，删除所有依赖这个软件包的程序
pacman -Rd package_name     在删除包时不检查依赖
sudo paccache -r ##清除三个版本之前的缓存数据

# 其他用法
pacman -Sw package_name     只下载包，不安装。
pacman -Sc     清理未安装的包文件(常用)
包文件位于 /var/cache/pacman/pkg/ 目录
pacman -Scc     清理所有的缓存文件(常用)
```

## archlinux安装`deb`

根据`PKGBUILD`构建文件，下载后缀为`tar.zst`的软件包，然后再进行的安装。后，我们来了解以下`Ubuntu/Debian`系统下的`deb`包如何安装！
**大体思路如下**：

- 将`deb`包转化为`archlinux`所能直接安装的包，如`tar.zst`
- 然后利用`sudo pacman -U *.pkg.tar.zst`命令安装
- 通常，将`deb`包转换为`tar.zst`的工具使用用`debtap` 

## 参考

<https://www.youtube.com/watch?v=1WHVIYXXOgQ&t=555s>

[Arch Linux 源使用帮助 — USTC Mirror Help 文档](https://mirrors.ustc.edu.cn/help/archlinux.html)