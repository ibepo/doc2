## 参考
[解决ssh登录后闲置时间过长而断开连接](https://blog.csdn.net/abld99/article/details/69388858)

## 查看 ssh 公钥秘钥
```shell
cd ~/.ssh
bat id_rsa.pub
```

## 本地生产秘钥对
```shell
ssh-keygen -t rsa
```

## 修改ssh文件夹权限过于开放的问题
```shell
chmod 600 ~/.ssh/id_rsa ~/.ssh/id_rsa.pub
```

## 登录远程主机,并复制秘钥对
```shell
$ ssh-copy-id -i ~/.ssh/id_rsa.pub root@82.157.172.14
```

```shell
$ ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu@82.157.172.14
```

```
$ ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu@82.157.172.14
```

## 给远程主机设置别名
进入`～/.ssh` 目录，查看是否有名为`config`的文件，如果没有直接创建一个，然后修改config文件为远程主机起 别名
```shell
vim ~/.ssh/config
```

## config 文件的编写可以参考下面
```vim
Host s
HostName 39.102.138.62
User root
Port 22
```

## 通过别名 ssh 到远程主机
```shell
ssh s
```

## 删除当前服务器登陆的其他终端连接

``` shell
w
pkill -kill -t pts/0 
```

## SSH 上传/下载文件
SSH 可以通过 scp 命令来上传文件，是 Linux 系统下基于 SSH 登陆进行安全的远程文件拷贝命令，scp 是 secure copy 的简写，可以使用它上传本地文件夹到远程服务器，也可以从远程服务器上下载文件夹到本地：

```bash
# 上传文件夹到远程服务器
scp -P port -r /local/dir username@servername:/remote/dir
# scp -p 2333 -r /test/a root@192.168.0.101:/var/b

# 从远程服务器下载文件夹
scp -P port -r username@servername:/remote/dir/ /local/dir
# scp -p 2333 -r root@192.168.0.101:/var/b /test/a
```

`-r` 参数表示递归复制，即复制该目录下面的文件和目录，如果要上传单个文件，只要把 `-r` 删除。大写的 `P` 表示的是端口，如果还是默认的 SSH 端口 22 没有更改，则不需要 `-P`。
