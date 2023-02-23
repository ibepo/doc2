### 查看 ssh 公钥秘钥
```shell
cd ~/.ssh
bat id_rsa.pub
```

### 本地生产秘钥对
```shell
ssh-keygen -t rsa
```

### 修改ssh文件夹权限过于开放的问题
```shell
chmod 600 ~/.ssh/id_rsa ~/.ssh/id_rsa.pub
```

### 登录远程主机,并复制秘钥对
```shell
$ ssh-copy-id -i ~/.ssh/id_rsa.pub root@82.157.172.14
```

```shell
$ ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu@82.157.172.14
```

```
$ ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu@82.157.172.14
```

### 给远程主机设置别名
进入`～/.ssh` 目录，查看是否有名为`config`的文件，如果没有直接创建一个，然后修改config文件为远程主机起 别名
```shell
vim ~/.ssh/config
```

### config 文件的编写可以参考下面
```vim
Host s
HostName 39.102.138.62
User root
Port 22
```

### 通过别名 ssh 到远程主机
```shell
ssh s
```
