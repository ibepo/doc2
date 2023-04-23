1. 安装ubuntu18.4
2. 修改主机名
`hostnamectl set-hostname`
3. 在远程服务器的授权密钥上安装 本机的SSH 密钥
`ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu@82.157.172.14`
4. 安装docker
