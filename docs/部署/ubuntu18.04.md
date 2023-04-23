 安装ubuntu18.4

 在远程服务器的授权密钥上安装 本机的SSH 密钥
 `ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu@82.157.172.14`
 
 修改主机名`hostnamectl set-hostname`
 
 更新apt-get`sudo apt-get update` 
 
 安装docker
 ```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
 ```
