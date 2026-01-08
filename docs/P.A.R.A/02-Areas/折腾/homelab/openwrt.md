## 安装基础软件包
```
$ yum install -y vim unzip zip wget gzip zlib zlib-devel lsof gcc-c++ make
```

## 安装docker
```shell
yum install -y yum-utils
yum-config-manager \ 
     --add-repo \        https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce docker-ce-cli containerd.io
systemctl start docker

```
[Site Unreachable](https://linuxopsys.com/topics/linux-distribution-list#heading-6)