云服务器选择`ubuntu18.4`镜像

在远程服务器的授权密钥上安装 本机的SSH 密钥
```shell 
ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu@82.158.173.24
```
 
修改主机名
```shell 
hostnamectl set-hostname`
``` 

更新apt-get
`sudo apt-get update` 
 
安装工具箱
```shell
sudo apt install ripgrep tmux htop

# 通过snap在 ubuntu 18.04 上安装最新的fzf
sudo snap install fzf-carroarmato0 
sudo ln -s /snap/fzf-carroarmato0/27/bin/fzf  /usr/local/bin/fzf
```

 安装docker和docker-compose
```shell
sudo apt-get install docker
sudo apt-get install docker-compose
```
 