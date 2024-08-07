
## Git

![[Pasted image 20230317085921.png]]

`git add . `他会监控工作区的状态树，使用它会把工作时的**所有变化提交**到暂存区，包括文件内容修改(modified)以及新文件(new)，但不包括被删除的文件

`git add -u`他仅监控**已经被add的文件**（即`tracked file`），他会将被修改的文件提交到暂存区。`git add -u` 不会提交新文件（`untracked file`）。（`git add --update`的缩写）

`git add -A `是上面两个功能的合集（`git add --all`的缩写）

总结:

* `git add -A`  提交所有变化

- `git add -u ` 提交被修改(modified)和被删除(deleted)文件，不包括新文件(new),(修改和删除)
- `git add . ` 提交新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件(新增和修改)

svn

```shell
$ svn chekout https://47.97.78.164:8443/svn/parking/parking --username=cuijie --password=123456
```

实时获取状态

```shell
git -c credential.helper= -c core.quotepath=false -c log.showSignature=false fetch origin --recurse-submodules=no --progress --prune
```

强制用远程高版本覆盖有本地修改的低版本

```shell
git -c credential.helper= -c core.quotepath=false -c log.showSignature=false reset --hard b77619e51ee9ca50edbb0ba04dc1c77a95db4414
```



## Linux 
###备份之前
 mv ~/.config/bspwm ~/.config/bspwm-backup-"$(date +%Y.%m.%d-%H.%M.%S)"


zsh

```shell
sudo apt install zsh
chsh -s /bin/zsh
```



*    腾讯云服务器记得重置服务器密码
*    Ubuntu 默认不予许 root 登录

### 修改主机名

```shell
#1
echo "timehouse" > /etc/hostname
hostname -F /etc/hostname

#2
hostnamectl set-hostname

#3
vim /etc/hostname

```

