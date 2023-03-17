# ssh免密登录

## 编辑 `~/.ssh/config`

```fallback
1Host 输入代替名
2    HostName 输入IP
3    Port 输入端口号
4    User 输入用户名
5    # ProxyCommand "C:\Program Files\Git\mingw64\bin\connect.exe" -S 127.0.0.1:7890 -a none %h %p
6
7# 定时发送心跳确保不断开连接
8ServerAliveInterval 30 # 每隔30秒发送一次
9ServerAliveCountMax 60 # 连续60次服务端无响应断开连接
```

## 生成并发送密钥

```fallback
1ssh-keygen -t rsa
```

然后将公钥 `~/.ssh/id_rsa.pub` 复制到目标主机 `~/.ssh/authorized_keys` 文件中。

## 可能出现的问题：密钥算法不匹配

如果出现以下错误：

no matching key exchange method found. Their offer: diffie-hellman-group1-sha1

则是本地密钥算法与远程主机密钥算法**不匹配**造成的！

可以在ssh_config或config文件中添加密钥算法配置：

```fallback
1Host 输入代替名
2	HostName 输入IP
3	Port 输入端口号
4	User 输入用户
5	KexAlgorithms +diffie-hellman-group1-sha1
```