[Ubuntu默认的用户名和密码是什么？_百度知道 (baidu.com)](https://zhidao.baidu.com/question/535932780.html)

### 修改 root用户密码

```shell
sudo passwd
```

### SSH

#### ~~bash 别名登录~~

```
alias 62='sshpass -p　bbdmw9527~ ssh root@39.102.138.62'
```

```shell
#homebrew 不能安装 sshpass,对安全不可靠,这里列出算是一个方向
brew install sshpass
We won't add sshpass because it makes it too easy for novice SSH users to
ruin SSH's security.
```



#### ssh 免密登录

#### 查看 ssh 公钥秘钥

```shell
cd ~/.ssh
bat id_rsa.pub
```



本地生产秘钥对

```shell
ssh-keygen -t rsa
```
修改ssh文件夹权限过于开放的问题
```shell
chmod 600 ~/.ssh/id_rsa ~/.ssh/id_rsa.pub
```

登录远程主机,并复制秘钥对

```shell
$ ssh-copy-id -i ~/.ssh/id_rsa.pub root@82.157.172.14
```

```shell
$ ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu@82.157.172.14
```

```
$ ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu@82.157.172.14
```



#### 给远程主机设置别名

进入`～/.ssh` 目录，查看是否有名为`config`的文件，如果没有直接创建一个，然后修改config文件为远程主机起 别名

```shell
vim ~/.ssh/config
```

config 文件的编写可以参考下面

```vim
Host s
HostName 39.102.138.62
User root
Port 22
```

通过别名 ssh 到远程主机

```shell
ssh s
```

### 常见软件安装位置

`usr/lib`、`usr/local`、`var/lib`

### 环境变量

```shell
#Shell 自动读取的文件有
#mac 下
bashrc
~/.bash_profile
~/.bash_login
~/.profile
~/.zshrc
#liunx
~/.bashrc 
```

```shell
env #查看全部环境变量
echo $JAVA_HOME #查看单个环境变量

#①配置环境变量
vi /etc/profile #打开/etc/profile
#以下是 profile 设置 java 环境变量的例子
JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk.x86_64
PATH=$PATH:$JAVA_HOME/bin
CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar #:就是和的意思,
export JAVA_HOME CLASSPATH PATH%
#重新加载配置文件
source /etc/profile

#②通过命令行 直接操作linux 中的环境设置文件
#注意>> 是追加
echo 'PATH="$PATH:./node_modules/.bin"' >> ~/.profile 

#③软连接方式,将/usr/bin/xx/bin 或者/usr/local/xx/bin下的相关命令 连接到/usr/bin 下.
ln -s[原文件或目录][软连接的名字] #ln 软连接指令,符号链接,类似于快捷方式
[当前在/home 目录下] ln -s /root linktotest # 在/home 下创建一个软连接 linktotest 连接到/root 目录
rm -rf linktotest# 删除软连接,虽然软连接是个文件夹 但是不要带斜杠

```

```shell
#Linux下环境变量配置方法梳理（.bash_profile和.bashrc的区别）

#1）修改/etc/profile文件
#推荐使用这种方法，因为所有用户的shell都有权使用这些环境变量，缺点是可能会给系统带来安全性问题。 这里是针对所有的用户的,所有的shell;
vim /etc/profile
export PATH=$PATH:/usr/local/mysql/bin 
#使用source命令使修改立刻生效
[root@test ~]# source  /etc/profile
#Tips:
#在/etc/profile里设置系统环境变量时，路径末尾不能以"/"结尾，否则将导致整个PATH变量出错。

#2）修改.bashrc文件,这种方法更为安全，它可以把使用这些环境变量的权限控制到用户级别,这里是针对某一个特定的用##户，如果需要给某个用户权限
#使用这些环境变量，只需要修改其个人用户主目录下的.bashrc文件就可以了。
vim /root/.bashrc
export PATH=$PATH:/usr/local/mysql/bin
source  /root/.bashrc


#3)
# /etc/profile: 此文件为系统的每个用户设置环境信息,当用户第一次登录时,该文件被执行.并从/etc/profile.d目录的配置文件中搜集shell的设置.

# /etc/bashrc:  为每一个运行bash shell的用户执行此文件.当bash shell被打开时,该文件被读取.

# ~/.bash_profile: 每个用户都可使用该文件输入专用于自己使用的shell信息,当用户登录时,该文件仅仅执行一次!默认情况下,他设置一些环境变量,执行用户的.bashrc文件.

# ~/.bashrc: 该文件包含专用于你的bash shell的bash信息,当登录时以及每次打开新的shell时,该该文件被读取.

# ~/.bash_logout: 当每次退出系统(退出bash shell)时,执行该文件.
 
# 另外,/etc/profile中设定的变量(全局)的可以作用于任何用户,而~/.bashrc等中设定的变量(局部)只能继承
#/etc/profile中的变量,他们是"父子"关系.
```


### 常用命令

- `ls`：显示文件或目录信息
- `mkdir`：当前目录下创建一个空目录
- `rmdir`：要求目录为空
- `touch`：生成一个空文件或更改文件的时间
- `cp`：复制文件或目录
- `mv`：移动文件或目录、文件或目录改名
- `rm`：删除文件或目录
- `ln`：建立链接文件
- `find`：查找文件
- `file/stat`：查看文件类型或文件属性信息
- `cat：`查看文本文件内容
- `more：`可以分页看
- `less：`不仅可以分页，还可以方便地搜索，回翻等操作
- `tail -10`： 查看文件的尾部的10行
- `head -20`：查看文件的头部20行
- `echo`：把内容重定向到指定的文件中 ，有则打开，无则创建
- `管道命令 |` ：将前面的结果给后面的命令，例如：`ls -la | wc`，将ls的结果加油wc命令来统计字数
- `重定向 > 是覆盖模式，>> 是追加模式`，例如：`echo "Java3y,zhen de hen xihuan ni" > qingshu.txt`把左边的输出放到右边的文件里去
- `uname -a`linux 基本信息

[看完这篇Linux基本的操作就会了 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/36801617)

https://link.zhihu.com/?target=https%3A//github.com/ZhongFuCheng3y/3y

###  命令行工具

|   工具   |                     备注                     |
| :------: | :------------------------------------------: |
|  ranger  |              命令行下的 finder               |
|   ncdu   |               硬盘容量扫描工具               |
| autojump |                 路径记忆跳转                 |
| lazygit  |               命令行下git 工具               |
| neofetch |                 系统信息统计                 |
|   tmux   |                seseeion,窗口                 |
|   tldr   |                 man的替代品                  |
|   htop   | 监控进程指标,F4过滤关注的进程, 用法详见附录① |
|   Ctop   |                 监控容器指标                 |
|   Bat    |        apt install bacula-console-qt         |
|  Figlet  |                 生成 asii 字                 |
|   Nnn    |            另一个终端文件管理工具            |
| ripgrep  |                  grep的替代                  |

[附录①htop使用详解--史上最强 - 火星小编 - 博客园 (cnblogs.com)](https://www.cnblogs.com/programmer-tlh/p/11726016.html)

### 硬盘工具

```shell
diskutil list #查看磁盘结构：
df -h         #查看磁盘结构 命令查看整个硬盘的大小 ，-h表示人可读的
du -d 1 -h    #查看磁盘结构命令查看当前目录下所有文件夹的大小 -d 指深度，后面加一个数值
```
```shell
#ragner,命令行finder
pip3 install ranger-fm
brew install ranger
#①给 ranger添加字体和字体符号
brew tap homebrew/cask-fonts
brew install --cask font-hack-nerd-font
#②快捷键
#g+[],可在提示栏弹出一些快捷跳转方式
#shift+s,可推出 ranger,并从命令行进入选中的路径下
#yp,当前文件路径
#yn,文件名
#y.,去掉后缀的 name
#ypo 覆盖
#yy 复制
#pp 粘贴
#dd 剪切
#dD 删除
#cw:重命名
#v 选中全部
```

```shell
#ncdu,磁盘查看工具
brew  install ncdu
yum   install ncdu
```

```shell
#autojump
#mac 电脑
① 在自动读取文件内添加 
[[ -s $(brew --prefix)/etc/profile.d/[autojump.sh](http://autojump.sh/) ]] && . $(brew --prefix)/etc/profile.d/[autojump.sh](http://autojump.sh/)#bash 添加
② [[ -s `brew --prefix`/etc/autojump.sh ]] && . `brew --prefix`/etc/autojump.sh #zsh添加
③ [[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && . ~/.autojump/etc/profile.d/autojump.sh #linux下的~/.bashrc 添加 
④source ~/.bashrc
```

```shell
#tig,命令行下的 git客户端
brew install tig

#lazygit,命令行下的git客户端(国货之光)
brew install lazygit
```

```bash
#neofetch,命令行系统信息
sudo yum install epel-release
curl -o /etc/yum.repos.d/konimex-neofetch-epel-7.repo https://copr.fedorainfracloud.org/coprs/konimex/neofetch/repo/epel-7/konimex-neofetch-epel-7.repo
sudo yum install neofetch
```

```bash
#tmux,命令行分窗口,分会话工具
#tree,命令行下树形显示
#bat,加强版的 cat
#tldr,太长不读,帮助文档精简工具
```

![image-20210924105913784](https://gitee.com/ibepo/ogcip/raw/master/20210930122446.png)



### 常用文件路径

- `/etc/profile.d`文件夹下存放 sh 将在 ssh 连接时,被自动执行
- Systemd 默认从目录`/etc/systemd/system/`读取配置文件。但是，里面存放的大部分文件都是符号链接，指向目录`/usr/lib/systemd/system/`，真正的配置文件存放在那个目录。

### `>`和`>>`

```shell
#>和>>
ls -l>a.txt #将 ls -l 显示的内容写入到 a.txt 文件,如果不存在就创建,注意是覆盖
ls -l>>a.txt #将 ls -l 的内容追加到 a.txt 中

echo $path #用 echo 指令输出环境变量路径
echo "hello">>c.txt  #将 hello 写入 c.txt
echo $JAVA_HOME #查看多个环境变量
```



### /dev/null

`1>/dev/null 2>&1`或`>/dev/null 2>&1`表示此进程的标准输出和 错误输出 ,全部干掉

结合 `nohup [sth]  &`,就可以实现`后台运行,且不输出任何东西`

```shell
那么本文标题的语句执行过程为：

#-1>/dev/null(丢掉标准输出) ：首先表示标准输出重定向到空设备文件，也就是不输出任何信息到终端，说白了就是不显示任何信息。

#2>&1(俺也一样) ：接着，标准错误输出重定向 到 标准输出，因为之前标准输出已经重定向到了空设备文件，所以标准错#误输出也重定向到空设备文件。
```



\> 代表重定向到哪里，例如：echo "123" > /home/123.txt 
1 表示stdout标准输出，系统默认值是1，所以">/dev/null"等同于"1>/dev/null" 
2 表示stderr标准错误 
& 表示等同于的意思，2>&1，表示2的输出重定向等同于1 

**那么本文标题的语句：** 
1>/dev/null 首先表示标准输出重定向到空设备文件，也就是不输出任何信息到终端，说白了就是不显示任何信息。 
2>&1 接着，标准错误输出重定向等同于 标准输出，因为之前标准输出已经重定向到了空设备文件，所以标准错误输出也重定向到空设备文件。 

3、/dev/zero文件代表一个永远输出 0的设备文件，使用它作输入可以得到全为空的文件。因此可用来创建新文件和以覆盖的方式清除旧文件。 

下面使用dd命令将从zero设备中创建一个10K大小（bs决定每次读写1024字节，count定义读写次数为10次），但内容全为0的文件。 
dd if=/dev/zero of=file count=10 bs=1024

[Shell脚本———— /dev/null 2>&1详解 - Tinywan - 博客园 (cnblogs.com)](https://www.cnblogs.com/tinywan/p/6025468.html)



### rm

```shell
#移除有相同字符的两个文件
rm -f "${HOME}"/.{yabai,skhd}rc
```







### ls

用来显示目录或具体文件列表

```shell
#每行列出一个文件，即以单列形式列出
$ ls -1
#列出所有文件,包括隐藏文件
$ ls -al
#所有文件的长列表形式(权限,所有权,大小,修改日期)
$ ls -al
#使用人可读单位（KB，MB，GB）显示大小的长格式列表
$ ls -lh
#按大小排序的长格式列表（从大到小）
$ ls -lS
#按大小排序的长格式列表（从小到大）
$ ls -ltr
#-t,sort by modification time, newest first
$ ls -t
```

ls 结合通配符

```shell
# Linux命令中使用的通配符有 ？ * [] ；
$ ls /usr/bin/w*  #列出指定目录下的所有以w开头的文件或目录 ；
$ ls /usr/bin/w?? #的效果是 列出指定目录下的以w开头名称长度为3的所有文件或目录 ；
$ ls /usr/bin/[xyz]* #的效果是 列出指定目录下的文件名以x或y或z开头的所有文件或目录 ；
$ ls /usr/bin/[!a-h]* #的效果是 列出指定目录下的文件名不以a到h区间字母开头的所有文件或
```

<img src="https://gitee.com/ibepo/ogcip/raw/master/20211126093338.png" alt="image-20211126093337734" style="zoom:50%;" />

### head

> head [参数]... [文件]...

 head命令输出文件开头部分，默认情况下显示文件的头10行。如果指定多个文件，每个文件前都有一个标题，给出文件名。如果没有指定文件，或当文件为-时，读取标准输入。

```shell
-c,--bytes=[-]K 显示文件前K字节。如果K前有-，则表示显示除最后K字节外的所有内容
-n,--lines=[-]K 显示前K行。如果K前有-，则表示显示除最后K行外的所有行
-q,--quiet,--silent 不显示标题文件名
-v,--verbose 总是显示标题文件名
--help 显示帮助信息并退出
--version 显示版本信息并退出
```

```shell
#显示文件的前10行
$head -n 10 1.txt

#显示文件的前10个字节
$head -c 10 1.txt

#显示从文件头到倒数第N个字符的内容
#2,就是除了文件末尾的两个字符不显示,其余都显示
$head -c -2 1.txt 
```

```shell
$tail -10： 查看文件的尾部的10行
$head -20：查看文件的头部20行
```

实战

列出文件夹中所有的 txt 格式的文档,按时间排序 取出最新的一个
注意 `bash`下可以 `ls  sth -t`,但是`zsh `下,要按照正常的`ls -t  sth`

```shell
$ls  *.txt -t |head -1
```



### ln

```bash
#ln 软连接指令,符号链接,类似于快捷方式
ln -s[原文件或目录][软连接]
# 在/home 下创建一个软连接 linktotest 连接到/root 目录
#[当前在/home 目录下] ln -s /root linktotest
# 删除软连接,虽然软连接是个文件夹 但是不要带斜杠
rm -rf linktotest
```

### history

```bash
# 显示执行过的所有制令
history
# 执行历史编号为 5 的指令
history 5
```

### which

`which`指令会在环境变量`$PATH`设置的目录里查找符合条件的文件

```bash
#查找某个命令的具体位置
$ which nvim
```

### whereis

有时，在使用命令行的时候，我们需要快速找到某一个命令的二进制文件所在位置。这种情况下可以选择 find 命令，但使用它会耗费时间，可能也会出现意料之外的情况。有一个专门为这种情况设计的命令：`whereis`

```bash
$ whereis systemd                                                        
systemd: /usr/lib/systemd /etc/systemd /usr/share/systemd /usr/share/man/man1/systemd.1.gz  
```

### w

可以看到有哪些用户以及主机登陆了这台机器

`load average`

linux 中的`load`是对当前 CPU 工作量的度量,简单的说就是进程队列的长度

`load average`就是一段时间(1 分钟,5 分钟,15 分钟)内平均`load`

第一行数据从前往后分别是 1 分钟,5 分钟,15 分钟的负载

注:`linux`系统是 5 秒钟进行一次 load 采样.

```shell
ubuntu@timehouse:~$ w
 09:05:31 up 71 days, 21:34,  1 user,  load average: 0.02, 0.05, 0.06
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
ubuntu   pts/0    106.117.224.230  09:04    0.00s  0.01s  0.00s w
```

```shell
查看cpu 核数命令
$ grep 'model name' /proc/cpuinfo | wc -l
```



### chmod

`chmod`修改文件权限

```shell
#将 xxx/logos 下的所有文件执行全部组可读权限
$ /panghu/nav/nginx/html/nav/assets/images/logos# chmod 644 *
```

```shell
mkdir -p #-p, --parents     需要时创建上层目录，如目录早已存在则不当作错误
cat /etc/passwd #查看用户
chmod -R  777 /dir   #将此文件夹的权限设为谁都可以
chown -R  ibepo:dev  /home/ibepo  #修改目录的拥有者是root用户和root组 
```



#### `-rw-rw-r-- `

最前面那个 - 代表的是类型(-文件 d 文件夹)
中间那三个 rw- 代表的是所有者（user）
然后那三个 rw- 代表的是组群（group）
最后那三个 r-- 代表的是其他人（other）

`r` 表示文件可以被读（read）

 `w `表示文件可以被写（write）

 `x `表示文件可以被执行（如果它是程序的话） - 表示相应的权限还没有被授予

#### 常见权限

|  权限表示  | 权限代码 |  所有者权限  |   群组权限   |  所有人权限  |
| :--------: | :------: | :----------: | :----------: | :----------: |
| -rwxrwxrwx |   777    | 读、写、执行 | 读、写、执行 | 读、写、执行 |
| -rw-rw-rw- |   666    |    读、写    |    读、写    |    读、写    |
| -rw------- |   600    |    读、写    |      -       |      -       |
| -rw-r–r--  |   644    |    读、写    |      读      |      读      |
| -rwx------ |   700    | 读、写、执行 |      -       |      -       |
| -rwxr-xr-x |   755    | 读、写、执行 |   读、执行   |   读、执行   |
| -rwx–x--x  |   711    | 读、写、执行 |     执行     |     执行     |

#### 修改权限

```
# 文件
chmod 777 demo.txt  # 一个文件 可写可读可执行

chmod 777 *.txt   # 目录下所有 txt 文件 可写可读可执行

chmod 777 *.*  # 目录下所有文件 可写可读可执行

# 目录
chmod 777 /demo  # 目录 可写可读可执行

chmod 777 *  # 目录下所有的文件夹

chmod -R 777 /demo   # 修改文件夹内所有的文件和文件夹及子文件夹

```

u 代表所有者（user）
g 代表所有者所在的组群（group）
o 代表其他人，但不是u和g （other）
a 代表全部的人，也就是包括u，g和o
r 表示文件可以被读（read）
w 表示文件可以被写（write）
x 表示文件可以被执行（如果它是程序的话）

其中：rwx也可以用数字来代替

```
r ------------4
w ------------2
x ------------1
- ------------0
```

### paste

```shell
paste file1 file2         #合并两个文件或两栏的内容
paste -d '+' file1 file2  #合并两个文件或两栏的内容，中间用"+"区分
```



### sort

```shell
sort file1 file2           #排序两个文件的内容
sort file1 file2 | uniq    #取出两个文件的并集(重复的行只保留一份)
sort file1 file2 | uniq -u #删除交集，留下其他的行
sort file1 file2 | uniq -d #取出两个文件的交集(只留下同时存在于两个文件中的文件)

```

### tar

```shell
（对文件进行打包，默认情况并不会压缩，如果指定了相应的参数，它还会调用相应的压缩程序（如gzip和bzip等）进行压缩和解压）
-c         # 小写c新建打包文件
-t         #查看打包文件的内容含有哪些文件名
-x         #解打包或解压缩的功能，可以搭配-C（大写）指定解压的目录，注意-c,-t,-x不能同时出现在同一条命令中
-j         #通过bzip2的支持进行压缩/解压缩
-z         #通过gzip的支持进行压缩/解压缩
-v         #在压缩/解压缩过程中，将正在处理的文件名显示出来
-f filename#filename为要处理的文件
-C dir     #指定压缩/解压缩的目录dir
压缩：tar -jcv -f filename.tar.bz2 要被处理的文件或目录名称
查询：tar -jtv -f filename.tar.bz2
解压：tar -jxv -f filename.tar.bz2 -C 欲解压缩的目录
bunzip2 file1.bz2 #解压一个叫做 'file1.bz2'的文件
bzip2 file1       #压缩一个叫做 'file1' 的文件
gunzip file1.gz   #解压一个叫做 'file1.gz'的文件
gzip file1        #压缩一个叫做 'file1'的文件
gzip -9 file1     #最大程度压缩
rar a file1.rar test_file 创建一个叫做 'file1.rar' 的包
tar -xzvf file.tar.gz #解压tar.gz
```





### grep/sed/awk

测试文本

```
cat caatbar catfoobar
```

匹配带有字符` cat` 的文本

```/cat/```

匹配c 后边至少有一个 `a`的文本

```
/cat{1,}/
```

只匹配 cat,`\b`字符边界

```
/\bcat\b/
```

高屏操作

```shell
#（分析一行的信息，若当中有我们所需要的信息，就将该行显示出来，该命令通常与管道命令一起使用，用于对一些命令的输出进行筛选加工等等）

grep Aug /var/log/messages  #在文件 '/var/log/messages'中查找关键词"Aug"
grep ^Aug /var/log/messages #在文件 '/var/log/messages'中查找以"Aug"开始的词汇
grep [0-9] /var/log/messages #选择 '/var/log/messages' 文件中所有包含数字的行
grep Aug -R /var/log/*       # 在目录 '/var/log' 及随后的目录中搜索字符串"Aug"

#将example.txt文件中的 "string1" 替换成 "string2"
sed 's/stringa1/stringa2/g' example.txt 
#从example.txt文件中删除所有空白行，前面的^指行首，$指行尾，最后的d指删除的意思。
sed '/^$/d' example.txt                 
```



-  https://juejin.cn/post/6844903845227659271



### brctl

`网桥管理工具brctl `

```shell
#Centos系统
$ yum install bridge-utils

#Ubuntu系统   
$ apt-get  install bridge-utils

#显示所有的网桥信息
$ sudo brctl show

#显示某个网桥(br0)的信息
$ sudo brctl show br0
```



### lsof

`lsof`(list open files)是一个列出当前系统打开文件的工具。

```bash
#列出所有的端口占用情况
$ lsof -i
#查看端口占用情况
$ lsof -i:8080

$ lsof abc.txt                       #显示开启文件abc.txt的进程
$ lsof -c abc：                      #显示abc进程现在打开的文件
$ lsof -c -p 1234                    #列出进程号为1234的进程所打开的文件
$ lsof -g gid                        #显示归属gid的进程情况
$ lsof +d /usr/local/                #显示目录下被进程开启的文件
$ lsof +D /usr/local/                #同上，但是会搜索目录下的目录，时间较长
$ lsof -d 4                          #显示使用fd为4的进程
$ lsof -i -U                         #显示所有打开的端口和UNIX domain文件
```



### netstat

```bash
$ netstat -ntlp   //查看当前所有tcp端口

$ netstat -ntulp | grep 80   //查看所有80端口使用情况

$ netstat -ntulp | grep 3306   //查看所有3306端口使用情况

$ netstat -tunpl
```

参数项

- -t (tcp) 仅显示tcp相关选项

- -u (udp)仅显示udp相关选项

- -n 拒绝显示别名，能显示数字的全部转化为数字

- -l 仅列出在Listen(监听)的服务状态

- -p 显示建立相关链接的程序名

### rsync

`rsync` 被用来与远程服务器间传送文件，与 `scp` 类似，但 `rsync` 可以实现增量传送

如需要传输k8s所需要的镜像压缩包时: 首次打包了总共5个镜像为 k8s.tar，传输到目标节点。随后发现一个镜像没有打包，于是再次打包，总共6个镜像为 k8s.tar，再次传输到目标节点。`rsync` 可以对比文件差异而做到仅传输最后一次丢掉的镜像。

```shell
# 把本机的 k8s.tar 传送到 shanyue 服务器的 /root 目录
# -a 代表归档
# -v 代表打印详细信息，这个参数很常见了 --verbose
# -h 代表打印可读性好的信息，这个参数也很常见 --human-readable
# -z 代表打包传送，减小传送体积
$ rsync -avhzP k8s.tar shanyue:/root
```

### 防火墙

```bash
netstat -ntlp   #查看当前所有tcp端口
netstat -ntulp |grep 1935   #查看所有1935端口使用情况
tt -tal #查看 soket 套接字运行状况
systemctl start firewalld #开启防火墙 
```

```bash
#开放指定端口
# 命令含义：
#--zone #作用域
#--add-port=1935/tcp  #添加端口，格式为：端口/通讯协议
#--permanent  #永久生效，没有此参数重启后失效
firewall-cmd --zone=public --add-port=1935/tcp --permanent    
```

```bash
firewall-cmd --reload #重启防火墙
```

### curl

[curl 的用法指南 - 阮一峰的网络日志 (ruanyifeng.com)](http://www.ruanyifeng.com/blog/2019/09/curl-reference.html)

[还在用 Postman？手把手教你用 Curl 提高工作效率](https://developer.51cto.com/art/202111/689151.htm)


```bash

#curl,
#下边代码演示的是通过 curl 下载 docker-compose,并下载到指定位置,然后增加执行的权限给全局

curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

#-L 跟随重定向跳转
#-o参数将服务器的回应保存成文件，等同于wget命令。
#-O参数将服务器回应保存成文件，并将 URL 的最后部分当作文件名。
#-s参数将不输出错误和进度信息
#-S参数指定只输出错误信息，通常与-s一起使用。
#-v参数输出通信的整个过程，用于调试。
#-x参数指定 HTTP 请求的代理。
#-X参数指定 HTTP 请求的方法。
chmod +x /usr/local/bin/docker-compose
```

`curl`高频操作

```shell
# 发送 get 请求
$ curl www.baidu.com

# 使用-i选项,打印服务器响应的http头部信息
$ curl -i www.baidu.com

# 使-l 选项,打印响应头信息,注意此时发送的是 head 请求
# -I 向服务器发送HEAD请求 --head 等同于【-I】
$ curl -l www.baidu.com

# 通过-H选项,可以为请求添加头
# 可以指定多个-H选项 
$ curl -H 'Accept-Language: en-US' -H 'Secret-Message: xyzzy' http://google.com 

#使用 -o 或 -O 选项，可以将网络资源保存到文件中
#如果想显示下载进度条，可以使用 -# 选项
# 等效于 wget 
$ curl -o chopin.html http://linuxblogs.cn 
# -O 选项，可以将 URL 的最后部分当做文件名 
$ curl -O http://linuxblogs.cn/bar.html 


#我们可以使用 > 符号将输出重定向到本地文件中
curl http://www.baidu.com > index.html
```

##### 选项

- -A 指定User-Agent
- -b 发送Cookie
- -c Cookie写入文件
- -D 输出响应标头
- -d 发送请求对，默认发送POST请求，且HTTP 请求加上标头【Content-Type : application/x-www-form-urlencoded】，【-G】可以覆盖默认设置
- --data-urlencode 类似-d，数据会进行URL编码
- -e 设置Referer
- -F 上传二进制文件，HTTP 请求加上标头【Content-Type: multipart/form-data】
- -G 发送GET请求
- -H 添加HTTP请求的标头
- --head 等同于【-I】
- -i 打印服务器返回的HTTP标头
- -I 向服务器发送HEAD请求
- -L HTTP请求跟随服务器的重定向，默认不重定向
- --limit-rate 限制带宽
- -m 设置超时时间
- -M 显示curl手册
- -o 【文件名】服务器的回应保存成文件
- -O 服务器的回应保存成文件，自动命名
- -s 安静模式
- -S 覆盖-s，输出错误信息
- -T 上传文件
- -u 设置登录用户名和密码
- -v 输出通信整个过程
- -x 指定HTTP请求的代理
- -X 指定HTTP请求方法



### wget

```bash
wget

```

### ps 

[~~Linux查看所有service的状态~~](https://blog.csdn.net/weixin_40367126/article/details/104670163 )

[服务器监控指标小记 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/90303333)

[linux每日命令(34):ps命令和pstree命令 - Aray007 - 博客园 (cnblogs.com)](https://www.cnblogs.com/zhongbokun/p/10296760.html)

```bash
#ps
ps -A #显示所有进程
ps -ef #显示所有进程连带命令行
ps -ef|grep mysql  #查看mysql进程
ps -u root #显示 root 用户的进程状态
ps -l #列出这次登陆的 pid 和与其相关的状态,在预设的情况下， ps 仅会列出与目前所在的 bash shell 有关的 PID 而已，所以， 当我使用 ps -l 的时候，只有三个 PID。
ps -axjf #以类似进程树的结构显示
ps -aux | more #可以用 | 管道和 more 连接起来分页查看
```

```shell
（用于将某个时间点的进程运行情况选取下来并输出，process之意）

-a      #所有的进程均显示出来
-u      #有效用户的相关进程
-l      #较长，较详细地将PID的信息列出
-f      #展示出进程的uids, ppids
```

```shell
ps aux # 查看系统所有的进程数据
ps ax  # 查看不与terminal有关的所有进程
ps -lA # 查看系统所有的进程数据
ps axjf # 查看连同一部分进程树状态
```



命令行选项

| 参数 | 描述                                             |
| ---- | ------------------------------------------------ |
| -A   | 列出所有的行程                                   |
| -e   | 等于“-A”                                         |
| -a   | 显示现行终端机下的所有进程，包括其他用户的进程； |
| -u   | 以用户为主的进程状态 ；                          |
| x    | 通常与 a 这个参数一起使用，可列出较完整信息。    |
| -w   | 显示加宽可以显示较多的资讯                       |
| -au  | 显示较详细的资讯                                 |
| -aux | 显示所有包含其他使用者的行程                     |
| -f   | 做一个更为完整的输出。                           |

各相关信息的意义

| 标志  | 意义                                                         |
| ----- | ------------------------------------------------------------ |
| F     | 代表这个程序的旗标 (flag)， 4 代表使用者为 super user        |
| S     | 代表这个程序的状态 (STAT)，关于各 STAT 的意义将在内文介绍(参见附表①) |
| UID   | 程序被该 UID 所拥有                                          |
| PID   | 就是这个程序的 ID ！                                         |
| PPID  | 则是其上级父程序的ID                                         |
| C     | CPU 使用的资源百分比                                         |
| PRI   | 指进程的执行优先权(Priority的简写)，其值越小越早被执行；     |
| NI    | 这个进程的nice值，其表示进程可被执行的优先级的修正数值。     |
| ADDR  | 这个是内核函数，指出该程序在内存的那个部分。如果是个 running的程序，一般就是 "-" |
| SZ    | 使用掉的内存大小                                             |
| WCHAN | 目前这个程序是否正在运作当中，若为 - 表示正在运作            |
| TTY   | 登入者的终端机位置                                           |
| TIME  | 使用掉的 CPU 时间。                                          |
| CMD   | 所下达的指令为何                                             |

附表①[ps工具标识进程的5种状态码]

- D ：不可中断 uninterruptible sleep (usually IO)
- R ：该程序目前正在运作，或者是可被运作
- S ：该程序目前正在睡眠当中 (可说是 idle 状态)，但可被某些讯号 (signal) 唤醒。
- T ：该程序目前正在侦测或者是停止了
- Z ：该程序应该已经终止，但是其父程序却无法正常的终止他，造成 zombie (疆尸) 程序的状态



### ps |aux

| 标志    | 意义                                                         |
| ------- | ------------------------------------------------------------ |
| USER    | 该 process 属于那个使用者账号的                              |
| PID     | 该 process 的号码                                            |
| %CPU    | 该 process 使用掉的 CPU 资源百分比                           |
| %MEM    | 该 process 所占用的物理内存百分比                            |
| VSZ     | 该 process 使用掉的虚拟内存量 (Kbytes)                       |
| RSS     | 该 process 占用的固定的内存量 (Kbytes)                       |
| TTY     | 该 process 是在那个终端机上面运作，若与终端机无关，则显示 ?，另外， tty1-tty6 是本机上面的登入者程序，若为 pts/0 等等的，则表示为由网络连接进主机的程序。 |
| STAT    | 该程序目前的状态                                             |
| START   | 该 process 被触发启动的时间,STAT：该程序目前的状态，主要的状态有 |
| TIME    | 该 process 实际使用 CPU 运作的时间                           |
| COMMAND | 该程序的实际指令                                             |

### pstree

> pstree命令以树状图显示进程间的关系（display a tree of processes）。ps命令可以显示当前正在运行的那些进程的信息，但是对于它们之间的关系却显示得不够清晰。在Linux系统中，系统调用fork可以创建子进程，通过子shell也可以创建子进程，Linux系统中进程之间的关系天生就是一棵树，树的根就是进程PID为1的init进程。

```bash
pstree -p #以树状图显示进程同时还显示PID

#以树状图显示进程PID为的进程以及子孙进程，如果有-p参数则同时显示每个进程的PID
pstree [-p] <pid> 
pstree -p 21858 

pstree -p | less #因为pstree输出的信息可能比较多，所以最好与more/less配合使用,使用上下箭头查看，按q退出
```

### systemd

>Systemd 就是为了解决这些问题而诞生的。它的设计目标是，为系统的启动和管理提供一套完整的解决方案。根据 Linux 惯例，字母`d`是守护进程（daemon）的缩写。 Systemd 这个名字的含义，就是它要守护整个系统。

![img](https://gitee.com/ibepo/ogcip/raw/master/20210930122501.png)





###### 系统管理

`Systemd` 并不是一个命令，而是一组命令，涉及到系统管理的方方面面。

`systemctl`是 Systemd 的主命令，用于管理系统

```bash
# 重启系统
$ sudo systemctl reboot

# 关闭系统，切断电源
$ sudo systemctl poweroff

# CPU停止工作
$ sudo systemctl halt

# 暂停系统
$ sudo systemctl suspend

# 让系统进入冬眠状态
$ sudo systemctl hibernate

# 让系统进入交互式休眠状态
$ sudo systemctl hybrid-sleep

# 启动进入救援状态（单用户状态）
$ sudo systemctl rescue
```



`hostnamectl`命令用于查看当前主机的信息

```bash
# 显示当前主机的信息
$ hostnamectl

# 设置主机名。
$ sudo hostnamectl set-hostname rhel7
```

### 

`localectl`命令用于查看本地化设置。

 ```bash
 # 查看本地化设置
 $ localectl
 
 # 设置本地化参数。
 $ sudo localectl set-locale LANG=en_GB.utf8
 $ sudo localectl set-keymap en_GB
 ```



`timedatectl`命令用于查看当前时区设置。

 ```bash
 # 查看当前时区设置
 $ timedatectl
 
 # 显示所有可用的时区
 $ timedatectl list-timezones                                                                                   
 
 # 设置当前时区
 $ sudo timedatectl set-timezone America/New_York
 $ sudo timedatectl set-time YYYY-MM-DD
 $ sudo timedatectl set-time HH:MM:SS
 ```



`loginctl`命令用于查看当前登录的用户。

 ```bash
 # 列出当前session
 $ loginctl list-sessions
 
 # 列出当前登录用户
 $ loginctl list-users
 
 # 列出显示指定用户的信息
 $ loginctl show-user ruanyf
 ```

参考网址

[Systemd 入门教程：实战篇 - 阮一峰的网络日志 (ruanyifeng.com)](https://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-part-two.html)

[使用Systemctl命令来管理系统服务 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/388897743)

[systemctl 设置自定义服务管理（以nginx为例） ](https://segmentfault.com/a/1190000009723940)

[linux systemctl 指令 —— 阮一峰 - 七脉 - 博客园 (cnblogs.com)](https://www.cnblogs.com/zwcry/p/9602756.html)

[🦍Systemd 入门教程：命令篇 - 阮一峰的网络日志 (ruanyifeng.com)](http://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-commands.html)



###### Unit含义

Systemd 可以管理所有系统资源。不同的资源统称为`Unit`（单位）。

Unit 一共分成12种。

> - Service unit：系统服务
> - Target unit：多个 Unit 构成的一个组
> - Device Unit：硬件设备
> - Mount Unit：文件系统的挂载点
> - Automount Unit：自动挂载点
> - Path Unit：文件或路径
> - Scope Unit：不是由 Systemd 启动的外部进程
> - Slice Unit：进程组
> - Snapshot Unit：Systemd 快照，可以切回某个快照
> - Socket Unit：进程间通信的 socket
> - Swap Unit：swap 文件
> - Timer Unit：定时器

`systemctl list-units`命令可以查看当前系统的所有 Unit 。

```bash
$ systemctl list-units                         #列出所有运行中单元
$ systemctl list-units --all                   #列出所有Unit，包括没有找到配置文件的或者启动失败的
$ systemctl list-units --all --state=inactive  #列出所有没有运行的 Unit
$ systemctl list-units --type=service          #列出所有正在运行的、类型为 service 的 Unit 
$ systemctl list-units --failed                #🦍列出所有加载失败的 Unit
```

###### Unit 状态

`systemctl status`命令用于查看系统状态和单个 Unit 的状态。

```bash
$ systemctl status nginx.service                              # 显示单个 Unit 的状态     
$ systemctl status                                            # 显示系统状态
$ systemctl status bluetooth.service                          # 显示单个 Unit 的状态
$ systemctl -H root@rhel7.example.com status httpd.service    # 显示远程主机的某个 Unit 的状态
```

```vim
nginx.service - nginx - high performance web server                                          
   Loaded: loaded (/usr/lib/systemd/system/nginx.service; disabled; vendor preset: disabled) 
   Active: active (running) since Tue 2021-09-28 10:23:24 CST; 19min ago                     
  Process: 24489 ExecStop=/usr/local/nginx/sbin/nginx -s stop (code=exited, status=1/FAILURE) 
  Process: 24512 ExecStart=/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf (code=exited, status=0/SUCCESS)                                                               
  Process: 24511 ExecStartPre=/usr/local/nginx/sbin/nginx -t -c /usr/local/nginx/conf/nginx.conf (code=exited, status=0/SUCCESS)                                            
 Main PID: 24514 (nginx)                                                                     
    Tasks: 2                                                                                 
   Memory: 1000.0K                                                                           
   CGroup: /system.slice/nginx.service                                                       
           ├─24514 nginx: master process /usr/local/nginx/sbin/nginx -c /usr/local/nginx/con...
           └─24515 nginx: worker process   
```

- `Loaded`行：配置文件的位置，是否设为开机启动
- `Active`行：表示正在运行
- `Main PID`行：主进程ID
- `Status`行：由应用本身（这里是 httpd ）提供的软件当前状态
- `CGroup`块：应用的所有子进程
- 日志块：应用的日志

🦍除了`status`命令，`systemctl`还提供了三个查询状态的简单方法，主要供脚本内部的判断语句使用。

```bash
# 显示某个 Unit 是否正在运行
$ systemctl is-active application.service

# 显示某个 Unit 是否处于启动失败状态
$ systemctl is-failed application.service

# 显示某个 Unit 服务是否建立了自启动链接
$ systemctl is-enabled application.service
```

######  Unit 管理

对于用户来说，最常用的是下面这些命令，用于启动和停止 Unit（🦍主要是 service）。

 ```bash
 # 立即启动一个服务
 $ sudo systemctl start apache.service
 
 # 立即停止一个服务
 $ sudo systemctl stop apache.service
 
 # 重启一个服务
 $ sudo systemctl restart apache.service
 
 # 杀死一个服务的所有子进程
 $ sudo systemctl kill apache.service
 
 # 重新加载一个服务的配置文件
 $ sudo systemctl reload apache.service

 # 重载所有修改过的配置文件
 $ sudo systemctl daemon-reload
 
 # 🦍显示某个 Unit 的所有底层参数
 $ systemctl show nginx.service
 
# 显示某个 Unit 的指定属性的值
 $ systemctl show -p CPUShares httpd.service

 # 设置某个 Unit 的指定属性
 $ sudo systemctl set-property httpd.service CPUShares=500
 ```



###### 依赖关系

Unit 之间存在依赖关系：A 依赖于 B，就意味着 Systemd 在启动 A 的时候，同时会去启动 B。

`systemctl list-dependencies`命令列出一个 Unit 的所有依赖。

```bash
$ systemctl list-dependencies nginx.service
```

🦍上面命令的输出结果之中，有些依赖是 Target 类型（详见下文），默认不会展开显示。如果要展开 Target，就需要使用`--all`参数。

 ```bash
 $ systemctl list-dependencies --all nginx.service
 ```



###### Unit 配置

######      ① 概述

每一个 Unit 都有一个配置文件，告诉 Systemd 怎么启动这个 Unit 。

Systemd 默认从目录`/etc/systemd/system/`读取配置文件。但是，里面存放的大部分文件都是符号链接，指向目录`/usr/lib/systemd/system/`，真正的配置文件存放在那个目录。

`systemctl enable`命令用于在上面两个目录之间，建立符号链接关系。

 ```bash
 $ sudo systemctl enable clamd@scan.service
 # 等同于
 $ sudo ln -s '/usr/lib/systemd/system/clamd@scan.service' '/etc/systemd/system/multi-user.target.wants/clamd@scan.service'
 ```



`systemctl enable`

如果配置文件里面设置了开机启动，`systemctl enable`命令相当于激活开机启动。

与之对应的，`systemctl disable`命令用于在两个目录之间，撤销符号链接关系，相当于撤销开机启动。

```bash
$ sudo systemctl disable clamd@scan.service
```

配置文件的后缀名，就是该 Unit 的种类，比如`sshd.socket`。如果省略，Systemd 默认后缀名为`.service`，所以`sshd`会被理解成`sshd.service`。



###### ②配置文件的状态

`systemctl list-unit-files`命令用于列出所有配置文件。注意，从配置文件的状态无法看出，该 Unit 是否正在运行。这必须执行前面提到的`systemctl status`命令。

```bash
# 列出所有配置文件
$ systemctl list-unit-files
# 列出指定类型的配置文件
$ systemctl list-unit-files --type=service
```

这个命令会输出一个列表,附录①

````bash
UNIT FILE              STATE
chronyd.service        enabled
clamd@.service         static
clamd@scan.service     disabled
````

附录①

- enabled：已建立启动链接
- disabled：没建立启动链接
- static：该配置文件没有`[Install]`部分（无法执行），只能作为其他配置文件的依赖
- masked：该配置文件被禁止建立启动链接



xxx. service

①进入systemctl status ng.service文件夹

```bash
#systemctl
cd /usr/lib/systemd/system    #进入/usr/lib/systemd/system
vi tomcat.service #以tomcat为例，/usr/lib/systemd/system下创建tomcat.service文件
```

②编写 tomcat.service 启动文件

```shell
#tomcat.service
[Unit]
Description=tomcatapi
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/apache-tomcat-8.5.29/bin/startup.sh #服务启动的命令（对应你自己服务器的命令）
ExecReload=
ExecStop=/usr/local/apache-tomcat-8.5.29/bin/shutdown.sh #服务停止的命令（同理）
PrivateTmp=true

[Install]
WantedBy=multi-user.target

```

③添加 tomcat.service 文件的启动权限

```
chmod +x tomcat.service
```

④测试

```bash
 systemctl stop tomcat
 systemctl start tomcat
```



###### ③配置文件的格式

配置文件就是普通的文本文件，可以用文本编辑器打开。

`systemctl cat`命令可以查看配置文件的内容。

 ```bash
 $ systemctl cat atd.service
 
 [Unit]
 Description=ATD daemon
 
 [Service]
 Type=forking
 ExecStart=/usr/bin/atd
 
 [Install]
 WantedBy=multi-user.target
 ```

从上面的输出可以看到，配置文件分成几个区块。每个区块的第一行，是用方括号表示的区别名，比如`[Unit]`。注意，配置文件的区块名和字段名，都是大小写敏感的。

每个区块内部是一些等号连接的键值对。

 ```bash
 [Section]
 Directive1=value
 Directive2=value
 ```

注意，键值对的等号两侧不能有空格。



###### ④配置文件的区块

`[Unit]`区块通常是配置文件的第一个区块，用来定义 Unit 的元数据，以及配置与其他 Unit 的关系。

`[Install]`通常是配置文件的最后一个区块，用来定义如何启动，以及是否开机启动。

`[Service]`区块用来 Service 的配置，只有 Service 类型的 Unit 才有这个区块。



````bash
systemctl cat sshd.service

[Unit]
Description=OpenSSH server daemon
Documentation=man:sshd(8) man:sshd_config(5)

#After字段表示如果network.target或sshd-keygen.service需要启动，那么sshd.service应该在它们之后启动。定义sshd.service应该在哪些服务之前启动。
After=network.target sshd-keygen.service 

#Wants字段：表示sshd.service与sshd-keygen.service之间存在"弱依赖"关系，即如果"sshd-eygen.service"启动失败或停止运行，不影响sshd.service继续执行。
Wants=sshd-keygen.service

[Service]
#EnvironmentFile字段：指定当前服务的环境参数文件。该文件内部的key=value键值对，可以用$key的形式，在当前配置文件中获取。
EnvironmentFile=/etc/sysconfig/sshd

#♠ExecStart字段：定义启动进程时执行的命令。
#执行的命令是/usr/sbin/sshd -D $OPTIONS，其中的变量$OPTIONS就来自EnvironmentFile字段指定的环境参数文件。
ExecStart=/usr/sbin/sshd -D $OPTIONS

ExecReload=/bin/kill -HUP $MAINPID

#Type字段定义启动类型。它可以设置的值如下,附录①
Type=simple

#KillMode字段：定义 Systemd 如何停止 sshd 服务。
#上面这个例子中，将KillMode设为process，表示只停止主进程，不停止任何sshd 子进程，即子进程打开的 SSH #session 仍然保持连接。这个设置不太常见，但对 sshd 很重要，否则你停止服务的时候，会连自己打开的 SSH #session 一起杀掉。,附录②
KillMode=process

#Restart字段：定义了 sshd 退出后，Systemd 的重启方式。
#Restart设为on-failure，表示任何意外的失败，就将重启sshd。如果 sshd 正常停止（比如执行systemctl stop命
#令），它就不会重启,附录③
Restart=on-failure

#RestartSec字段：表示 Systemd 重启服务之前，需要等待的秒数。上面的例子设为等待42秒。
RestartSec=42s

[Install]
WantedBy=multi-user.target
````

附录①:

`Type`字段定义启动类型。它可以设置的值如下

- simple（默认值）：`ExecStart`字段启动的进程为主进程
- forking：`ExecStart`字段将以`fork()`方式启动，此时父进程将会退出，子进程将成为主进程
- oneshot：类似于`simple`，但只执行一次，Systemd 会等它执行完，才启动其他服务
- dbus：类似于`simple`，但会等待 D-Bus 信号后启动
- notify：类似于`simple`，启动结束后会发出通知信号，然后 Systemd 再启动其他服务
- idle：类似于`simple`，但是要等到其他任务都执行完，才会启动该服务。一种使用场合是为让该服务的输出，不与其他服务的输出相混合



附录②:

`KillMode`字段可以设置的值如下。

- control-group（默认值）：当前控制组里面的所有子进程，都会被杀掉
- process：只杀主进程
- mixed：主进程将收到 SIGTERM 信号，子进程收到 SIGKILL 信号
- none：没有进程会被杀掉，只是执行服务的 stop 命令。



附录③:

`Restart`字段可以设置的值如下。

- no（默认值）：退出后不会重启
- on-success：只有正常退出时（退出状态码为0），才会重启
- on-failure：非正常退出时（退出状态码非0），包括被信号终止和超时，才会重启
- on-abnormal：只有被信号终止和超时，才会重启
- on-abort：只有在收到没有捕捉到的信号终止时，才会重启
- on-watchdog：超时退出，才会重启
- always：不管是什么退出原因，总是重启



###### Target

启动计算机的时候，需要启动大量的 Unit。如果每一次启动，都要一一写明本次启动需要哪些 Unit，显然非常不方便。Systemd 的解决方案就是 Target。

简单说，Target 就是一个 Unit 组，包含许多相关的 Unit 。启动某个 Target 的时候，Systemd 就会启动里面所有的 Unit。从这个意义上说，Target 这个概念类似于"状态点"，启动某个 Target 就好比启动到某种状态。

传统的`init`启动模式里面，有 RunLevel 的概念，跟 Target 的作用很类似。不同的是，RunLevel 是互斥的，不可能多个 RunLevel 同时启动，但是多个 Target 可以同时启动。

```bash
# 查看当前系统的所有 Target
$ systemctl list-unit-files --type=target

# 查看一个 Target 包含的所有 Unit
$ systemctl list-dependencies multi-user.target

# 查看启动时的默认 Target
$ systemctl get-default

# 设置启动时的默认 Target
$ sudo systemctl set-default multi-user.target

# 切换 Target 时，默认不关闭前一个 Target 启动的进程，
# systemctl isolate 命令改变这种行为，
# 关闭前一个 Target 里面所有不属于后一个 Target 的进程
$ sudo systemctl isolate multi-user.target
```

`Target` 与 传统 `RunLevel` 的对应关系如下。

```bahs
Traditional runlevel      New target name     Symbolically linked to...

Runlevel 0           |    runlevel0.target -> poweroff.target
Runlevel 1           |    runlevel1.target -> rescue.target
Runlevel 2           |    runlevel2.target -> multi-user.target
Runlevel 3           |    runlevel3.target -> multi-user.target
Runlevel 4           |    runlevel4.target -> multi-user.target
Runlevel 5           |    runlevel5.target -> graphical.target
Runlevel 6           |    runlevel6.target -> reboot.target
```

Target与 init 进程的主要差别

**（1）默认的 RunLevel**（在`/etc/inittab`文件设置）现在被默认的 Target 取代，位置是`/etc/systemd/system/default.target`，通常符号链接到`graphical.target`（图形界面）或者`multi-user.target`（多用户命令行）。

**（2）启动脚本的位置**，以前是`/etc/init.d`目录，符号链接到不同的 RunLevel 目录 （比如`/etc/rc3.d`、`/etc/rc5.d`等），现在则存放在`/lib/systemd/system`和`/etc/systemd/system`目录。

**（3）配置文件的位置**，以前`init`进程的配置文件是`/etc/inittab`，各种服务的配置文件存放在`/etc/sysconfig`目录。现在的配置文件主要存放在`/lib/systemd`目录，在`/etc/systemd`目录里面的修改可以覆盖原始设置。



###### 日志管理

Systemd 统一管理所有 Unit 的启动日志。带来的好处就是，可以只用`journalctl`一个命令，查看所有日志（内核日志和应用日志）。日志的配置文件是`/etc/systemd/journald.conf`。

`journalctl`功能强大，用法非常多。

```bash
# 查看所有日志（默认情况下 ，只保存本次启动的日志）
$ sudo journalctl

# 查看内核日志（不显示应用日志）
$ sudo journalctl -k

# 查看系统本次启动的日志
$ sudo journalctl -b
$ sudo journalctl -b -0

# 查看上一次启动的日志（需更改设置）
$ sudo journalctl -b -1

# 查看指定时间的日志
$ sudo journalctl --since="2012-10-30 18:17:16"
$ sudo journalctl --since "20 min ago"
$ sudo journalctl --since yesterday
$ sudo journalctl --since "2015-01-10" --until "2015-01-11 03:00"
$ sudo journalctl --since 09:00 --until "1 hour ago"

# 显示尾部的最新10行日志
$ sudo journalctl -n

# 显示尾部指定行数的日志
$ sudo journalctl -n 20

# 实时滚动显示最新日志
$ sudo journalctl -f

# 查看指定服务的日志
$ sudo journalctl /usr/lib/systemd/systemd

# 查看指定进程的日志
$ sudo journalctl _PID=1

# 查看某个路径的脚本的日志
$ sudo journalctl /usr/bin/bash

# 查看指定用户的日志
$ sudo journalctl _UID=33 --since today

# 查看某个 Unit 的日志
$ sudo journalctl -u nginx.service
$ sudo journalctl -u nginx.service --since today

# 实时滚动显示某个 Unit 的最新日志
$ sudo journalctl -u nginx.service -f

# 合并显示多个 Unit 的日志
$ journalctl -u nginx.service -u php-fpm.service --since today

# 查看指定优先级（及其以上级别）的日志，共有8级
# 0: emerg
# 1: alert
# 2: crit
# 3: err
# 4: warning
# 5: notice
# 6: info
# 7: debug
$ sudo journalctl -p err -b

# 日志默认分页输出，--no-pager 改为正常的标准输出
$ sudo journalctl --no-pager

# 以 JSON 格式（单行）输出
$ sudo journalctl -b -u nginx.service -o json

# 以 JSON 格式（多行）输出，可读性更好
$ sudo journalctl -b -u nginx.serviceqq
 -o json-pretty

# 显示日志占据的硬盘空间
$ sudo journalctl --disk-usage

# 指定日志文件占据的最大空间
$ sudo journalctl --vacuum-size=1G

# 指定日志文件保存多久
$ sudo journalctl --vacuum-time=1years
```



### 用户

[ Linux环境下为普通用户添加sudo权限](https://blog.csdn.net/qq_39290007/article/details/81125750?utm_medium=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromMachineLearnPai2~default-3.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromMachineLearnPai2~default-3.no_search_link)

```bash
#创建用户 
useradd xiaoming #当用户创建后,将在/home 下自动创建同名的家目录 /home/xiaoming
useradd -d /home/tiger xiaoming #创建小明账号,并自动创建他的家目录是/home/tinger

visudo #注意编辑/etc/sudoers 文件,将 自己安排的 dev 用户组增加 root 所有拥有的权限,这里选择需要密码 ,防呆设计

#查看用户
cat /etc/passwd 

#创建密码
passwd xiaoming  回车后输入密码

#删除用户
userdel xiaoming    #只删除用户,保留家目录
userdel -r xiaoming #删除用户和其家目录

#查询用户基本信息
id xiaoming

#切换用户 swith user
su ibepo #切换用户
su -ibepo #切换用户,并跳转到切换的用户的家目录下
su #切换至 root 用户
exit #返回到原来的用户

#以 root 的权限运行某指令
sudo
sudo su - #以 root 权限切换至 root 用户,并切换到 root 目录下
```





### 用户组

```bash
#增加组
groupadd wudang #创建武当组

#删除组
groupdel wudang

#增加一个用户张无忌,将他指定到武当组中
useradd -g wudang zhangwuji

#修改用户组,张无忌这个用户修改到明教组
groupadd mingjiao
usermod -g mingjiao zhagnwuji

#用户、用户组的相关文件

#用户信息配置文件
/etc/passwd 
每行的含义:用户名:口令:用户标识号:组标识号:注释性描述:主目录:登录 shell

 #组配置文件
/etc/group
每行的含义: 组名:口令组标识号:组内用户列表

#密码和登录信息配置文件(加密的)
/etc/shadow 

#=================组管理和权限管理================================

#分配sudo权限给用户
sudo的工作过程如下：

1，当用户执行sudo时，系统会主动寻找/etc/sudoers文件，判断该用户是否有执行sudo的权限
2，确认用户具有可执行sudo的权限后，让用户输入用户自己的密码确认
3，若密码输入成功，则开始执行sudo后续的命令
4，root执行sudo时不需要输入密码(eudoers文件中有配置root ALL=(ALL) ALL这样一条规则)
5，若欲切换的身份与执行者的身份相同，也不需要输入密码

visudo使用vi打开/etc/sudoers文件，但是在保存退出时，visudo会检查内部语法，避免用户输入错误信息
visudo需要root权限
找到#%wheel ALL=(ALL) ALL,在其下方添加如下一行,对用户组dev授予sudo权限

%dev ALL=ALL(ALL) ALL

```





### 搜索

```bash
find[搜索范围][选项]
#根据名称,查找/home 文件夹下边的 a.txt 文件
find /home -name a.txt
find /home -name mysql.*
#根据文件的拥有者 来查找
find /home -user zhangwuji
#查找 linux 下大于 10M 的文件
find /home -size +20M
```

```bash
#head 输入文件开头部分的内容
head -n 5 #显示文件头五行的内容,不加选项,默认显示前 10 行

#tail 默认显示文件结束部分的前10 行
tai -n 10
tail -f #实施追踪该文档的所有更新,重点
```

```bash
#试试监控一个文件,如果该文件更新则追加日期
1 、 当一个终端 ls -l >>mydata.txt
2 、 此终端的 tail -f mydata.txt 会变化
```



### 压缩

```bash
#当我们用 gzip 对文件进行压缩后,不会保留之前的文件
gzip hello.txt
gunzip 

#zip 压缩文件 unzip 解压文件
#常用选项 
 -r :递归压缩,即压缩目录
# 指定解压到的存放目录
unzip -d 

tar 打包指令,最后打包的文件是 xxx.tar.gz
-z 打包同时压缩
-c 产生.tar 打包文件
-v 显示详细信息
-x 解包.tar 文件
-f 指定要素后的文件名

#压缩多个文件 将/home/1.txt 和/home/2.txt 文件 有所成 a.tar.gz
tar -cvzf a.tar.gz 1.txt 2.txt

#将 mysql.tar.gz 解压到/opt/www 下
tar -xvzf mysql.tar.gz -C /opt/www

```





### vimium

```

单个页面的操作

j 向下滚动页面 (scrollDown)
k 向上滚动页面 (scrollUp)
d 向下滚动半屏页面 (scrollPageDown)
u 向上滚动半屏页面 (scrollPageUp)
gg 向上滚动到页面最上方 (scrollToTop)
G 向下滚动到页面最底部 (scrollToBottom)
yy 赋值当前url到剪切板 Copy the current URL to the clipboard
gi 聚焦页面第一个文本输入框 Focus the first text input on the page (focusInput)
f Open a link in the current tab (LinkHints.activateMode)
F Open a link in a new tab

多标签页操作

yt 重新打开一个当前标签页 Duplicate current tab (duplicateTab)
W  将当前tab移动到新窗口  (moveTabToNewWindow)
T   通过打开的tab进行搜索 Search through your open tabs
```

## hombrew

```shell
brew ls tmux #查看软件安装的位置
```

## ideaVim

```SHELL
:actionlist #列出idea 所有的动作映射
```

```shell
gs        #前往类的是实现
<leader>s #查看类的方法列表
<leader>` #打开文件浏览器   
<leader>h #文件浏览器的显示和隐藏
<leader>u #查看此方法在别的类中的所有调用
<leader>t #打开重构 pop
<leader>n #加断点
<leader>i #maven install
<leader>p #最近项目
<leader>g #打开构造 pop
```



## tmux

```shell
#创建回话
tmux new -s <sessionName>

#退出
exit 或者 Ctrl+d

#打开 session列表
ctrl+b s 或者 tmux ls
#重命名回话
ctrl+b $
#离开回话,后台运行
ctrl+b d 或者 tmux detach
#进入 session
tmux attach -t <sessionName>
#删除所有session
Ctrl+b :kill-server
#删除session
Ctrl+b :kill-session
#删除指定session
tmux kill-session -t $session_name
#列出ohmytmux 所有的快捷键
ctrl+b ?
#热键
ohmytmux 默认设置了热键 ctrl+f 和 ctrl+a

#创建窗口
ctrl+b c
#切换到 2号窗口
ctrl+b 2
#重命名窗口
ctrl+b ,
#关闭窗口
ctrl+b &

#水平切分
ctrl+b %  
#垂直切分
ctrl+b "  
#关闭窗格
ctrl+b x`
```



使用以下命令安装 tmux，linux与mac都可以使用[brew (opens new window)](http://houdunren.gitee.io/note/linux/2 常用工具.html#brew)进行安装

```shell
# Mac
$ brew install tmux

# Ubuntu 或 Debian
$ sudo apt-get install tmux

# CentOS 或 Fedor可以使用yum/dnf/brew等方式安装，brew版本更高些
$ yum install tmux
```

### 字体图标

执行以下指令安装字体图标到系统中，有些风格需要图标时就可以正常显示了

```text
cd
git clone https://github.com/powerline/fonts.git --depth=1
cd fonts
./install.sh
cd ..
rm -rf fonts
```

使用的是 item2 需要进行以下设置

![image-20200109152424996](https://gitee.com/ibepo/ogcip/raw/master/20220127130350.png)

### [#](https://doc.houdunren.com/soft/10 tmux.html#安装风格)安装风格

下面介绍两款风格包

**tmux-onedark-theme**

大叔喜欢颜色不那么鲜艳的 [tmux-onedark-theme (opens new window)](https://github.com/odedlaz/tmux-onedark-theme)风格

![image-20200109160737009](https://gitee.com/ibepo/ogcip/raw/master/20220127110837.png)

安装方式如下

1. Clone 项目代码

   ```text
   git clone https://github.com/odedlaz/tmux-onedark-theme
   ```

2. 删除原~/.tmux.conf文件（注意不是删除内容，因为存在的.tmux.conf可能是软链接），然后新建配置文件 `~/.tmux.conf` 添加以下内容，如果想显示完整日期就将前2~4行注释掉。

   ```text
   run-shell ~/tmux-onedark-theme/tmux-onedark-theme.tmux
   set -g @onedark_widgets " "
   set -g @onedark_time_format "%I:%M "
   set -g @onedark_date_format "%m/%d"
   set-option -g status-position bottom
   ```

3. 加载配置

   ```text
   tmux source-file ~/.tmux.conf
   ```

**gpakosz/.tmux**

tmux 的风格包很多，下面介绍 [gpakosz/.tmux (opens new window)](https://github.com/gpakosz/.tmux)风格包的安装方法

![Screenshot](https://gitee.com/ibepo/ogcip/raw/master/20220127110843.gif)

通过执行以下命令安装风格，之后通过修改 `～/.tmux.conf.local` 来定义界面

```text
cd
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .
```

重新加载 tmux 配置项以使风格生效

```text
tmux source-file ~/.tmux.conf
```

### 会话管理

会话是最大的单位，包含窗口与窗格

| 命令                | 说明                                     | 快捷键   |
| ------------------- | ---------------------------------------- | -------- |
| tmux new -s         | 创建会话                                 |          |
| tmux detach         | 退出当前会话，会话进程仍然在后台运行     | Ctrl+b d |
| tmux ls             | 查看当前所有的 会话                      | Ctrl+b s |
| tmux attach -t      | 重新接入某个已存在的会话                 |          |
| tmux kill-session   | 杀死某个会话                             |          |
| tmux switch -t      | 切换会话                                 |          |
| tmux rename-session | 重新命名会话                             | Ctrl+b $ |
| tmux at -d          | 重绘窗口，在不同屏幕上保持窗口为最小尺寸 |          |

tmux默认会同步会话到所有窗口，并使用尺寸最小窗口的尺寸，这会造成大窗口有小点。

![image-20200123210737845](https://gitee.com/ibepo/ogcip/raw/master/20220127110850.png)

使用以下方式来解决

```shell
tmux at -d #简写为 tmux a -d
```

### 窗口管理

窗口属于会话，窗口包含多个窗格

| 命令                  | 说明           | 快捷键   |
| --------------------- | -------------- | -------- |
| tmux new-window -n    | 创建新窗口     | Ctrl+b c |
| tmux select-window -t | 切换窗口       |          |
| tmux rename-window    | 重命名当前窗口 | Ctrl+b , |

切换窗口快捷键

| 快捷键   | 说明                                              |
| -------- | ------------------------------------------------- |
| Ctrl+b p | 切换到上一个窗口（按照状态栏上的顺序）            |
| Ctrl+b n | 切换到下一个窗口                                  |
| Ctrl+b   | 切换到指定编号的窗口，number 是状态栏上的窗口编号 |
| Ctrl+b w | 从列表中选择窗口                                  |
| ctrl+b & | 关闭当前窗口                                      |
| ctrl+b x | 删除窗口                                          |

### [#](https://doc.houdunren.com/soft/10 tmux.html#窗格管理)窗格管理

**拆分窗格**

| 命令                 | 说明             |
| -------------------- | ---------------- |
| tmux split-window -h | 划分左右两个窗格 |
| tmux split-window    | 划分上下两个窗格 |

**移动窗格**

| 命令                | 说明               |
| ------------------- | ------------------ |
| tmux select-pane -U | 光标切换到上方窗格 |
| tmux select-pane -D | 光标切换到下方窗格 |
| tmux select-pane -L | 光标切换到左边窗格 |
| tmux select-pane -R | 光标切换到右边窗格 |
| tmux swap-pane -U   | 当前窗格上移       |
| tmux swap-pane -D   | 当前窗格下移       |

**窗格快捷键**

| 快捷键            | 说明                                       |
| ----------------- | ------------------------------------------ |
| Ctrl+b %          | 划分左右两个窗格                           |
| Ctrl+b "          | 划分上下两个窗格                           |
| Ctrl+b ;          | 切换到上一个窗格                           |
| Ctrl+b o          | 光标切换到下一个窗格                       |
| Ctrl+b {          | 当前窗格左移                               |
| Ctrl+b }          | 当前窗格右移                               |
| Ctrl+b Ctrl+o     | 当前窗格上移                               |
| Ctrl+b Alt+o      | 当前窗格下移                               |
| Ctrl+b x          | 关闭当前窗格                               |
| Ctrl+b !          | 将当前窗格拆分为一个独立窗口               |
| Ctrl+b z          | 当前窗格全屏显示，再使用一次会变回原来大小 |
| Ctrl+b q          | 显示窗格编号                               |
| Ctrl+b Alt+方向键 | 调整窗格大小                               |

### [#](https://doc.houdunren.com/soft/10 tmux.html#保存会话)保存会话

默认情况下当重起系统后，需要重新定义tmux窗口，这很不是方便。

### [#](https://doc.houdunren.com/soft/10 tmux.html#安装插件)安装插件

我们需要安装 [tmp (opens new window)](https://github.com/tmux-plugins/tpm)与[tmux-resurrect (opens new window)](https://github.com/tmux-plugins/tmux-resurrect)插件

```text
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
git clone https://github.com/tmux-plugins/tmux-resurrect ~/.tmux/plugins/resurrect
```

修改配置文件 `~/.tmux.conf`添加以下内容

```text
# 自动保存会话
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'
set -g @continuum-save-interval '15'
set -g @continuum-restore 'on'
set -g @resurrect-capture-pane-contents 'on'
run '~/.tmux/plugins/tpm/tpm'

run-shell ~/.tmux/plugins/resurrect/resurrect.tmux
```

返回终端重新加载配置项

```text
tmux source ~/.tmux.conf
```

然后执行命令安装插件

```text
prefix + I 
```

### [#](https://doc.houdunren.com/soft/10 tmux.html#保存会话-2)保存会话

插件安装后就可以管理会话了，下例中的 prefix就是.tmux.conf文件中定义的prefix

保存会话

```text
prefix + Ctrl-s
```

恢复会话

```text
prefix + Ctrl-r
```

## [#](https://doc.houdunren.com/soft/10 tmux.html#大叔配置)大叔配置

下面是我配置好的.tmux.conf文件内容，但要注意里面有插件的配置，所以需要保证已经安装了相关插件。

```shell
run-shell ~/tmux-onedark-theme/tmux-onedark-theme.tmux

set -g @onedark_widgets "houdunren.com < B站/抖音@后盾人 #(ip)"
set -g @onedark_time_format "%I:%M %p"
set -g @onedark_date_format "%Y/%m/%d"
set-option -g default-terminal "screen-256color"
set -g default-terminal "screen-256color"

# 解决neovim中esc响应慢
set -s escape-time 0
set-option -g status-position bottom

# 自动保存会话
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'
set -g @continuum-save-interval '15'
set -g @continuum-restore 'on'
set -g @resurrect-capture-pane-contents 'on'
run '~/.tmux/plugins/tpm/tpm'

run-shell ~/.tmux/plugins/resurrect/resurrect.tmux

# 解除默认前缀
unbind C-b
# 设置自定义前缀
set -g prefix C-f
# 采用vim的操作方式
setw -g mode-keys vi
# 窗口序号从1开始计数
set -g base-index 1
# 开启鼠标模式
set-option -g mouse on

# 通过前缀+KJHL快速切换pane
#up
bind-key k select-pane -U
#down
bind-key j select-pane -D
#left
bind-key h select-pane -L
#right
bind-key l select-pane -R
```

[tmux-plugins/tpm: Tmux Plugin Manager (github.com)](https://github.com/tmux-plugins/tpm)





## 软连接

### linux

```shell
ln -s  /home/ubuntu/dotfiels/.oh-my-zsh ~/.oh-my-zsh
```

### macox

```shell
ln -s /Users/ibepo/dotfiles/.oh-my-zsh ~/.oh-my-zsh
```



## vim

![image-20211122155323410](https://gitee.com/ibepo/ogcip/raw/master/20211122155324.png)

```
ctrl+u 删除命令行开始至光标处
ctrl+k 删除光标处至命令行结尾
ctrl+a 光标移动到最前面
ctrl+e 光标移动到最后面
```

```shell
vim 全选，全部复制，全部删除
全选（高亮显示）：按esc后，然后ggvG或者ggVG
全部复制：按esc后，然后ggyG
全部删除：按esc后，然后dG
解析：
gg：是让光标移到首行，在vim才有效，vi中无效 
v ： 是进入Visual(可视）模式 \
G ：光标移到最后一行 
选中内容以后就可以其他的操作了，比如： 
d  删除选中内容 
y  复制选中内容到0号寄存器 
+y  复制选中内容到＋寄存器，也就是系统的剪贴板，供其他程序用 
```

```shelll

 ln -s /home/ubuntu/dotfiles/nvim/  ~/.config/nvim
```



### vimrc

[VIM学习笔记 配置文件(vimrc) - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/154383194)



### 高频操作

- `:w` 快速保存
- `%`  在花括号或者中括号中间开始和结尾进行跳转
- `<C-[>` 退出 insert 模式，与 `esc` 类似
- `0` 快速移动到行首
- `gg` 快速移动到文件首
- `G` 快速移动至文件尾
- `<c-o>` 移动至最近一次位置
- `<c-i>` 返回当前编辑位置
- `zz` 把光标移动至本屏中间
- `:12` 快速移动至特定行
- `dd` 剪切本行
- `yy` 复制本行
- `yi{` 复制括号中内容
- `=i{` 自动缩进
- `<c-p>` 自动补全
- `"*yy` 复制到系统剪切板
- `*` 快速查找关键字，类似于sublime/vscode 的 `Command + d`
- `:noh` 取消关键字高亮
- `o` 快速进入 insert 模式，并定位到下一行
- `u` 撤销
- `:vs` 垂直分配
- `:sp` 水平分屏
- `<c-w> +hjkl` 窗口间移动

### 移动

#### 字母间跳动

<img src="https://gitee.com/ibepo/ogcip/raw/master/20211122150127.png" alt="image-20211122150126543" style="zoom:50%;" />

- `f{char}`  向后查找相关字母
- `F{char}` 向前查找相关字母
- `;` 重复上次字符查找
- `,` 反向重复上次查找



#### 单词间跳动

<img src="https://gitee.com/ibepo/ogcip/raw/master/20211122104214.png" alt="image-20211122104214437" style="zoom:50%;" />

- `w` 跳到一个单词开头
- `b` 跳到本单词或上一个单词的开头
- `e` 跳到本单词或下一个单词的结尾
- `ge` 跳到上一个单词结尾

#### 行间跳动

<img src="https://gitee.com/ibepo/ogcip/raw/master/20211122133225.png" alt="image-20211122133224492" style="zoom:50%;" />

- `O`     跳到行首
- `^`     跳到从行首开始第一个非空字符
- `$`     跳到行尾
- `gg`   跳到第一行
- `G`     跳到最后一行



### 动作

<img src="https://gitee.com/ibepo/ogcip/raw/master/20211122151017.png" alt="image-20211122151017105" style="zoom:50%;" />

- `i`和`a`的区别就是包不包括`锚点字符`

- `i`和`a`属于`跑马圈地`的`范围缩小器`,要配合上相应的行为,

  `c`修改,删除之前的并进入编辑模式

  `d`删除,不仅如此编辑模式 

​       `y`复制

- `ciw`  **change inner word**  选中当前的单词,并删除它,进入修改模式

- `dw`     可以从光标处删除至一个单词的末尾

-  `d$` 从当前光标删除到行末

- `diw`   delect inner word

- `yiw`   copy innner word

- `dib`   删除括号内内容

- `ci[`   删除数组内内容

- `ci` `  删除模板字符串的内容

- `2dd` 删除两行

- `2cc`删除并编辑两行

- `2yy`复制两行

- ```shell
  #vim is awesome
  ```

  `dfa`  删除`vim is a`

  `d^`    从此处删除到开头

  `d$`   从此处删除到结尾

- `die` 删除全部

- `yie` 复制全部

### 日常总结

- `zz`  将光标所在位置,移动到屏幕的中央
- `ctrl+u` 前进一页
- `ctrl+d` 后退一页
- `normal 模式下` 按`shift+a` 在当前行的行尾,append
- `normal 模式下` 按`shift+i` 在当前行的行首,append
- `shift+z+q`  等同于`:q!` , 强制退出不保存
- `shift+z+z` 等同于`:wq`,退出并保存
- `xp` 交换前后两个字符
- `ddp`交换两行
- `bi`在当前单词的前边插入单词
- `ea`在当前单词的后边插入单词

| 标识符号               | 代表含义                                   |
| ---------------------- | ------------------------------------------ |
| `<Esc>`                | 代表 `Escape` 键                           |
| `<CR>`                 | 代表 `Enter` 键                            |
| `<C-Esc>`              | 代表 `Ctrl-Esc`                            |
| `<S-F1>`               | 表示 `Shift-F1`                            |
| `<D>`                  | 代表 `Command` 键，对于 Mac 用户，可以使用 |
| `<M-key>` 或 `<A-key>` | 代表 `Alt` 键                              |

<img src="https://gitee.com/ibepo/ogcip/raw/master/20211126154057.png" alt="image-20211126154056356" style="zoom:50%;" />



![image-20211215085550135](https://gitee.com/ibepo/ogcip/raw/master/20211215085550.png)



Plug-vim 的中国地址镜像

```shell
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
https://gitee.com/ibepo/dotfiles/raw/master/.config/nvim/autoload/plug.vim
```



## 插件

```shell
Plug 'mg979/vim-visual-multi'
```

- `S-Right`,用 shift+鼠标右键选择`chart`,通过`n`向下移动,通过`N`向上移动, 和`'lfv89/vim-interestingwords`功能类似



```shell
Plug 'junegunn/vim-peekaboo'
```

- `"`调出寄存器历史记录



```shell
CocConfig coc-explorer
```

- `tt` toggle coc-explorer
- `<leader>e` 打开explorer



```shell
Plug 'easymotion/vim-easymotion'
let g:EasyMotion_do_mapping = 0        "取消缺省映射
map <leader>f <Plug>(easymotion-bd-f)  "雙向搜尋，搜尋結果不限制在此行
map <leader>s <Plug>(easymotion-s2)    "使用兩個字母最為限制去搜尋
```



```shell
Plug 'justinmk/vim-sneak'
```

- 简化版的] easymotion
- `f+{char}{char}`自动跳转



```shell
Plug 'jiangmiao/auto-pairs'
```

- 使用 auto-pairs 插件，可以在 Vim 插入模式下，输入左大括号后自动补全右大括号
- 在一对括号之间按回车键，将自动分为 3 行并调整缩进和光标位置



```shell
Plug 'airblade/vim-gitgutter'
```

- `<leader>gf` 折叠未修改的代码



```shell
Plug 'tpope/vim-surround'
```

| 键                    | 原内容               | 结果                   |
| --------------------- | -------------------- | ---------------------- |
| 单词加引号ysiw'       | houdunren.com        | 'houdunren.com'        |
| 添加标签 ysiwt h2     | houdunren.com        | houdunren.com          |
| 整行加引号 yss"       | houdunren.com 后盾人 | "houdunren.com 后盾人" |
| 替换为单引号 cs"'     | "houdunren"          | 'houdunren.com'        |
| 整行替换 cS'"         | 'houdunren'          | "houdunren"            |
| 替换引号为标签cs"t h2 | 'houdunren'          | houdunren              |
| 删除绰号 ds'          | 'ds'                 | ds                     |
| 删除标签 dst          | houdunren            | Houdunren              |

```shell
Plug 'terryma/vim-smooth-scroll'
```
- `c+j` 平滑向下滚动一屏
- `c+k` 平滑向上滚动一屏

## spacevim

### 安装spacevim

```shell
curl -sLf https://spacevim.org/cn/install.sh | bash
```
## Traefik

### 简介

如果看过我[之前的文章](https://soulteary.com/tags/traefik.html)，那么你会 Traefik 这个软件应该有一些简单的理解，提供类似 Nginx 的负载能力，不同的是可以自动化配置 “`upstream`”，或者说是免配置即开即食的`consul`。官方的定义如下：

> A reverse proxy / load balancer that’s easy, dynamic, automatic, fast, full-featured, open source, production proven, provides metrics, and integrates with every major cluster technologies… No wonder it’s so popular!

简单来说就是，不论你用它来做负载均衡还是反向代理，都是符合它的设计理念的，也提供了大量的功能支撑，让你能够在不同的业务场景下，简单的配置就能实现一定规模的高性能应用。

实际使用的话，不论是配合 `K8S`、`compose`、`Etcd`、`rancher`、`tradition docker`都是可以的。

我个人使用在 `compose` 的场景下，以下配置皆以此为例，其他环境配置大体一致，细节稍有不同，等回头买几台微塔服务器，再折腾个人的 `K8S` 吧（毕竟单节点没什么意思）。

### 适合的场景

- 如果你的机器或者 IP 资源有限，但是你却需要部署多个站点，又期望能够让站点应用保持高度隔离。
- 你已经厌烦传统方案中使用 `haproxy` 或者 `nginx` 对于多个应用的前后端扩容修改要来回修改的麻烦事儿。
- 你不想在服务端挂载 `SSL`，配置加密算法，添加 `gzip` 等本该 `Gateway` 提供的能力，希望让每一层的功能保持简单纯粹。
- 1分钟内拥有有一个轻量高效的本地开发环境。
- 无须重启即可更新配置
- 自动的服务发现与负载均衡
- 与 `docker` 的完美集成，基于 `container label` 的配置

[(HTTPS 深入浅出 - 什么是 SNI？](https://blog.csdn.net/firefile/article/details/80532161)

### 配置

![image-20211112102052045](https://gitee.com/ibepo/ogcip/raw/master/20211112102052.png)



`traefik` 一般需要一个配置文件来管理路由，服务，证书等。我们可以通过 `docker` 启动 `traefik` 时来挂载配置文件

它的配置分为 `static`部分和 `dynamic`两部分,

其中`entrypoints` `provider` `connection`  `infromation`可通过`static `配置也可以通过` docker-compose.yml`的 `label`设置

另外`routers`、 `services`、 `middlewares` `certificates`通过`dynamic`动态配置

关于静态配置一些使用的规则

- 发现路由的规则

​        以上的配置,表示如果没有`Rule`,将默认通过`<Name>.ibepo.cn`的形式发现路由

```toml
  [providers.docker]
  endpoint = "unix:///var/run/docker.sock"
  defaultRule = "Host(`{{ normalize .Name }}.ibepo.cn`)"
```

- 日志

  日志极为重要，当某个路由配置不成功，或者 https 配置失败时，可以通过日志文件找到蛛丝马迹

  ```toml
  # Writing Logs to a File, in JSON
  [log]
    filePath = "/path/to/log-file.log"
    format = "json"
  ```

- 请求日志

```toml
[accessLog]
filePath = "./traefik-access.json"
format = "json"
```

请求日志文件配置为 `json` 格式，结构化数据方便调试

- entryPoint

```toml
[entryPoints]
  [entryPoints.web]
    address = ":80"

  [entryPoints.web-secure]
    address = ":443"
```

考虑到隐私以及安全，不对外公开的服务可以配置 `Basic Auth`，`Digest Auth` 或者 `WhiteList`，或者直接搭建 VPN，在内网内进行访问。至于 `Basic Auth` 等，可以参考 [traefik middlewares](https://docs.traefik.io/middlewares/overview/)

- prometheus metrics

```toml
[metrics.prometheus]
  buckets = [0.1,0.3,1.2,5.0]
  entryPoint = "metrics"
```

[Prometheus (opens new window)](https://prometheus.io/)作为时序数据库，可以用来监控 traefik 的日志，支持更加灵活的查询，报警以及可视化。traefik 默认设置 prometheus 作为日志收集工具。另外可以使用 `grafana` 做为 `prometheus` 的可视化工具。

### Docker Provider，Router and Service

![image-20211112103815283](https://gitee.com/ibepo/ogcip/raw/master/20211112103815.png)

- `Providers` 服务提供者，如 docker，如一个 http service
- `Routers` 分析请求的 `Host`，`Header` 或者 `Path`
- `Services` 选择合适的 `Provider` (负载均衡等)

我们使用 `Docker` 作为 `Provider`，而 `Router` 与 `Service` 可以通过 `container labels` 来进行配置，我们一般使用 `docker-compose.yaml` 中的 `labels` 来配置

我们可以通过 `traefik.http.routers.<container-name>.rule` 来配置路由规则，类似与 `nginx` 中的 `location`

```yml
labels:
  - "traefik.http.routers.blog.rule=Host(`traefik.io`) || (Host(`containo.us`) && Path(`/traefik`))"
```

### 负载均衡

如果要为 `docker provider` 进行负载均衡怎么办?

只需要使用 `docker-compose up --scale` 对容器横向扩容即可完成

```shell
$ docker-compose up --scale whoami=3
WARNING: The scale command is deprecated. Use the up command with the --scale flag instead.
Starting whoami_whoami_1 ... done
Creating whoami_whoami_2 ... done
Creating whoami_whoami_3 ... done
```

在 `traefik dashboard` 中查看该 `service`时，已负载到三个容器



### 灰色发布



### Traefik Dashboard

`traefik` 默认有一个 `dashboard`，通过 `:8080` 端口暴露出去。我们可以在浏览器中直接通过 `<IP>:8080` 访问，但是

1. 使用 `IP` 地址肯定不是特别方便，此时我们可以配置 `Host`
2. 在公网环境下访问有安全性问题，此时可以配置 `basicAuth`，`digestAuth`，`IpWhiteList` 或者 `openVPN` 等中间件

再次更改 `traefik` 的 `docker-compose.yaml` 文件如下：

```
version: '3'

services:
  reverse-proxy:
    image: traefik:v2.2
    restart: always
    ports:
      - "80:80"
      - "8080:8080"
    volumes:
      - ./traefik.toml:/etc/traefik/traefik.toml
      - /var/run/docker.sock:/var/run/docker.sock
    container_name: traefik
    labels:
      - "traefik.http.routers.api.rule=Host(`traefik.ibepo.local`)"
      - "traefik.http.routers.api.service=api@internal"
```

此时可以通过 `traefik.ibepo.local` 来访问 `dashboard`

### https 证书

`https` 已经成为一个现代网站的标配，以至于当一个网站没有 `https` 时，某些浏览器都会把它标识为不安全。而除了安全方面，`https` 对网站的SEO也影响很多，而对于某些新型的浏览器 API，也只有在 `https` 下才能使用。不管怎么说，`https` 也成为一个网站的刚需。

而当你使用了 `traefik` 作为反向代理时，你可以配置 `ACME` 自动为域名提供证书，只需几行即可解决问题。免费的证书，当然是通过 `Let's Encrypt` 来解决。

#### ACME 配置

通过它可以很方便地自动签发证书并且自动续期，我们在 `traefik.toml` 中进行相关配置

```toml
[certificatesResolvers.le.acme]
  email = "xianger94@qq.com"
  storage = "acme.json"

  [certificatesResolvers.le.acme.tlsChallenge]
```

其中，`storage` 指存放证书的位置

#### 服务配置

如果你需要为你的服务提供 https 流量，只需要添加两行代码

```yaml
labels:
  - traefik.http.routers.whoami.tls=true
  - traefik.http.routers.whoami.tls.certresolver=le
```

我们依然使用 `whoami` 做测试，`docker-compose.yaml` 文件内容如下

```yaml
version: '3'

services:
  whoami:
    image: containous/whoami
    labels:
      - traefik.http.routers.whoami.rule=Host(`whoami.shanyue.tech`)
      - traefik.http.routers.whoami.tls=true
      - traefik.http.routers.whoami.tls.certresolver=le
    # environments:
    #   TMUX
    
networks:
  default:
    external:
      name: traefik_default
```

服务启动后，使用 `curl` 测试服务是否正常工作，我们可以看到 `X-Forwarded-Proto` 为 `https`，配置成功

```bash
$ curl https://whoami.shanyue.tech
Hostname: c9c3cc850e2b
IP: 127.0.0.1
IP: 172.18.0.2
RemoteAddr: 172.18.0.3:35320
GET / HTTP/1.1
Host: whoami.shanyue.tech
User-Agent: curl/7.29.0
Accept: */*
Accept-Encoding: gzip
X-Forwarded-For: 59.110.159.217
X-Forwarded-Host: whoami.shanyue.tech
X-Forwarded-Port: 443
X-Forwarded-Proto: https
X-Forwarded-Server: 9d783174aca9
X-Real-Ip: 59.110.159.217
```

### `Path`和`PathPrefix`

```
Path: /sub/             匹配请求的子目录
PathStrip: /sub/        匹配请求的子目录，并把子目录去掉后的请求转发到后端
PathPrefix: /sub/       匹配请求的子目录及包含该子目录的请求
PathPrefixStrip: /sub/  匹配请求的子目录及包含该子目录的请求,并把子目录去掉后的请求转发到后端
```

```Toml
# 使用自定义模板（可选）
# filename = "docker.tmpl"

# 对容器默认进行暴露（默认开启）
#   如果关闭选项，则容器不包含 `traefik.enable=true` 标签，就不会被暴露
exposedbydefault = false

# 使用绑定端口的IP地址取代内部私有网络（默认关闭）
usebindportip = false

# 使用 Swarm Mode （默认关闭）
swarmmode = false
```



## Docker



###  docker 的安装

1. **安装底层工具**

`sudo yum install ‐y yum‐utils device‐mapper‐persistent‐data lvm2`

这是我们安装Docker的底层工具，它就会自动的给我们提示下载，很快下载就完成了。

2.**加入阿里云yum仓库提速docker下载过程**

`sudo yum‐config‐manager ‐‐add‐repo http://mirrors.aliyun.com/docker‐ce/linu `

增加阿里云的Docker下载仓库，默认情况下，Docker官方是从他的国外的服务器下载速度是非常慢的，所以在这里我们是使用yum config manager组件来指定一个新的下载源，指向的是阿里的应用服务器，通过阿里来提高我们Docker的下载速度。

3. **更新一下仓库的源信息**

`sudo yum makecache fast`

**4.** **自动安装下载Docker**

`sudo yum ‐y install docker‐ce`

在这里它就会自动的下载解析，可以看到利用阿里云下载速度是非常快的,我们的Docker便自动安装成功。

5. **启动Docker服务**

`sudo service docker start`

最后咱们来验证一下

**6.** **验证docker是否启动成功**

`docker version`

至此docker-ce版本安装成功 这里我们使用和windows环境完全相同的命令，docker它的安装过程，因为操作系统可能有不同，但是命令每个平台都是一样的，docker version显示我们当前已安装的版本，这里是1809.7，这个版本其实就是对应于我们windows的2.0.3。

7.**Aliyun加速镜像下载**

[镜像加速器 - Docker —— 从入门到实践 (gitbook.io)](https://yeasy.gitbook.io/docker_practice/install/mirror)

[Docker官方中国区加速镜像 | sleele的博客](https://sleele.com/2018/12/29/docker官方中国区加速镜像/)

Centos命令行输入下面的指令加入Aliyun容器镜像，加速镜像的下载https://cr.console.aliyun.com/cn-shanghai/instances/mirrors

![image-20210910115155976](https://gitee.com/ibepo/ogcip/raw/master/20210930122520.png)

```  shell 
sudo mkdir ‐p /etc/docker
sudo tee /etc/docker/daemon.json
{
"registry‐mirrors": ["https://fskvstob.mirror.aliyuncs.com"]
} EOF
sudo systemctl daemon‐reload
sudo systemctl restart docker 
```

```shell
#启动关闭docker
systemctl start docker #通过 systemctl 启动docker
systemctl stop docker # 通过 systemctl 关闭docker
systemctl restart docker#通过systemctl 重启docker
systemctl enable docker #通过systemctl 设置docker开机自启动

#另一个加速镜像
# vi进入docker的镜像编辑界面 输入ustc源地址
vi /etc/docker/daemon.json
{
"registry-mirrors":["https://docker.mirrors.ustc.edu.cn"]
}
#：wq退出
```

###  docker 常用命令

```shell
docker images #查看当前docker 下载的镜像
docker ps #查看当前正在运行的容器
docker ps -a #列出所有容器 包括已停止的
docker inspect 【容器id】 #查看此容器的详细信息

#一个完整的运行命令
docker run \
--name=chatBot \
--volume="/panghu/work/wechatbot/index.js":/bot/index.js \
aibotk/wechat-bot #启动 命名 指定目录挂载数据券


#数据卷
docker volume ls     #查看挂载到 /var/lib/docker/volumes/下的数据券
ls /var/lib/docker/volumes/     #查看此文件夹的内容

#进入容器
docker exec -it [容器 id] /bin/bash #通过命令行 进入容器内部

#网路段
docker network inspect my-bridge #查看加入到网路组的容器
docker network create ‐d bridge my‐bridge #创建虚拟网段

#删除
docker rm - f containid     #强制删除容器
docker rmi -f iamgesid      #强制删除镜像
docker network rm my-bridge #强制删除网络组

#docker 日志
docker logs -ft --tail=10 --since="2016-07-01" chatBot 
-f : 跟踪日志输出
--since :显示某个开始时间的所有日志
-t : 显示时间戳
--tail :仅列出最新N条容器日志


#显示所有容器的内网 ip
docker inspect --format='{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq)    

#后台启动容器
docker run -d centos
#这样 docker 容器使用后台运行,就必须要有一个前台进程,docker 发现没有应用,就会自动停止
#nginx 容器启动后,发现自己没有提供服务,就立刻停止了
docker run -d -it centos #这样就行了

docker ps #列出所有容器
docker port #查看容器端口映射
docker stats #查看资源占用


#docker 内部shell 安装工具 找不着仓库的处理办法
$apt-get update
```

网络相关

```shell
#创建网桥
$ docker network create ‐d bridge my‐bridge
# 查看网段
$ docker network ls
```

#### 查看容器状态

```shell
$ docker stats
```



### docker 部署容器

<img src="https://gitee.com/ibepo/ogcip/raw/master/20210930122525.png" alt="image-20210910121026566" style="zoom:55%;" />




####  docker 部署 [Portainer]

```shell

#拉去镜像
docker pull portainer/portainer

#docker 运行
docker run -p 9000:9000 -p 8000:8000 --name portainer \
--restart=always \
-v /var/run/docker.sock:/var/run/docker.sock \
-v /mydata/portainer/data:/data \
-d portainer/portainer

#访问 ip:9000
id:root1234  pwd:root1234
```


#### docker 部署 [ MySQL 5.7] 

  [docker 中 mysql 的部署和启动](https://juejin.cn/post/6844904095950569480#heading-1)

[docker 中开启 binglog](https://www.cnblogs.com/cpw6/p/11597553.html)

[docker搭建mysql 主从复制](https://mp.weixin.qq.com/s/sV1Ox9k7Lu1mykwjQ1Y8Ww)

```shell
docker run \
‐p 3306:3306 \ 
‐‐network my‐bridge \ #--network my-bridge 代表将db容器加入到my-bridge虚拟网段,这样才可以和其他容器通信 
‐‐name db \
‐v /usr/local/bsbdj/sql:/docker‐entrypoint‐initdb.d \
‐v /usr/local/bsbdj/data:/var/lib/mysql \
-v /etc/mysql:/etc/mysql  #本地配置路径,之后可以放入 my.cnf,开启 binglog 和做一些配置
‐e MYSQL_ROOT_PASSWORD=root \ 
‐d mysql:5.7
```

- docker run ...mysql 5.7 代表创建并自动运行mysql 5.7 容器，如果宿主机没有 mysql 5.7镜像，则自动会从dockerhub进行下载。 
- --name db是容器的名字 
- -p 3306:3306 代表将容器内部MySQL5.7 映射到宿主机的3306端口，这样才可以从外界进行访问 
- --network my-bridge 代表将db容器加入到my-bridge虚拟网段,这样才可以 和其他容器通信 
- -v /usr/local/bsbdj/sql ... 代表将宿主机的sql目录挂载到容器内的docker- entrypoint-initdb.d，根据dockerhub 的描述，放入docker-entrypoint-initdb.d 目录下的SQL文件会在MySQL容器创建后自动执行，完成数据初始化任务。 
- -v /usr/local/bsbdj/data ...同样是挂载，因为容器很容易创建或迁移，如果将 MySQL数据文件保存在容器内部，容器销毁数据就会丢失，因此同样使用-v命令将 容器内产生的数据文件挂载到宿主机的data目录下，这样即使容器销毁数据也不会丢 失。
- -e MYSQL_ROOT_PASSWORD=root ,mysql容器要求的环境参数，说明创建容器时默认数据库root密码为root. 
- -d 代表采用后台模式运行，不加-d则采用前台独占方式运行

```shell
#这个脚本以问答交互的方式执行，按提示操作就可以了。注意修改 root 账号密码的那一步，设置一个自己能记住的密##码。本地开发用的，不用搞太复杂。
mysql_secure_installation

```



#### docker 部署 [Minio]

[🔗docker中minio解决浏览器无法访问的问题](https://blog.csdn.net/qq_38132995/article/details/118812013)

```
#docker 拉去最新镜像
docker pull minio/minio
# 进入minio 命令行
docker run -it --entrypoint=/bin/sh minio/mc
# 正确的启动方式,之前测试的浏览器会打不开,因为你 console 端口会动态变化,这直接给它写死 就没问题了
docker run -p 9090:9000 --name minio   -v /mydata/minio/data:/data   -v /mydata/minio/config:/root/.minio   -d minio/minio server /data --console-address ":9000" --address ":9090"
```

#### docker 部署 [Elasticsearch]

```
docker pull docker.io/elasticsearch:7.4.2

docker images

#-d：后台启动
#--name：容器名称
#-p：端口映射
#-e：设置环境变量
#discovery.type=single-node：单机运行
#b0e9f9f047e6：镜像id
#如果启动不了，可以加大内存设置：-e ES_JAVA_OPTS="-Xms512m -Xmx512m"
docker run
-d
--name es
-p 9200:9200
-p 9300:9300
-e "http.cors.allow-  origin=http://39.102.138.62:8085" -e ES_JAVA_OPTS="-Xms412m -Xmx412m" -e "discovery.type=single-node"
b1179d41a7b4
 
docker exec -it es /bin/bash
```

#### docker部署 [elasticvue]

```
 docker run --name esvue  -p 7010:8080 -d cars10/elasticvue 
 docker exec -it esvue /bin/bash
```

#### docker 部署 [ build 镜像]

```shell
#dockfile
FROM openjdk:11
ADD ./app /usr/local/bsbdj
WORKDIR /usr/local/bsbdj 
CMD ["java","‐jar", "bsbdj.jar"]
```



```shell
docker run \ 
‐‐name app1 \
‐‐network my‐bridge \ 
‐p 8080:8080 \ 
‐d itlaoqi/bsbdj:1.0

docker run \
‐‐name app2 \
‐‐network my‐bridge \ 
‐p 8081:8080 \ 
‐d itlaoqi/bsbdj:1.0

docker run \
‐‐name app3 \
‐‐network my‐bridge \
‐p 8082:8080 \ 
‐d itlaoqi/bsbdj:1.0
```

#### docker 部署 Ngnix

```shell
docker run \
‐‐name nginx \
‐v /usr/local/bsbdj/nginx/nginx.conf:/etc/nginx/nginx.conf \ #这里的 ngnix 配置需要注意下
‐‐network my‐bridge \ 
‐p 80:80 \
‐d nginx
```

#### 一键发布脚本sh

(ngnix+三个后端服务一键式部署)

```shell
docker network create ‐d bridge my‐bridge

docker run \ 
‐p 3306:3306 \
‐‐network my‐bridge \
‐‐name db \
‐v /usr/local/bsbdj/sql:/docker‐entrypoint‐initdb.d \
‐v /usr/local/bsbdj/data:/var/lib/mysql \ 
‐e MYSQL_ROOT_PASSWORD=root \ 
‐d mysql:5.7 

#这里是构建镜像
cd /usr/local/bsbdj 
docker build ‐t itlaoqi/bsbdj:1.0 .

docker run \ 
‐‐name app1 \ 
‐‐network my‐bridge \
‐p 8080:8080 \ 
‐d itlaoqi/bsbdj:1.0 

docker run ‐‐name app2 \
‐‐network my‐bridge \ 
‐p 8081:8080 \
‐d itlaoqi/bsbdj:1.0 

docker run \ 
‐‐name app3 \ 
‐‐network my‐bridge \ 
‐p 8082:8080 \ 
‐d itlaoqi/bsbdj:1.0 

docker run ‐‐name nginx \
‐v /usr/local/bsbdj/nginx/nginx.conf:/etc/nginx/nginx.conf \
‐‐network my‐bridge \
‐p 80:80 \
‐d nginx
```



### docker 八股文

#### docker stack

```yaml
#举例说明 docker stack 的用法
#YAML
version: '3.1'
 
services:
 
  wordpress:
    image: wordpress
    restart: always
    ports:
      - 8080:80
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: exampleuser
      WORDPRESS_DB_PASSWORD: examplepass
      WORDPRESS_DB_NAME: exampledb
    volumes:
      - wordpress:/var/www/html
 
  db:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_DATABASE: exampledb
      MYSQL_USER: exampleuser
      MYSQL_PASSWORD: examplepass
      MYSQL_RANDOM_ROOT_PASSWORD: '1'
    volumes:
      - db:/var/lib/mysql
 
volumes:
  wordpress:
  db:
```

```bash
#docker_cli
docker stack deploy -c stack.yml wordpress #-c 指定yml文件，deploy可以换成up
```



#### docker.sock

[op-note/docker.md at master · shfshanyue/op-note (github.com)](https://github.com/shfshanyue/op-note/blob/master/docker.md)

[docker，containerd，runc，docker-shim - 简书 (jianshu.com)](https://www.jianshu.com/p/52c0f12b0294)

[关于/var/run/docker.sock - Fundebug - 博客园 (cnblogs.com)](https://www.cnblogs.com/fundebug/p/6723464.html)

>运行过Docker Hub的Docker镜像的话，会发现其中一些容器时需要挂载**/var/run/docker.sock**文件。**这个文件是什么呢？为什么有些容器需要使用它？**简单地说，它是**Docker守护进程(Docker daemon)**默认监听的**Unix域套接字(Unix domain socket)**，容器中的进程可以通过它与Docker守护进程进行通信。

![image-20211009094548684](https://gitee.com/ibepo/ogcip/raw/master/20211009094609.png)

#### Portainer

不妨看一下 [Portainer](http://portainer.io/)，它提供了图形化界面用于管理`Docker主机`和`Swarm集群`。如果使用`Portainer`管理本地Docker主机的话，需要绑定`/var/run/docker.sock`.

访问9000端口可以查看图形化界面，可以管理容器(container)，镜像(image)，数据卷(volume)...

Portainer通过绑定的`/var/run/docker.sock`文件与`Docker守护进程(Docker daemon)`通信，执行各种管理操作。

#### Docker守护进程的API

安装Docker之后，Docker守护进程会监听Unix域套接字：/var/run/docker.sock。这一点可以通过Docker daemon的配置选项看出来(在ubuntu上执行cat /etc/default/docker )：

```
-H unix:///var/run/docker.sock
```

注: 监听网络TCP套接字或者其他套接字需要配置相应的**-H**选项。

#### 套接字方式,完成容器全周期

**1. 创建nginx容器**

curl命令通过Unix套接字发送**{“Image”:”nginx”}**到Docker守护进程的**/containers/create**接口，这个将会基于Nginx镜像创建容器并返回容器的ID。

```shell
curl -XPOST --unix-socket /var/run/docker.sock\
-d ‘{“Image”:”nginx”}’ \
-H ‘Content-Type: application/json’ \
http:``//localhost/containers/create
```

输出返回了容器ID:

```shell
{“Id”:”fcb65c6147efb862d5ea3a2ef20e793c52f0fafa3eb04e4292cb4784c5777d65",”Warnings”:``null``}
```

**2. 启动nginx容器**

使用返回的容器ID，调用**/containers/<ID>/start**接口，即可启动新创建的容器。

```shell
curl -XPOST --unix-socket /var/run/docker.sock\
http://localhost/containers/fcb65c6147efb862d5ea3a2ef20e793c52f0fafa3eb04e4292cb4784c5777d65/start
```

注意: 绑定Docker套接字之后，容器的权限会很高，可以控制Docker守护进程。因此，这一点必须谨慎使用，只能用于足够信任的容器。

### docker-compose

#### 命令

docker-compose的完整命令的用法是：`docker-compose [-f <arg>...] [options] [COMMAND] [ARGS...]` 主要分为2段，一是options，二是COMMAND。

常用options有：

- `-f, --file FILE` 指定使用的 Compose 模板文件，默认为 `docker-compose.yml`，可以多次指定。
- `-p, --project-name NAME` 指定项目名称，默认将使用所在目录名称作为项目名。
- `--verbose` 输出更多调试信息。
- `-v, --version` 打印版本并退出。
- `--env-file PATH`设置环境变量

常用COMMAND有：

- build：构建（重新构建）项目中的服务容器。

- config：验证 Compose 文件格式是否正确，若正确则显示配置，若格式错误显示错误原因。

- down：此命令将会停止 `up` 命令所启动的容器，并移除网络

- `docker-compose exec service名称 COMMAND`：进入指定的容器。

- images：列出 Compose 文件中包含的镜像。

- `docker-compose logs <service名称>`：查看服务容器的输出。默认情况下，docker-compose 将对不同的服务输出使用不同的颜色来区分。可以通过 `--no-color` 来关闭颜色。

- scale：通过`service=num` 设置指定服务运行的容器个数。如`docker-compose scale web=3 db=2`

- up：将尝试自动完成包括构建镜像，（重新）创建服务，启动服务，并关联服务相关容器的一系列操作。大部分时候都可以直接通过该命令来启动一个项目。默认情况，

  ```
  docker-compose up
  ```

  启动的容器都在前台，控制台将会同时打印所有容器的输出信息，可以很方便进行调试。当通过

  ```
  Ctrl-C 
  ```

  停止命令时，所有容器将会停止。如果使用

  ```
  docker-compose up -d
  ```

  ，将会在后台启动并运行所有的容器。一般推荐生产环境下使用该选项。

  - `-d` 在后台运行服务容器。
  - `--no-color` 不使用颜色来区分不同的服务的控制台输出。
  - `--no-deps` 不启动服务所链接的容器。
  - `--force-recreate` 强制重新创建容器，不能与 `--no-recreate` 同时使用。
  - `--no-recreate` 如果容器已经存在了，则不重新创建，不能与 `--force-recreate` 同时使用。
  - `--no-build` 不自动构建缺失的服务镜像。
  - `-t, --timeout TIMEOUT` 停止容器时候的超时（默认为 10 秒）。



我们使用 `Compose` 进行应用启动的时候，如果是第一次调试，建议执行：

```bash
docker-compose up
```

因为可以在终端中直接看到应用的实际运行日志，如果出错，可以按下 `CTRL+C` 组合键，中断执行，返回调试。

当你的应用**完全就绪**之后，我们需要长期稳定的运行这个服务的时候，再使用 `Compose` 的时候，则可以添加一个 `-d` 参数，让应用以 daemon 模式执行。

```bash
docker-compose up -d
```

这时，应用会乖乖的静默在后台执行，不会向终端输出任何有价值的信息，如果应用异常，我们需要调试，想看到应用日志该怎么处理呢？执行下面的命令就可以了。

```bash
docker-compose logs -f
```

如果发现应用执行出错，使用 `docker-compose down` 结束应用运行后，调整编排配置文件，重新使用不带参数的的 `docker-compose up` 启动应用，待应用完全就绪后，再添加 `daemon` 参数就可以了。



#### 配置文件

compose默认的模板文件名称为 `docker-compose.yml`，格式为 YAML 格式。注意每个服务都必须通过 `image` 指令指定镜像或 `build` 指令（需要 Dockerfile）等来自动构建生成镜像。其常用的指令有：

- services：后面一行接的是服务名，当compose运行之后 ，其容器名为：`项目名_服务名_1`

- image：后接镜像名，image与bulid只能出现一个

- bulid：后接 `Dockerfile` 所在文件夹的路径。Compose将会利用它自动构建这个镜像，然后使用这个镜像。也可以使用 `context` 指令指定 `Dockerfile` 所在文件夹的路径，再使用 `dockerfile` 指令指定 `Dockerfile` 文件名。

- command：**覆盖**容器启动后默认执行的命令。

- depends_on：先启动容器所依赖的服务名，再来启动自己的。

- environment：设置环境变量。只给定名称的变量会自动获取运行 Compose 主机上对应变量的值，可以用来防止泄露不必要的数据。

- env_file：从文件中获取环境变量，可以为单独的文件路径或列表。如果变量很多，可以将变量写入到一个文件里面，然后使用env_file来配置文件路径。另外：Compose 模板文件支持动态读取主机的系统环境变量和当前目录下的 `.env` 文件中的变量。若当前目录存在 `.env` 文件，执行 `docker-compose` 命令时将从该文件中读取变量。

- ports：暴露端口信息。使用宿主端口：容器端口 `(HOST:CONTAINER)` 格式，或者仅仅指定容器的端口（宿主将会随机选择端口）都可以。

- expose: 只把此端口暴露给 link 到容器的容器, 暴露端口，但不映射到宿主机，只被连接的服务访问。仅可以指定内部端口为参数

- >  子容器依旧全部使用 `expose` 使用私有化的方法导出端口给网关---苏洋

- extra_hosts: - "git.lab.com:127.0.0.1" ,改docker容器中的hosts文件(docker 命令行中是通过参数`--add-host`来添加域名和IP信息到容器的`/etc/hosts`文件中t)

- volumes：数据卷所挂载路径设置。可以设置为宿主机路径(`HOST:CONTAINER`)或者数据卷名称(`VOLUME:CONTAINER`)，并且可以设置访问模式 （`HOST:CONTAINER:ro`）。如果路径为数据卷名称，必须在文件中配置数据卷。

- network external true，如果在`docker-compose`文件中设置`external`为`true`，那么使用`docker-compose up -d`来启动服务时，首先`docker`引擎会查找`external`声明的网络，找到后进行连接。否则会提示错误

- `labels`为容器添加 Docker 元数据（metadata）信息。例如可以为容器添加辅助说明信息。

- ###### networks 配置容器连接的网络。

####  最佳实践 

```yaml
version: '3.8'

services:
  portainer:
    image: portainer/portainer
    container_name: "portainer"
    restart: always
    networks:
       - traefik
    ports:
      - "8000:8000"
      - "9000:9000"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
      - "${PWD}/portainer/data:/data"

  trafik:
    image: traefik:v2.5
    container_name: "trafik"
    restart: always
    networks:
       - traefik
    ports:
      - "80:80"
      - "8080:8080"
      - "443:443"
    volumes:
      # 仅限标准的 Linux 环境
      - "/etc/localtime:/etc/localtime:ro"
      - "/etc/timezone:/etc/timezone:ro"
      - "/var/run/docker.sock:/var/run/docker.sock"
      # - ./trafik/traefik.toml:/etc/traefik.toml:ro
      - "./trafik/config/:/etc/traefik/config/:ro"
      - "./trafik/ssl:/data/ssl"
      - "./trafik/logs:/data/logs"
    command:
      - "--global.sendanonymoususage=false"
      - "--global.checknewversion=false"
      - "--entrypoints.http.address=:80"
      - "--entrypoints.https.address=:443"
      - "--api=true"
      - "--api.insecure=true"
      - "--api.dashboard=true"
      - "--api.debug=false"
      - "--ping=false"
      - "--log.level=warn"
      - "--log.format=common"
      - "--accesslog=false"
      - "--providers.docker=true"
      - "--providers.docker.watch=true"
      - "--providers.docker.exposedbydefault=false"
      - "--providers.docker.endpoint=unix:///var/run/docker.sock"
      - "--providers.docker.swarmMode=false"
      - "--providers.docker.useBindPortIP=false"
      - "--providers.docker.network=traefik"
      - "--providers.file=true"
      - "--providers.file.watch=true"
      - "--providers.file.directory=/etc/traefik/config"
      - "--providers.file.debugloggeneratedtemplate=true" 
    # labels:
    #   对外暴露容器服务
    #   - "traefik.enable=true"
    #   - "traefik.docker.network=traefik"
      # 默认请求转发 https 端口
      # - "traefik.http.routers.traefik-dash-default.middlewares=https-redirect@file"
      # - "traefik.http.routers.traefik-dash-default.entrypoints=http"
      # - "traefik.http.routers.traefik-dash-default.rule=Host(`dashboard.guava.lab.com`)"
      # - "traefik.http.routers.traefik-dash-default.service=dashboard@internal"
      # # 处理网页
      # - "traefik.http.routers.traefik-dash-web.entrypoints=http"
      # - "traefik.http.routers.traefik-dash-web.rule=PathPrefix(`/2`)"
      # - "traefik.http.routers.traefik-dash-web.tls=true"
      # - "traefik.http.routers.traefik-dash-web.service=dashboard@internal"
      # # 处理接口
      # - "traefik.http.routers.traefik-dash-api.entrypoints=http"
      # - "traefik.http.routers.traefik-dash-api.rule=Host(`dashboard.guava.lab.com`) && (PathPrefix(`/api`) || PathPrefix(`/dashboard`))"
      # - "traefik.http.routers.traefik-dash-api.tls=true"
      # - "traefik.http.routers.traefik-dash-api.service=api@internal"
    # healthcheck:
    #   test: ["CMD-SHELL", "wget -q --spider --proxy off localhost:8080/ping || exit 1"]
    #   interval: 3s
    #   retries: 12
    logging:
      driver: "json-file"
      options:
        max-size: "1m"  

  whoami:
    # A container that exposes an API to show its IP address
    image: containous/whoami
    networks:
       - traefik
    labels:
      # 声明公开此容器访问
      - "traefik.enable=true"
      # 服务将响应的域
      - "traefik.http.routers.whoami.rule=PathPrefix(`/w`)"
      # 只允许来自预定义的入口点“http”的请求
      - "traefik.http.routers.whoami.entrypoints=http"
      - "traefik.docker.network=traefik"

  nginx:
    container_name: nginx
    image: nginx:1.21.1-alpine
    restart: always
    # ports:
    #    - "9999:80"
    # expose:
    #    - "80"  #这里如果不写成xx:xx 的形式,会随机给宿主机分配端口号
    volumes:
       - "/usr/share/zoneinfo/Asia/Shanghai:/etc/localtime:ro"
       - ./nginx/html:/usr/share/nginx/html:ro
       # - "./nginx/conf/nginx.conf:/etc/nginx/nginx.conf"
       # - "./nginx/conf.d:/etc/nginx/conf.d"
       - "./nginx/logs:/var/log/nginx"
    networks:
       - traefik
    labels:
       - "traefik.enable=true"
       - "traefik.http.routers.nginx.entrypoints=http"
       - "traefik.docker.network=traefik"
       - "traefik.http.routers.nginx.rule=PathPrefix(`/h5`)"
    logging:
      driver: "json-file"
      options:
        max-size: "1m"
  # mysql:
     # image: mysql:5.7
     #command:
     # - --default_authentication_plugin=mysql_native_password
     # - --character-set-server=utf8mb4
     # - --collation-server=utf8mb4_unicode_ci
     # volumes:
       # - db_data:/var/lib/mysql
     # restart: always
     # environment:
       # MYSQL_ROOT_PASSWORD: 123456
       # MYSQL_DATABASE: wordpress
       # MYSQL_USER: root
       # MYSQL_PASSWORD: root1234
   
networks:
  traefik:
    external: true

```



#### 八股文

[docker入门教程六:容器编排compose | 无名老卒BLOG (wumingx.com)](https://www.wumingx.com/k8s/docker-compose.html)



### lazydocker

```shell
docker run -it --name lazydocker -v /var/run/docker.sock:/var/run/docker.sock -v /usr/local/work/LazyDocker/.config/lazydocker:/.config/jesseduffield/lazydocker lazyteam/lazydocker
```



## MySQL

![image-20211117090608776](https://gitee.com/ibepo/ogcip/raw/master/20211117090609.png)



`TokuDB`在事务机制下,适合`写多读少`的数据备份

`MyISAM`的 sql 语句是串行执行

`innoDB`允许并发读写



### CRUD操作

![image-20211117142654164](https://gitee.com/ibepo/ogcip/raw/master/20211117142654.png)

#### 插入

##### 批量插入忽略错误

当批量插入数据时,因为一条记录的问题,造成全部数据插入失败

```mysql
INSERT INTO t_dept (deptno, dname, loc )
VALUES
	(40,"企划部","北京"),
	(50,"培训部","上海"),
	(60,"后勤部","北京"),
	(70,"技术部","北京"),
	(80,"市场部","北京");
```

此时可以用关键字`IGNORE`忽略错误数据

```mysql
INSERT  IGNORE  INTO t_dept (deptno, dname, loc )
VALUES
	(40,"企划部","北京"),
	(50,"培训部","上海"),
	(60,"后勤部","北京"),
	(70,"技术部","北京"),
	(80,"市场部","北京");
```

##### 实现不存在就插入,存在就更新

````mysql
INSERT  INTO t_emp_ip (id,empno,ip)
VALUES
(5,8004,"192.168.2.555"),
(6,8005,"192.168.2.353"),
(7,8006,"192.168.2.666"),
(8,8007,"192.168.2.363"),
(9,8228,"192.168.2.888")
ON duplicate KEY  UPDATE  ip=values(ip);
````

这个`ON DUPLICATE KEY UPDATE`	有一个需要注意的地方,就是要看`主键约束`和`唯一约束`,如果`主键约束`或者`唯一约束`存在,就会在原来的基础上修改后边`ip=values(ip)`的数据,如果不存在就执行插入

#### 查询

##### 子查询

`mysql`数据库默认关闭了缓存,所以每个子查询都是`相关子查询`

`相关子查询`就是要循环执行多次的子查询

![image-20211117141354669](https://gitee.com/ibepo/ogcip/raw/master/20211117141355.png)

- `Mybatis` 等持久层框架开启了缓存功能,其中一级缓存就会保存`子查询结果`,所以在 mybatis 框架中可以放心的使用`子查询`,**但是前提是要配置`一对一关系`或者`一对多关系`**
- 结论:`sql 控制台`不要使用`子查询`,在`持久层框架`中可以使用`子查询`

##### 如何替代子查询

- 使用 `From` 子查询,代替 `Where `子查询

![image-20211117141934292](https://gitee.com/ibepo/ogcip/raw/master/20211117141934.png)

`FORM`子句在查询中最先被执行,而且只查询一次,所以不是相关子查询

`join on`子句,将`from`连接的表和`join`连接的表产生一个`笛卡尔积`,再用 `on`做筛选

`on`可以理解为在`什么..条件之上`

##### 外连接的 JOIN条件

- 内连接里,查询条件写在 `on`子句或者 `where` 子句,效果是相同的

![image-20211117142535288](https://gitee.com/ibepo/ogcip/raw/master/20211117142535.png)

![image-20211117143643048](https://gitee.com/ibepo/ogcip/raw/master/20211117143643.png)



- 外连接里,查询条件写在 on 子句或者 where 子句中,效果不同

![image-20211117143802581](https://gitee.com/ibepo/ogcip/raw/master/20211117143803.png)

##### 表连接修改

update 语句中的 where 子查询如何改为表连接

- 子查询方式

```mysql
#通过部门表找出叫做"SALES"的 部门code,
#更新员工表中相关 部门code 的 sal 字段
UPDATE t_emp
SET sal = 1000
WHERE deptno = ( SELECT deptno FROM t_dept WHERE dname = 'SALES' )
```

- 表连接方式

  两张表做内连接,可以同时 update 两张表中的数据

```mysql
UPDATE  t_emp e JOIN t_dept d ON e.deptno =d.deptno 
AND d.dname ='SALES'
SET e.sal =1000 , d.dname ='销售部';
```



###  MySQL索引失效,全表扫描

 [ 阿里开发规范解读，小心MySQL索引选择性陷阱](https://www.bilibili.com/video/BV1xv411P7BY?spm_id_from=333.999.0.0)

> 阿里巴巴的约束,页面搜索严禁左模糊或者全模糊,如果需要走搜索引擎解决(索引文件具有 b-tree 的最左前缀匹配特性,如果左边的值未确定,那么无法使用索引)



#####    什么是索引选择性陷阱? 

📌  mysql 是以主键索引和二级索引为主搭建的,当二级索引上命中过多单位,优化器就会认为预期二级索引在回表大面积扫描主键索引,为了节省这个回表的速度,还不如直接全表扫描主键索引,优化器就会不走索引

📌  命中索引值超过总量25%,就有可能造成索引选择性陷阱,导致全表扫描 ps:一切以 explain 执行计划为准

📌 常见案例:
 在业务表中只查询逻辑删=0 的数据(这里有个只是,就是业务表都是逻辑删除,不会真删除,比如订单表,流水表等)
 查询格力集团年薪<5 万的人员工资
 医院护士查询性别为女的工作人员 
 此三者都是命中登录太多的索引,所以还不如与直接走全表扫描

![索引命中和未命中的在执行计划中的体现](https://gitee.com/ibepo/ogcip/raw/master/20210930122632.png)



#####   索引选择性陷阱如何解决?

 📌 通过组合索引提高选择性问题(业务相关)
  select * from 护士表 where 科室="妇科"and 性别="女",在科室和性别上建立组合索引

 📌通过引入引擎索引 es 更换数据源
  例如:将护士表导入 es,es 是基于分片多线程检索,解决查询慢的问题,但是这个会增加复杂度 增加一些新的问题
  增加了额外的引擎,考虑可用性问题
   数据一致性问题 是 mq 数据同步 是canal 做binglog ,如果敏感这个时间需要考虑分布式锁的问题

 📌强制使用索引(有时会有奇效,以实际运行效果为准)
  explain select * from question forece index(answer) where answer='a';

 📌增加缓存,提高全表扫描速度(钞能力)
 innodb_buffer_pool_size=16G
 innodb_buffer_pool_instances=2



#####  MySQL脏读、幻读、不可重复读

> MySQL默认Repeatable Read(RR)-可重复读
> MySQL 5.1以后默认存储引擎就是InnoDB
> 因此MySQL默认RR也能解决幻读问题



 📌   **脏读**是读取到了其他事务中正在处理的未提交数据, 

​         事务 b 在提交事务之前修改为张老三了 ,结果让事务 a 读到了,结果事务 b   回滚了,这时候数据编程了张三

 📌  **不可重复度** 是指**并发更新**时,另一个事务前后查询相同数据时的数据不符合预期

​        事务a第一次 读是 张三 ,这时候事务 b 修改为张老三 ,事务 a 第二次读变成了张老三

📌  **幻读**是并发**新增、删除**这种会产生数量变化的操作

​       事务a第一读三条数据 事务b 写了一条 事务 a 再读变成了四条

📌  事务隔离级别

​		读未提交  读已提交  可重复读(innodb 会处理掉幻读)  串行化



```shell
#获取当前事务隔离界别，默认RR可重复读
SHOW VARIABLES LIKE 'transaction_isolation'; # REPEATABLE-READ

#设置当前会话事务隔离级别为“读未提交”
SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

```

![image-20210910155205141](https://gitee.com/ibepo/ogcip/raw/master/20210930122651.png)

![image-20210910153814448](https://gitee.com/ibepo/ogcip/raw/master/20210930122657.png)

![image-20210910154016692](https://gitee.com/ibepo/ogcip/raw/master/20210930122703.png)



![image-20210910154225837](https://gitee.com/ibepo/ogcip/raw/master/20210930122710.png)

####  MVCC机制

> 在MySQL InnoDB存储引擎下
> RC、RR基于MVCC（多版本并发控制）进行并发事务控制
> MVCC是基于”数据版本”对并发事务进行访问

<img src="https://gitee.com/ibepo/ogcip/raw/master/20210930122715.png" alt="image-20210910160806338"  />

###### undo_log 版本链条

 📌  undolog 就是回滚日志的意思,是 innodb 特有的日志,真实的数据 其实是还有两个字段的

| 字段        |         解释         |
| ----------- | :------------------: |
| trx_id      | 添加的这条数据的事务 |
| db_rool_ptr | 链表头,用于往下遍历  |

<img src="https://gitee.com/ibepo/ogcip/raw/master/20210930122720.png" alt="image-20210910161138670" style="zoom:50%;" />

![image-20210915111506579](https://gitee.com/ibepo/ogcip/raw/master/20210930122725.png)

###### Readview (快照读) 

📌 **快照读**(Readview)就是最普通的 select 查询 SQL 语句

​        SQL 执行时, **MVCC** 提取数据的依据,**且只有这时候用到了 MVCC 控制**

​       **Readview** 是一个数据结构,包含四个字段

| 字段           |                             解释                             |
| -------------- | :----------------------------------------------------------: |
| m_ids          |                    当前活跃的事务编号集合                    |
| min_trx_id     |                       最小活跃事务编号                       |
| max_trx_id     |              预分配事务编号,当前最大事务编号+1               |
| creator_trx_id | ReadView创建者的事务编号,一般是 调用 `select` 命令的那个事务 |

:one: 读已提交(RC)

读已提交在每一次执行快照读(select)时生成 ReadView

![image-20210910164505490](https://gitee.com/ibepo/ogcip/raw/master/20210930122730.png)

这里就要根据生成的 Readview 和 undolog 版本链进行判断对比了 

规则如下:

> undolog 版本链现在遍历得到这一行数据 `temp`和 readview 中的字段进行逻辑判断,如果条件符合就看小一条

① `temp`中的 `trx_id` 是不是 `creator_trx_id`?

成立说明就是自己这个事务修改的,采用这个 temp 作为结果,就是自己这个事务,先执行了 update 在执行了 select

②`temp`中的 `trx_id`<`min_trx_id`?

成立说明数据已经提交了可以访问,说明temp 是在

③`temp`中的 `trx_id`<`max_trx_id`?

![image-20210910164134776](https://gitee.com/ibepo/ogcip/raw/master/20210930122736.png)



###### 当前读

📌 **当前读**是指执行以下语句是进行数据读取的方式

​    `Insert` ` Update` `Delete` 

​    `Select ... for update`

​    `Select ...lock in share mode`

####  bin_log



![image-20210910130843984](https://gitee.com/ibepo/ogcip/raw/master/20210930122743.png)

```
$ vi my.cnf

[mysqld]
server_id=1
log-bin=master
binlog_format=row


# 是否启用binlog日志
show variables like 'log_bin';

# 查看详细的日志配置信息
show global variables like '%log%';

# mysql数据存储目录
show variables like '%dir%';

# 查看binlog的目录
show global variables like "%log_bin%";

# 查看当前服务器使用的biglog文件及大小
show binary logs;

# 查看主服务器使用的biglog文件及大小

# 查看最新一个binlog日志文件名称和Position
show master status;


# 事件查询命令
# IN 'log_name' ：指定要查询的binlog文件名(不指定就是第一个binlog文件)
# FROM pos ：指定从哪个pos起始点开始查起(不指定就是从整个文件首个pos点开始算)
# LIMIT [offset,] ：偏移量(不指定就是0)
# row_count ：查询总条数(不指定就是所有行)
show binlog events [IN 'log_name'] [FROM pos] [LIMIT [offset,] row_count];

# 查看 binlog 内容
show binlog events;

# 查看具体一个binlog文件的内容 （in 后面为binlog的文件名）
show binlog events in 'master.000003';

# 设置binlog文件保存事件，过期删除，单位天
set global expire_log_days=3; 

# 删除当前的binlog文件
reset master; 

# 删除slave的中继日志
reset slave;

# 删除指定日期前的日志索引中binlog日志文件
purge master logs before '2019-03-09 14:00:00';

# 删除指定日志文件
purge master logs to 'master.000003';
```

![image-20210913093935918](https://gitee.com/ibepo/ogcip/raw/master/20210930122749.png)

![image-20210915104742055](https://gitee.com/ibepo/ogcip/raw/master/20210930122753.png)



### PerconaTookit

```shell
#安装依赖包
yum install -y perl-DBI
yum install -y perl-DBD-mysql
yum install -y perl-IO-Socket-SSL
yum install -y perl-Digest-MD5
yum install -y perl-TermReadKey
```

![image-20211116181349491](https://gitee.com/ibepo/ogcip/raw/master/20211116181349.png)

##### 线上实时修改表结构

```shell
docker run -it perconalab/percona-toolkit \
  pt-online-schema-change --host=39.102.138.62 --port=3306 --user=root --password=123456\
  D=cms,t=b_side\
  --alter "MODIFY CODE int(13) NOT NULL DEFAULT '2'"\
  --print --execute
```





## Nginx

### 安装

```bash
/usr/local/nginx/sbin/nginx #启动 nginx
/usr/local/nginx/sbin/nginx -s reload ##重新加载Nginx配置文件，然后以优雅的方式重启Nginx
/usr/local/nginx/sbin/nginx -s stop #强制停止Nginx服务

nginx -t #检测配置文件是否有语法错误，然后退出
```

![image-20210507102156114](https://gitee.com/ibepo/ogcip/raw/master/20210930122800.png)

### 配置

```nginx
#nginx.conf
user  nobody;
worker_processes  1;

events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;


# root是定位到服务器真实目录的一个目录作为初始目录 再加上location中的目录
# 比如 root是/panghu/s,这个作为basepath+location中的/s/,那么访问localhost/s/,就能访问到该目录下
# 一个server中的优先级是正则表达式>深路径>浅路径
    server {
        server_tokens off;
        listen       80;
        server_name  localhost;
        location  / {
            root   /panghu/work/h5;
            index  index.html index.htm;
        }
        location /s/{
                 root   /panghu/work
                 index  index.html index.htm;
        }
                #location ~\.(gif|jpg|png){
                #   # root   /panghu/work/s;
                #}
    }

}
```



```shell
# Nginx配置文件
/etc/nginx/nginx.conf # nginx 主配置文件
/etc/nginx/nginx.conf.default

# 可执行程序文件
/usr/bin/nginx-upgrade
/usr/sbin/nginx

# nginx库文件
/usr/lib/systemd/system/nginx.service # 用于配置系统守护进程
/usr/lib64/nginx/modules # Nginx模块目录

# 帮助文档
/usr/share/doc/nginx-1.16.1
/usr/share/doc/nginx-1.16.1/CHANGES
/usr/share/doc/nginx-1.16.1/README
/usr/share/doc/nginx-1.16.1/README.dynamic
/usr/share/doc/nginx-1.16.1/UPGRADE-NOTES-1.6-to-1.10

# 静态资源目录
/usr/share/nginx/html/404.html
/usr/share/nginx/html/50x.html
/usr/share/nginx/html/index.html

# 存放Nginx日志文件
/var/log/nginx

```

```shell
# 开机配置
systemctl enable nginx # 开机自动启动
systemctl disable nginx # 关闭开机自动启动

# 启动Nginx
systemctl start nginx # 启动Nginx成功后，可以直接访问主机IP，此时会展示Nginx默认页面

# 停止Nginx
systemctl stop nginx

# 重启Nginx
systemctl restart nginx

# 重新加载Nginx
systemctl reload nginx

# 查看 Nginx 运行状态
systemctl status nginx

# 查看Nginx进程
ps -ef | grep nginx

# 杀死Nginx进程
kill -9 pid # 根据上面查看到的Nginx进程号，杀死Nginx进程，-9 表示强制结束进程


```



### 参考

[前端仔也需要懂的nginx内容](https://juejin.cn/post/7007346707767754765)

[Nginx 的 try_files 指令使用实例 ](https://www.hi-linux.com/posts/53878.html)

[前端部署演化史.op-note/deploy-fe.md at master · shfshanyue/op-note (github.com)](https://github.com/shfshanyue/op-note/blob/master/deploy-fe.md)

[使用apt-get安装Nginx - 快乐的凡人721 - 博客园 (cnblogs.com)](https://www.cnblogs.com/luo630/p/9363478.html)

[万字总结，体系化带你全面认识 Nginx ！ - 掘金 (juejin.cn)](https://juejin.cn/post/6942607113118023710)

## Redis

### 安装

#### 原生安装

```shell
#①上传安装包,自己编译
yum install gcc-c++    #gcc编译器
cd /opt                #在/opt 目录下 下载打包压缩的redis
wget http://download.redis.io/releases/redis-2.8.17.tar.gz
cd  /opt/redis-2.8.17.tar.gz
tar xzvf

make #编译
如果编译出现错误，执行命令，清除缓存
make distclean
make 
make insatall
```

```shell
#②yum 添加源,yum 安装到/usr/local/bin
yum install epel-release #安装Fedora的epel仓库
yum install redis
```

![image-20210507102119205](https://gitee.com/ibepo/ogcip/raw/master/20210930122805.png)

### 配置

```toml
redis配置文件样例

# Note on units: when memory size is needed, it is possible to specifiy
# it in the usual form of 1k 5GB 4M and so forth:
#
# 1k => 1000 bytes
# 1kb => 1024 bytes
# 1m => 1000000 bytes
# 1mb => 1024*1024 bytes
# 1g => 1000000000 bytes
# 1gb => 1024*1024*1024 bytes
#
# units are case insensitive so 1GB 1Gb 1gB are all the same.

# Redis默认不是以守护进程的方式运行，可以通过该配置项修改，使用yes启用守护进程
# 启用守护进程后，Redis会把pid写到一个pidfile中，在/var/run/redis.pid
daemonize yes

# 当Redis以守护进程方式运行时，Redis默认会把pid写入/var/run/redis.pid文件，可以通过pidfile指定
pidfile /var/run/redis.pid

# 指定Redis监听端口，默认端口为6379
# 如果指定0端口，表示Redis不监听TCP连接
port 6379

# 绑定的主机地址
# 你可以绑定单一接口，如果没有绑定，所有接口都会监听到来的连接
# bind 127.0.0.1
bind 0.0.0.0

# Specify the path for the unix socket that will be used to listen for
# incoming connections. There is no default, so Redis will not listen
# on a unix socket when not specified.
#
# unixsocket /tmp/redis.sock
# unixsocketperm 755

# 当客户端闲置多长时间后关闭连接，如果指定为0，表示关闭该功能
timeout 0

# 指定日志记录级别，Redis总共支持四个级别：debug、verbose、notice、warning，默认为verbose
# debug (很多信息, 对开发／测试比较有用)
# verbose (many rarely useful info, but not a mess like the debug level)
# notice (moderately verbose, what you want in production probably)
# warning (only very important / critical messages are logged)
loglevel verbose

# 日志记录方式，默认为标准输出，如果配置为redis为守护进程方式运行，而这里又配置为标准输出，则日志将会发送给/dev/null
logfile /logs/redis.log

# To enable logging to the system logger, just set 'syslog-enabled' to yes,
# and optionally update the other syslog parameters to suit your needs.
# syslog-enabled no

# Specify the syslog identity.
# syslog-ident redis

# Specify the syslog facility.  Must be USER or between LOCAL0-LOCAL7.
# syslog-facility local0

# 设置数据库的数量，默认数据库为0，可以使用select <dbid>命令在连接上指定数据库id
# dbid是从0到‘databases’-1的数目
databases 16

################################ SNAPSHOTTING  #################################
# 指定在多长时间内，有多少次更新操作，就将数据同步到数据文件，可以多个条件配合
# Save the DB on disk:
#
#   save <seconds> <changes>
#
#   Will save the DB if both the given number of seconds and the given
#   number of write operations against the DB occurred.
#
#   满足以下条件将会同步数据:
#   900秒（15分钟）内有1个更改
#   300秒（5分钟）内有10个更改
#   60秒内有10000个更改
#   Note: 可以把所有“save”行注释掉，这样就取消同步操作了

save 900 1
save 300 10
save 60 10000

# 指定存储至本地数据库时是否压缩数据，默认为yes，Redis采用LZF压缩，如果为了节省CPU时间，可以关闭该选项，但会导致数据库文件变的巨大
rdbcompression yes

# 指定本地数据库文件名，默认值为dump.rdb
dbfilename dump.rdb

# 工作目录.
# 指定本地数据库存放目录，文件名由上一个dbfilename配置项指定
#
# Also the Append Only File will be created inside this directory.
#
# 注意，这里只能指定一个目录，不能指定文件名
dir ./

################################# REPLICATION #################################

# 主从复制。使用slaveof从 Redis服务器复制一个Redis实例。注意，该配置仅限于当前slave有效
# so for example it is possible to configure the slave to save the DB with a
# different interval, or to listen to another port, and so on.
# 设置当本机为slav服务时，设置master服务的ip地址及端口，在Redis启动时，它会自动从master进行数据同步
# slaveof <masterip> <masterport>


# 当master服务设置了密码保护时，slav服务连接master的密码
# 下文的“requirepass”配置项可以指定密码
# masterauth <master-password>

# When a slave lost the connection with the master, or when the replication
# is still in progress, the slave can act in two different ways:
#
# 1) if slave-serve-stale-data is set to 'yes' (the default) the slave will
#    still reply to client requests, possibly with out of data data, or the
#    data set may just be empty if this is the first synchronization.
#
# 2) if slave-serve-stale data is set to 'no' the slave will reply with
#    an error "SYNC with master in progress" to all the kind of commands
#    but to INFO and SLAVEOF.
#
slave-serve-stale-data yes

# Slaves send PINGs to server in a predefined interval. It's possible to change
# this interval with the repl_ping_slave_period option. The default value is 10
# seconds.
#
# repl-ping-slave-period 10

# The following option sets a timeout for both Bulk transfer I/O timeout and
# master data or ping response timeout. The default value is 60 seconds.
#
# It is important to make sure that this value is greater than the value
# specified for repl-ping-slave-period otherwise a timeout will be detected
# every time there is low traffic between the master and the slave.
#
# repl-timeout 60

################################## SECURITY ###################################

# Warning: since Redis is pretty fast an outside user can try up to
# 150k passwords per second against a good box. This means that you should
# use a very strong password otherwise it will be very easy to break.
# 设置Redis连接密码，如果配置了连接密码，客户端在连接Redis时需要通过auth <password>命令提供密码，默认关闭
requirepass yourpass
# Command renaming.
#
# It is possilbe to change the name of dangerous commands in a shared
# environment. For instance the CONFIG command may be renamed into something
# of hard to guess so that it will be still available for internal-use
# tools but not available for general clients.
#
# Example:
#
# rename-command CONFIG b840fc02d524045429941cc15f59e41cb7be6c52
#
# It is also possilbe to completely kill a command renaming it into
# an empty string:
#
# rename-command CONFIG ""

################################### LIMITS ####################################

# 设置同一时间最大客户端连接数，默认无限制，Redis可以同时打开的客户端连接数为Redis进程可以打开的最大文件描述符数，
# 如果设置maxclients 0，表示不作限制。当客户端连接数到达限制时，Redis会关闭新的连接并向客户端返回max Number of clients reached错误信息
# maxclients 128

# Don't use more memory than the specified amount of bytes.
# When the memory limit is reached Redis will try to remove keys with an
# EXPIRE set. It will try to start freeing keys that are going to expire
# in little time and preserve keys with a longer time to live.
# Redis will also try to remove objects from free lists if possible.
#
# If all this fails, Redis will start to reply with errors to commands
# that will use more memory, like SET, LPUSH, and so on, and will continue
# to reply to most read-only commands like GET.
#
# WARNING: maxmemory can be a good idea mainly if you want to use Redis as a
# 'state' server or cache, not as a real DB. When Redis is used as a real
# database the memory usage will grow over the weeks, it will be obvious if
# it is going to use too much memory in the long run, and you'll have the time
# to upgrade. With maxmemory after the limit is reached you'll start to get
# errors for write operations, and this may even lead to DB inconsistency.
# 指定Redis最大内存限制，Redis在启动时会把数据加载到内存中，达到最大内存后，Redis会先尝试清除已到期或即将到期的Key，
# 当此方法处理后，仍然到达最大内存设置，将无法再进行写入操作，但仍然可以进行读取操作。
# Redis新的vm机制，会把Key存放内存，Value会存放在swap区
# maxmemory <bytes>

# MAXMEMORY POLICY: how Redis will select what to remove when maxmemory
# is reached? You can select among five behavior:
#
# volatile-lru -> remove the key with an expire set using an LRU algorithm
# allkeys-lru -> remove any key accordingly to the LRU algorithm
# volatile-random -> remove a random key with an expire set
# allkeys->random -> remove a random key, any key
# volatile-ttl -> remove the key with the nearest expire time (minor TTL)
# noeviction -> don't expire at all, just return an error on write operations
#
# Note: with all the kind of policies, Redis will return an error on write
#       operations, when there are not suitable keys for eviction.
#
#       At the date of writing this commands are: set setnx setex append
#       incr decr rpush lpush rpushx lpushx linsert lset rpoplpush sadd
#       sinter sinterstore sunion sunionstore sdiff sdiffstore zadd zincrby
#       zunionstore zinterstore hset hsetnx hmset hincrby incrby decrby
#       getset mset msetnx exec sort
#
# The default is:
#
# maxmemory-policy volatile-lru

# LRU and minimal TTL algorithms are not precise algorithms but approximated
# algorithms (in order to save memory), so you can select as well the sample
# size to check. For instance for default Redis will check three keys and
# pick the one that was used less recently, you can change the sample size
# using the following configuration directive.
#
# maxmemory-samples 3

############################## APPEND ONLY MODE ###############################

#
# Note that you can have both the async dumps and the append only file if you
# like (you have to comment the "save" statements above to disable the dumps).
# Still if append only mode is enabled Redis will load the data from the
# log file at startup ignoring the dump.rdb file.
# 指定是否在每次更新操作后进行日志记录，Redis在默认情况下是异步的把数据写入磁盘，如果不开启，可能会在断电时导致一段时间内的数据丢失。
# 因为redis本身同步数据文件是按上面save条件来同步的，所以有的数据会在一段时间内只存在于内存中。默认为no
# IMPORTANT: Check the BGREWRITEAOF to check how to rewrite the append
# log file in background when it gets too big.

appendonly yes

# 指定更新日志文件名，默认为appendonly.aof
# appendfilename appendonly.aof

# The fsync() call tells the Operating System to actually write data on disk
# instead to wait for more data in the output buffer. Some OS will really flush
# data on disk, some other OS will just try to do it ASAP.

# 指定更新日志条件，共有3个可选值：
# no:表示等操作系统进行数据缓存同步到磁盘（快）
# always:表示每次更新操作后手动调用fsync()将数据写到磁盘（慢，安全）
# everysec:表示每秒同步一次（折衷，默认值）

appendfsync everysec
# appendfsync no

# When the AOF fsync policy is set to always or everysec, and a background
# saving process (a background save or AOF log background rewriting) is
# performing a lot of I/O against the disk, in some Linux configurations
# Redis may block too long on the fsync() call. Note that there is no fix for
# this currently, as even performing fsync in a different thread will block
# our synchronous write(2) call.
#
# In order to mitigate this problem it's possible to use the following option
# that will prevent fsync() from being called in the main process while a
# BGSAVE or BGREWRITEAOF is in progress.
#
# This means that while another child is saving the durability of Redis is
# the same as "appendfsync none", that in pratical terms means that it is
# possible to lost up to 30 seconds of log in the worst scenario (with the
# default Linux settings).
#
# If you have latency problems turn this to "yes". Otherwise leave it as
# "no" that is the safest pick from the point of view of durability.
no-appendfsync-on-rewrite no

# Automatic rewrite of the append only file.
# Redis is able to automatically rewrite the log file implicitly calling
# BGREWRITEAOF when the AOF log size will growth by the specified percentage.
#
# This is how it works: Redis remembers the size of the AOF file after the
# latest rewrite (or if no rewrite happened since the restart, the size of
# the AOF at startup is used).
#
# This base size is compared to the current size. If the current size is
# bigger than the specified percentage, the rewrite is triggered. Also
# you need to specify a minimal size for the AOF file to be rewritten, this
# is useful to avoid rewriting the AOF file even if the percentage increase
# is reached but it is still pretty small.
#
# Specify a precentage of zero in order to disable the automatic AOF
# rewrite feature.

auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb

################################## SLOW LOG ###################################

# The Redis Slow Log is a system to log queries that exceeded a specified
# execution time. The execution time does not include the I/O operations
# like talking with the client, sending the reply and so forth,
# but just the time needed to actually execute the command (this is the only
# stage of command execution where the thread is blocked and can not serve
# other requests in the meantime).
#
# You can configure the slow log with two parameters: one tells Redis
# what is the execution time, in microseconds, to exceed in order for the
# command to get logged, and the other parameter is the length of the
# slow log. When a new command is logged the oldest one is removed from the
# queue of logged commands.

# The following time is expressed in microseconds, so 1000000 is equivalent
# to one second. Note that a negative number disables the slow log, while
# a value of zero forces the logging of every command.
slowlog-log-slower-than 10000

# There is no limit to this length. Just be aware that it will consume memory.
# You can reclaim memory used by the slow log with SLOWLOG RESET.
slowlog-max-len 1024

################################ VIRTUAL MEMORY ###############################

### WARNING! Virtual Memory is deprecated in Redis 2.4
### The use of Virtual Memory is strongly discouraged.

### WARNING! Virtual Memory is deprecated in Redis 2.4
### The use of Virtual Memory is strongly discouraged.

# Virtual Memory allows Redis to work with datasets bigger than the actual
# amount of RAM needed to hold the whole dataset in memory.
# In order to do so very used keys are taken in memory while the other keys
# are swapped into a swap file, similarly to what operating systems do
# with memory pages.
# 指定是否启用虚拟内存机制，默认值为no，
# VM机制将数据分页存放，由Redis将访问量较少的页即冷数据swap到磁盘上，访问多的页面由磁盘自动换出到内存中
# 把vm-enabled设置为yes，根据需要设置好接下来的三个VM参数，就可以启动VM了
# vm-enabled no
# vm-enabled yes

# This is the path of the Redis swap file. As you can guess, swap files
# can't be shared by different Redis instances, so make sure to use a swap
# file for every redis process you are running. Redis will complain if the
# swap file is already in use.
#
# Redis交换文件最好的存储是SSD（固态硬盘）
# 虚拟内存文件路径，默认值为/tmp/redis.swap，不可多个Redis实例共享
# *** WARNING *** if you are using a shared hosting the default of putting
# the swap file under /tmp is not secure. Create a dir with access granted
# only to Redis user and configure Redis to create the swap file there.
# vm-swap-file /tmp/redis.swap

# With vm-max-memory 0 the system will swap everything it can. Not a good
# default, just specify the max amount of RAM you can in bytes, but it's
# better to leave some margin. For instance specify an amount of RAM
# that's more or less between 60 and 80% of your free RAM.
# 将所有大于vm-max-memory的数据存入虚拟内存，无论vm-max-memory设置多少，所有索引数据都是内存存储的（Redis的索引数据就是keys）
# 也就是说当vm-max-memory设置为0的时候，其实是所有value都存在于磁盘。默认值为0
# vm-max-memory 0

# Redis swap文件分成了很多的page，一个对象可以保存在多个page上面，但一个page上不能被多个对象共享，vm-page-size是要根据存储的数据大小来设定的。
# 建议如果存储很多小对象，page大小最后设置为32或64bytes；如果存储很大的对象，则可以使用更大的page，如果不确定，就使用默认值
# vm-page-size 32

# 设置swap文件中的page数量由于页表（一种表示页面空闲或使用的bitmap）是存放在内存中的，在磁盘上每8个pages将消耗1byte的内存
# swap空间总容量为 vm-page-size * vm-pages
#
# With the default of 32-bytes memory pages and 134217728 pages Redis will
# use a 4 GB swap file, that will use 16 MB of RAM for the page table.
#
# It's better to use the smallest acceptable value for your application,
# but the default is large in order to work in most conditions.
# vm-pages 134217728

# Max number of VM I/O threads running at the same time.
# This threads are used to read/write data from/to swap file, since they
# also encode and decode objects from disk to memory or the reverse, a bigger
# number of threads can help with big objects even if they can't help with
# I/O itself as the physical device may not be able to couple with many
# reads/writes operations at the same time.
# 设置访问swap文件的I/O线程数，最后不要超过机器的核数，如果设置为0，那么所有对swap文件的操作都是串行的，可能会造成比较长时间的延迟，默认值为4
# vm-max-threads 4

############################### ADVANCED CONFIG ###############################

# Hashes are encoded in a special way (much more memory efficient) when they
# have at max a given numer of elements, and the biggest element does not
# exceed a given threshold. You can configure this limits with the following
# configuration directives.
# 指定在超过一定的数量或者最大的元素超过某一临界值时，采用一种特殊的哈希算法
# hash-max-zipmap-entries 512
# hash-max-zipmap-value 64

# Similarly to hashes, small lists are also encoded in a special way in order
# to save a lot of space. The special representation is only used when
# you are under the following limits:
list-max-ziplist-entries 512
list-max-ziplist-value 64

# Sets have a special encoding in just one case: when a set is composed
# of just strings that happens to be integers in radix 10 in the range
# of 64 bit signed integers.
# The following configuration setting sets the limit in the size of the
# set in order to use this special memory saving encoding.
set-max-intset-entries 512

# Similarly to hashes and lists, sorted sets are also specially encoded in
# order to save a lot of space. This encoding is only used when the length and
# elements of a sorted set are below the following limits:
zset-max-ziplist-entries 128
zset-max-ziplist-value 64

# Active rehashing uses 1 millisecond every 100 milliseconds of CPU time in
# order to help rehashing the main Redis hash table (the one mapping top-level
# keys to values). The hash table implementation redis uses (see dict.c)
# performs a lazy rehashing: the more operation you run into an hash table
# that is rhashing, the more rehashing "steps" are performed, so if the
# server is idle the rehashing is never complete and some more memory is used
# by the hash table.
#
# The default is to use this millisecond 10 times every second in order to
# active rehashing the main dictionaries, freeing memory when possible.
#
# If unsure:
# use "activerehashing no" if you have hard latency requirements and it is
# not a good thing in your environment that Redis can reply form time to time
# to queries with 2 milliseconds delay.
# 指定是否激活重置哈希，默认为开启
activerehashing yes

################################## INCLUDES ###################################

# 指定包含其他的配置文件，可以在同一主机上多个Redis实例之间使用同一份配置文件，而同时各实例又拥有自己的特定配置文件
# include /path/to/local.conf
# include /path/to/other.conf


```



### 使用

#### 安装 iredis

```shell
$ pip3 install iredis
```

#### 命令行通过加强工具 iredis 连接

```shell
$ iredis --url redis://39.102.138.62:6379/1
```

#### 设置某个键的值

```shell
$ set testkey "kobe"
```

#### 取得某个键的值

```shell
$ get testkey
```

#### 获取 redis 服务器的统计信息

```shell
$ info
```



[(6条消息) Redis——配置允许远程连接_小诸葛的博客-CSDN博客](https://blog.csdn.net/LONG_Yi_1994/article/details/113940332)



## RabbitMQ

<a href="http://39.102.138.62:15672/#/"><img src="https://img.shields.io/badge/RabbitMQ%20-3.9.4-green" ></a><a href="http://39.102.138.62:15672/#/"><img src="https://img.shields.io/badge/Erlang%20-23.3.4.5-yellowgreen" ></a>

- 环境准备:
  
   [🔗 rabbitmq安装指南](https://blog.csdn.net/u010783161/article/details/104833030)
  [🔗 rabbitmq web访问账号设置](https://blog.csdn.net/u014650004/article/details/105800637?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-1.essearch_pc_relevant&spm=1001.2101.3001.4242)
  
- yum 安装的安装路径为 `/usr/lib/rabbitmq/lib/rabbitmq_server-xxx`

- 启动/查看状态/停止/重启
  `service rabbitmq-server start/status/stop/restart`

```bash
yum -y update
yum -y install epel-release
yum -y install erlang socat
erl -verison  
sudo rabbitmqctl add_user ibepo 123456
sudo rabbitmqctl set_user_tags ibepo administrator
```

## jenkins

```bash
service jenkins restart #重启 jenkins
```



## Tailwind

宽度

`w-40`

其他尺寸都隐藏,桌面模式 现身

`hidden lg:block`

竖向排列

`flex  flex-col`

纵向铺满全屏幕,横向尺寸固定

`w-60 h-screen`

fflex 布局,垂直方向居中,*从行首起始位置开始排列*

```
.mx-6 {
    margin-left: 1.5rem/* 24px */;
    margin-right: 1.5rem/* 24px */;
}
.mt-10 {
    margin-top: 2.5rem/* 40px */;
}
```



`flex items-center justify-start mx-6 mt-10`

## Vite

- 基于 [unplugin-vue-components](https://www.npmjs.com/package/unplugin-vue-components) 的 vue 插件，可通过识别自定义组件 tag 前缀自动导入组件的工具。
-  [unplugin-element-plus](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Felement-plus%2Funplugin-element-plus),按需要引入饿了么组件



## node

```shell
npm install n -g
sudo n lts
sudo n stable
n <cr> #n +回车 切换当前 node 版本

export NODE_HOME=/usr/local
export PATH=$NODE_HOME/bin:$PATH
export NODE_PATH=$NODE_HOME/lib/node_modules:$PATH
```



## vue3

- [Vue3使用Mitt替代EventBus ](https://zhuanlan.zhihu.com/p/340244131)
- `<script setup>`语法糖,省去了 export default 的返回值,在其中的导入的 js,也可直接用到`template`中

```vue
//1.
<script setup>
console.log('hello script setup')
</script>

//2.
<script setup>
// 变量
const msg = 'Hello!'
// 函数
function log() {
  console.log(msg)
}
</script>
<template>
  <div @click="log">{{ msg }}</div>
</template>

```

### 一些维度

- vdom
- template
- jsx   

![image-20211109113931898](https://gitee.com/ibepo/ogcip/raw/master/20211109113932.png)



[【前端面试必备】Vue2与Vue3核心之『响应式原理』_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Dk4y127Ha?spm_id_from=333.999.0.0)



## vetega

- topbar
- 登录页
- 站点页脚
- 左侧菜单 navbar
- 站点锚点
- 右键菜单
- 查询列表页
- 分步表单页
- 分组表单页
- 开篇列表页





## Maven


 mvn clean package依次执行了clean、resources、compile、testResources、testCompile、test、jar(打包)等７个阶段。
 mvn clean install依次执行了clean、resources、compile、testResources、testCompile、test、jar(打包)、install等8个阶段。
 mvn clean deploy依次执行了clean、resources、compile、testResources、testCompile、test、jar(打包)、install、deploy等９个阶段。

 package命令完成了项目编译、单元测试、打包功能，但没有把打好的可执行jar包（war包或其它形式的包）布署到本地maven仓库和远程maven私服仓库

 install命令完成了项目编译、单元测试、打包功能，同时把打好的可执行jar包（war包或其它形式的包）布署到本地maven仓库，但没有布署到远程maven私服仓库

 deploy命令完成了项目编译、单元测试、打包功能，同时把打好的可执行jar包（war包或其它形式的包）布署到本地maven仓库和远程maven私服仓库

1. 父pom 的 packaging 要设为 pom,子 pom 的设为 jar
2. 父子的契约达成条件是 子 pom 的 parent 设为父 pom,且父 pom 中的 modules 中存在子 pom
3. 老老实实的维护版本号,不依赖 parents 中的默认配置是最稳妥的方式
4. spring-boot-starter-parent 的父依赖是spring-boot-dependencies,其中定义了一些 version,但是不全不要过分依赖
5. maven获取依赖包错误代码：501, ReasonPhrase:HTTPS Required❓
   自2020.01.15后maven中央仓库要求使用https进行访问，将maven配置中的原中央仓库地址http更改为https即可

## NPM

```SHELL
$ npm install eslint --save-dev #将 eslint 安装到开发依赖中
$ ni #一切皆可 ni
```



## Eslint

Eslint 只校验 js,stylelint 校验 css,两者搭配使用,以下是他两的 vscode 插件 需要在 setting.json 配置的`保存自动格式化 `相关代码

```JS
//工作区 setting.json
{
    "editor.codeActionsOnSave": {
        "source.fixAll.eslint": true,
        "source.fixAll.stylelint": true
    },
    "stylelint.validate": [
        "css",
        "scss",
        "vue"
    ],
    "vue3snippets.enable-compile-vue-file-on-did-save-code": false
}

```





## package.json

### scripts

- script 属性的意思是脚本，使用方法是在 cmd 窗口中输入 `npm run 指令` 的形式，如：`npm run lint:create`；
- `"lint:create": "eslint --init"` 这个脚本是为了生成 .eslintrc.js 文件，在介绍 Lint 的时候说到 Lint 应该提供编码规范，规范写在哪里，就写在这个文件，所以我们需要创建它；
- `"lint": "eslint src"` 在介绍 Lint 的时候也说到 Lint 应该提供自动校验代码的程序，这个脚本是让 Lint 自动检验 src 目录下所有的 .js 文件。
- 这里给 `"lint": "eslint src --fix",` 加上 `--fix` 参数，是 Eslint 提供的自动修复基础错误的功能。

```shell
"scripts": {
    "test": "react-scripts test --env=jsdom",
    "lint": "eslint src --fix",
    "lint:create": "eslint --init"
}
```





## Mybatis

### 代码生成器

mybatisplus 的代码生成器在 `3.5.1`之后有较大较好的更新,引入了`建造者模式`,简化了`数据库配置` `包配置` `模板配置` `注入配置` `策略配置`

[代码生成器（3.5.1+版本） | MyBatis-Plus (baomidou.com)](https://baomidou.com/guide/generator-new.html#包配置-packageconfig)

```JAVA
  FastAutoGenerator.create(url, username, password)
                .globalConfig(builder -> {
                    builder.author("ibepo") // 设置作者
                            //.enableSwagger() // 开启 swagger 模式
                            .fileOverride() // 覆盖已生成文件
                            .disableOpenDir()//禁止打开输出目录
                            .outputDir("src/main/java"); // 指定输出目录
                })
                .packageConfig(builder -> {
                    builder.parent("com.simas.goku") // 设置父包名
                            .moduleName("") // 设置父包模块名
                            .pathInfo(Collections.singletonMap(OutputFile.mapperXml, "src/main/resources/mapper")); // 设置mapperXml生成路径
                })
                .strategyConfig(builder -> {
                    builder.addInclude("customer") // 设置需要生成的表名
                            .addTablePrefix("t_", "c_"); // 设置过滤表前缀
                })
                .execute();
```



## MybatisPlus

- 自动填充
- version
- 逻辑删除
- Wrapper



```java
@Override
    public Optional<DwdPersonIoDataVo> findLastIoData(String personCode) {
      //LamdaQueryWrapper的创建方式 可以直接 new ,
      //也可以直接从此 serviceiml 集成的 baseserviceimpl 中 直接 this.lamdaquery 的方式拿到 
     //形式 1
      LambdaQueryWrapper<DwdPersonIoData> queryWrapper = new LambdaQueryWrapper<>();
        queryWrapper.eq(DwdPersonIoData::getPersonCode, personCode);
        queryWrapper.orderByDesc(DwdPersonIoData::getId);
        queryWrapper.last(" limit 1");
        DwdPersonIoData dwdPersonIoData = getBaseMapper().selectOne(queryWrapper);
       //形式 2
       LambdaQueryChainWrapper<DwdPersonIoData> last = this
                .lambdaQuery()
                .eq(DwdPersonIoData::getPersonCode, personCode)
                .orderByDesc(DwdPersonIoData::getId)
                .last("limit 1");
       DwdPersonIoData dwdPersonIoData1 = this.baseMapper.selectOne(last);

      //dto 转 vo
DwdPersonIoDataVo vo = BeanHelper.convertAndCopyWithRuntimeException(DwdPersonIoDataVo.class, dwdPersonIoData);
      
        return Optional.ofNullable(vo);
    }
```



## lombook

```java
@Slf4j lombok log对象
如果不想每次都写private  final Logger logger = LoggerFactory.getLogger(XXX.class); 可以用注解@Slf4j

这样在类中就可以直接使用log对象，

log.debug("debug message");
log.warn("warn message");
log.info("info message");
log.error("error message");
log.trace("trace message");


```

## Jackson

格式化返回的 日期格式

```java
 @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss")
```





## IDEA

[干了5年Java，我终于玩会了IDEA！ - 掘金 (juejin.cn)](https://juejin.cn/post/6988866268312895501#heading-21)

## hutool

输出友好的 json 字符串格式

```java
JSONUtil.toJsonPrettyStr(obj/json)
```



## JWT

[jwt 实践应用以及不适用特殊案例思考 | 山月行 (shanyue.tech)](https://shanyue.tech/post/jwt-guide.html#json-web-token)



1. 网关统一认证方式

![image-20211116141604210](https://gitee.com/ibepo/ogcip/raw/master/20211116141604.png)



2. 应用认证方案

![image-20211116142551585](https://gitee.com/ibepo/ogcip/raw/master/20211116142551.png)





![image-20211116142828945](https://gitee.com/ibepo/ogcip/raw/master/20211116142829.png)



## Nacos

```java
package com.simas.goku.controller;


import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RefreshScope
@RestController
public class ConfigController {

    @Value("${project.name:}")
    private String projectName;

    @Value("${project.org:}")
    private String projectOrg;

    @GetMapping("/config")
    public Map<String, Object> getConfig() {
        Map<String, Object> configMap = new HashMap();
        configMap.put("projectName", projectName);
        configMap.put("projectOrg", projectOrg);
        return configMap;
    }

}

```





## 组织结构

``` 
goku_jindowin
├── goku-kamehameha -- 微服务调用测试 将单体 goku 中的数据库访问那一套移植过来
├── goku-common -- 工具类及通用代码模块
├── goku-auth -- 基于Spring Security Oauth2的统一的认证中心
├── goku-gateway -- 基于Spring Cloud Gateway的微服务API网关服务
├── goku-monitor -- 基于Spring Boot Admin的微服务监控中心
├── goku-admin -- 后台管理系统服务
├── goku-search -- 基于Elasticsearch的商品搜索系统服务
├── goku-portal -- 移动端商城系统服务
├── goku-demo -- 微服务远程调用测试服务
└── config -- 配置中心存储的配置
```

## 技术选型

### 后端技术

| 技术                   | 说明                 | 官网                                                 |
| ---------------------- | -------------------- | ---------------------------------------------------- |
| Spring Cloud           | 微服务框架           | https://spring.io/projects/spring-cloud              |
| Spring Cloud Alibaba   | 微服务框架           | https://github.com/alibaba/spring-cloud-alibaba      |
| Spring Boot            | 容器+MVC框架         | https://spring.io/projects/spring-boot               |
| Spring Security Oauth2 | 认证和授权框架       | https://spring.io/projects/spring-security-oauth     |
| MyBatis                | ORM框架              | http://www.mybatis.org/mybatis-3/zh/index.html       |
| MyBatisGenerator       | 数据层代码生成       | http://www.mybatis.org/generator/index.html          |
| PageHelper             | MyBatis物理分页插件  | http://git.oschina.net/free/Mybatis_PageHelper       |
| Knife4j                | 文档生产工具         | https://github.com/xiaoymin/swagger-bootstrap-ui     |
| Elasticsearch          | 搜索引擎             | https://github.com/elastic/elasticsearch             |
| RabbitMq               | 消息队列             | https://www.rabbitmq.com/                            |
| Redis                  | 分布式缓存           | https://redis.io/                                    |
| MongoDb                | NoSql数据库          | https://www.mongodb.com/                             |
| Docker                 | 应用容器引擎         | https://www.docker.com/                              |
| Druid                  | 数据库连接池         | https://github.com/alibaba/druid                     |
| OSS                    | 对象存储             | https://github.com/aliyun/aliyun-oss-java-sdk        |
| MinIO                  | 对象存储             | https://github.com/minio/minio                       |
| JWT                    | JWT登录支持          | https://github.com/jwtk/jjwt                         |
| LogStash               | 日志收集             | https://github.com/logstash/logstash-logback-encoder |
| Lombok                 | 简化对象封装工具     | https://github.com/rzwitserloot/lombok               |
| Seata                  | 全局事务管理框架     | https://github.com/seata/seata                       |
| Portainer              | 可视化Docker容器管理 | https://github.com/portainer/portainer               |
| Jenkins                | 自动化部署工具       | https://github.com/jenkinsci/jenkins                 |
| Kubernetes             | 应用容器管理平台     | https://kubernetes.io/                               |

### 前端技术

| 技术       | 说明                  | 官网                           |
| ---------- | --------------------- | ------------------------------ |
| Vue        | 前端框架              | https://vuejs.org/             |
| Vue-router | 路由框架              | https://router.vuejs.org/      |
| Vuex       | 全局状态管理框架      | https://vuex.vuejs.org/        |
| Element    | 前端UI框架            | https://element.eleme.io/      |
| Axios      | 前端HTTP框架          | https://github.com/axios/axios |
| v-charts   | 基于Echarts的图表框架 | https://v-charts.js.org/       |



## Mac软件

|         工具          |                             地址                             |                             备注                             |
| :-------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|        typora         | [Typora — a markdown editor, markdown reader.](https://typora.io/) |                        主题:Ava Diana                        |
|         Edge          |                                                              | 插件:GitHub加速、Infinity 新标签页 (Pro)、JSON-handle、RSSHub Radar、侧边翻译、收藏猫、NeatDownloadManager Extension、Markdown Nice、Separate Window、Octotree - GitHub code tree、Smart TOC(MD列表)、Tree Style History,Gitako(git 树形显示) |
|      Fast-GitHub      |             https://github.com/ibepo/Fast-GitHub             |                                                              |
|    OpenInTerminal     |           https://github.com/ibepo/OpenInTerminal            |                         Finder 扩展                          |
|       cakebrew        |                                                              |                      homebrew 的桌面端                       |
|      SourceTree       |                                                              |                          GIt 桌面端                          |
|        Mangnet        |                                                              |                        window  manger                        |
|       SSH Shell       |                                                              |                       mac 端 ssh 工具                        |
|        ApiPost        |                                                              |   国产 postman ,支持在线生成文档,kefanbufan@163  lz123321    |
|       SniPaste        |                                                              |                             截图                             |
|          Mos          |                                                              |                    mac 下鼠标平滑移动工具                    |
|        clashx         |                                                              |                        飞机场配置工具                        |
|         IINA          |                                                              |                          mac 播放器                          |
|       Terimius        |                                                              |                     终端和 ftp 传输工具                      |
|        draw.io        |                                                              |                           UML工具                            |
|         Keka          |                                                              |                          解压缩工具                          |
|    The Unarchiver     |                                                              |                          解压缩工具                          |
| Nest Download Manager |                                                              |                            下载器                            |
|        iTerm2         |                                                              |                          命令行工具                          |
|        Downie4        |                                                              |                          视频下载器                          |
|         cubox         |                                                              |                           标签管理                           |
|         Drop          |                                                              |                           色号提取                           |
|        Charles        |                                                              |                      web debugger proxy                      |
|       MobaXterm       |                https://mobaxterm.mobatek.net/                | Enhanced terminal for Windows with X11 server, tabbed SSH client, network tools and much more |
|         Idea          |                                                              |               插件:IDE Eval Reset(无限期试用)                |
|      Sequel pro       |                                                              |                         数据库客户端                         |
|         Hyper         |                                                              |                      mac 命令行终端工具                      |
|         Xmind         |                                                              |                           脑图工具                           |
|       Swithhost       | [SwitchHosts/README_cn.md at master · oldj/SwitchHosts (github.com)](https://github.com/oldj/SwitchHosts/blob/master/README_cn.md) |                      本地修改 host 神器                      |
|       transmit        |                                                              |                        Ftp 工具最优解                        |
|         Macwk         |                    https://www.macwk.com/                    |                      盗版mac 应用集散地                      |
|       TablePlus       |                                                              |                      Redis mysql 客户端                      |
|       沙拉查词        |       [Saladict 沙拉查词](https://saladict.crimx.com/)       |                                                              |

端口说明

|    服务    |                端口                |
| :--------: | :--------------------------------: |
| `keyclock` | [9010](http://39.102.138.62:9010/) |



##### [懒程序员和他的 dotfiles - CoderZh Blog](https://blog.coderzh.com/2016/03/19/dotfiles/)

## skhdrc

```shell
alt+{1,2,3,4,5,6} #切换桌面
alt+hjkl #切换当前屏幕的焦点

ctrl+alt+a #切换到平铺模式
ctrl+alt+d #切换到普通浮动模式

shift+cmd +{12334}  #将当前关注移动到指定桌面
ctrl+cmd+{12334}    #将当前关注发射到指定显示器
```

最最重要的几个快捷键:

- alt + 数字键 可以快速进入对应空间
- alt + h/j/k/l 可以快速聚焦当前空间的某个窗口
- alt + f 将某个窗口全屏 (再按一次会推出全屏)
- shift + cmd + 数字键 可以将当前活跃窗口移动到指定空间
- ctrl + alt + 数字键 激活指定显示器
- ctrl + cmd + 数字键 将当前激活窗口发送到指定显示器上面去 (指定显示器不能是浮动模式)



## yabai

### focus

| Action      | Key Combination |
| ----------- | --------------- |
| focus west  | alt + h         |
| focus south | alt + j         |
| focus north | alt + k         |
| focus east  | alt + l         |

#### Resize windows

| Action       | Key Combination |
| ------------ | --------------- |
| Resize left  | shfit + cmd + h |
| Resize down  | shfit + cmd + j |
| Resize up    | shfit + cmd + k |
| Resize right | shfit + cmd + l |
| Equalise     | shfit + cmd + 0 |

#### Rotate windows

| Action               | Key Combination |
| -------------------- | --------------- |
| Rotate clockwise     | shift + alt + r |
| Rotate anticlockwise | alt + r         |
| Flip on x-axis       | shift + alt + x |
| Flip on y-axis       | shift + alt + y |

#### Window actions

| Action            | Key Combination |
| ----------------- | --------------- |
| Fullscreen        | alt + f         |
| Native fullscreen | shift + alt + f |
| Center window     | shift + alt + c |

#### Insertion point

| Action                       | Key Combination         |
| ---------------------------- | ----------------------- |
| Insert left                  | shift + lctrl + alt + h |
| Insert down                  | shift + lctrl + alt + j |
| Insert up                    | shift + lctrl + alt + k |
| Insert right                 | shift + lctrl + alt + l |
| Cancel insert (chunkwm only) | shift + lctrl + alt + x |

#### Misc

| Action          | Key Combination         |
| --------------- | ----------------------- |
| Toggle float    | shift + alt + space     |
| Toggle gaps     | lctrl + alt + g         |
| Restart chunkwm | lctrl + shift + alt + r |





#### Move windows

shift + alt + hjkl

#### Move windows to workspace

| Action                      | Key Combination   |
| --------------------------- | ----------------- |
| Send to last active desktop | shift + alt + m   |
| Send to previous workplace  | shift + alt + p   |
| Send to next workplace      | shift + alt + n   |
| Send to workplace           | shift + alt + num |

## 环境搭建

### 开发环境

| 工具          | 版本号 | 下载                                                         |
| ------------- | ------ | ------------------------------------------------------------ |
| JDK           | 1.8    | https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html |
| Mysql         | 5.7    | https://www.mysql.com/                                       |
| Redis         | 5.0    | https://redis.io/download                                    |
| Elasticsearch | 7.6.2  | https://www.elastic.co/cn/downloads/elasticsearch            |
| Kibana        | 7.6.2  | https://www.elastic.co/cn/downloads/kibana                   |
| Logstash      | 7.6.2  | https://www.elastic.co/cn/downloads/logstash                 |
| MongoDb       | 4.2.5  | https://www.mongodb.com/download-center                      |
| RabbitMq      | 3.7.14 | http://www.rabbitmq.com/download.html                        |
| nginx         | 1.10   | http://nginx.org/en/download.html                            |



kamehouse

![image-20211110121753806](https://gitee.com/ibepo/ogcip/raw/master/20211110121754.png)



### 搭建步骤

> Windows环境部署

- Windows环境搭建请参考：[mall-swarm在Windows环境下的部署](http://www.macrozheng.com/#/deploy/mall_swarm_deploy_windows);
- `mall-admin-web`项目的安装及部署请参考：[mall前端项目的安装与部署](http://www.macrozheng.com/#/deploy/mall_deploy_web);
- `ELK`日志收集系统的搭建请参考：[SpringBoot应用整合ELK实现日志收集](http://www.macrozheng.com/#/technology/mall_tiny_elk);
- 使用MinIO存储文件请参考：[前后端分离项目，如何优雅实现文件存储](http://www.macrozheng.com/#/technology/minio_use);
- 读写分离解决方案请参考：[你还在代码里做读写分离么，试试这个中间件吧](http://www.macrozheng.com/#/reference/gaea);
- `分布式事务`解决方案请参考：[使用Seata彻底解决Spring Cloud中的分布式事务问题！](http://www.macrozheng.com/#/cloud/seata)。

> Docker环境部署

- 使用虚拟机安装CentOS7.6请参考：[虚拟机安装及使用Linux，看这一篇就够了](http://www.macrozheng.com/#/reference/linux_install);
- Docker环境的安装请参考：[开发者必备Docker命令](http://www.macrozheng.com/#/reference/docker);
- 本项目Docker镜像构建请参考：[使用Maven插件为SpringBoot应用构建Docker镜像](http://www.macrozheng.com/#/reference/docker_maven);
- 本项目在Docker容器下的部署请参考：[mall-swarm在Linux环境下的部署（基于Docker容器）](http://www.macrozheng.com/#/deploy/mall_swarm_deploy_docker);
- 本项目使用Jenkins自动化部署请参考：[微服务架构下的自动化部署，使用Jenkins来实现](http://www.macrozheng.com/#/deploy/mall_swarm_deploy_jenkins)。

> Kubernetes环境部署

- 本项目使用Kubernetes部署请参考：[mall-swarm微服务项目在K8S下的实践！](http://www.macrozheng.com/#/deploy/mall_swarm_deploy_k8s)

- 监控中心应用信息，访问地址：http://192.168.3.101:8101

- API文档信息，访问地址：http://192.168.3.101:8201

- 日志收集系统信息，访问地址：http://192.168.3.101:5601

- 可视化容器管理，访问地址：http://192.168.3.101:9000

## 容器化基础平台搭建

![image-20211112085203065](https://gitee.com/ibepo/ogcip/raw/master/20211112085203.png)

### traefik

- 服务发现 docker 容器中的 基础设置
- 通过 `静态配置`或者 `compose 中的 labels和 command` 配置默认的路由转发规则
- 

### 数据库备份

```shell
echo ${WORKSPACE}
echo `ls ${WORKSPACE}/../backup-database/*.sql -t | head -1`
echo ${JENKINS_HOME}

mysql -u root -h 172.18.0.2 -P 3306 --password=SHBlueHour@2019 -D iot < `ls ${WORKSPACE}/../backup-database/*.sql -t | head -1`
```

```shell
mysqldump --hex-blob --default-character-set=utf8 -u root -h 172.17.0.9 -P 3306 --password=SHBlueHour@2019 iot > iot_production_`date +%w`.sql
```



### 后端部署

##### jenkins后端部署脚本案例(立宏iot 后端系统)

```shell
#echo "shutdown iot-app..."
#curl --connect-timeout 5 --max-time 10 -X POST http://localhost:8099/actuator/shutdown

port=9099
pid=$(ps -ef | grep "iot-app.jar" | grep -v grep | awk '{print $2}')
echo $pid
if [ -n "$pid" ]
then
   echo "kill iot-app.jar -9 pid:" $pid
   kill -9 $pid
fi
sleep 10
cd /opt/apps/server

rm -rf iot-app.jar.bak

mv iot-app.jar iot-app.jar.bak

mv iot-app-1.0.0-SNAPSHOT-exec.jar iot-app.jar

echo "startup application..."
nohup java -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=iot-app.hprof -jar -Dspring.profiles.active=production iot-app.jar  >/dev/null 2>&1  &


echo "done"

```



### 前端部署

[op-note/deploy-fe.md at master · shfshanyue/op-note (github.com)](https://github.com/shfshanyue/op-note/blob/master/deploy-fe.md)

[op-note/deploy-fe-with-docker.md at master · shfshanyue/op-note (github.com)](https://github.com/shfshanyue/op-note/blob/master/deploy-fe-with-docker.md)

#### 使用多阶段构建优化镜像

这中间其实经历了不少坎坷，其中过程如何，详见我的另一篇文章: [如何使用 docker 部署前端应用](https://juejin.im/post/5c83cbaa6fb9a04a0f65fdaa)。

其中主要的优化也是在上述所提到的两个方面

1. 构建镜像体积由 1G+ 变为 10M+
2. 构建镜像时间由 5min+ 变为 1min (视项目复杂程度，大部分时间在构建时间与上传静态资源时间)

```
FROM node:alpine as builder

ENV PROJECT_ENV production
ENV NODE_ENV production

WORKDIR /code

ADD package.json /code
RUN npm install --production

ADD . /code

# npm run uploadCdn 是把静态资源上传至 oss 上的脚本文件，将来会使用 cdn 对 oss 加速
RUN npm run build && npm run uploadCdn

# 🦖选择更小体积的基础镜像
FROM nginx:alpine
COPY --from=builder code/public/index.html code/public/favicon.ico /usr/share/nginx/html/
COPY --from=builder code/public/static /usr/share/nginx/html/static
```

那它怎么做的

1. 先 `ADD package.json /code`, 再 `npm install --production` 之后 `Add` 所有文件。充分利用镜像缓存，减少构建时间
2. 多阶段构建，大大减小镜像体积

另外还可以有一些小优化，如

- `npm cache` 的基础镜像或者 `npm` 私有仓库，减少 `npm install` 时间，减小构建时间
- `npm install --production` 只装必要的包

前端看着自己优化的 `dockerfile`，想着前几天还被运维吵，说什么磁盘一半的空间都被前端的镜像给占了，想着自己节省了前端镜像几个数量级的体积，为公司好像省了不少服务器的开销，想着自己的基础盘进一步扩大，又不禁开心的笑了

这时候再思考文章最前面两个问题

1. 缓存，缓存由前端控制，缓存在oss上设置，将会使用 cdn 对 oss 加速。此时缓存由前端写脚本控制
2. 跨域，跨域仍由运维在 `nginx` 中配置

立宏开发库配置

![image-20220516152740422](https://gitee.com/ibepo/ogcip/raw/master/20220516152741.png)

![image-20220516153233398](https://gitee.com/ibepo/ogcip/raw/6c4279f622e6d6bf6e8ba8f7bba8a7841e78b8ce/20220516153234.png)

