### epel 
```shell
sudo yum install -y yum-utils
sudo yum install epel-release # epel-release
```

### neofetch
```shell
curl -o /etc/yum.repos.d/konimex-neofetch-epel-7.repo https://copr.fedorainfracloud.org/coprs/konimex/neofetch/repo/epel-7/konimex-neofetch-epel-7.repo
yum install neofetch
```

### htop
`yum install htop`

### ripgrep
```shell
$ sudo yum-config-manager --add-repo=https://copr.fedorainfracloud.org/coprs/carlwgeorge/ripgrep/repo/epel-7/carlwgeorge-ripgrep-epel-7.repo
$ sudo yum install ripgrep
```

### vim
```shell
# vimrc
#全局配置
vim  /etc/vimrc
#用户配置
cd ~
touch ~/.vimrc
```

### Redis
```shell
#redis
cd /usr/local
mkdir redis
cd redis
tar xvzf /root/mysoft/redis-5.0.8.tar.gz -C ./
cd redis-5.0.8/
yum -y install gcc
make MALLOC=libc
make install
cd utils/
./install_server.sh
redis-cli
vim /eetc/redis/6379.conf
将`bind 127.0.0.1` 修改为`0.0.0.0`
将 `requirepass foobared` 改为自己的密码
systemctl restart redis-6379.service
redis-cli
auto 你的密码
set foo bar
get foo
```


---
---

### mysql
* 配置文件位置`/etc/my.cnf`
* 基础文件位置`/usr/local/mysql`
* 数据文件位置`/usr/local/mysql/data`
* 关于`my.ini`  https://blog.csdn.net/lienfeng6/article/details/78140404

```shell
# mysql

##remove mariadb
rpm -qa|grep mariadb
yum -y remove xxx

## 解压mysql压缩包
tar -zxvf /root/mysql-5.7.30-linux-glibc2.12-x86_64.tar.gz -C /usr/local/
mv mysql-5.7.30-linux-glibc2.12-x86_64 mysql
groupadd mysql
useradd -q mysql mysql

cd /etc && vim my.cnf

mkdir /var/lib/mysql
chomod 777 /var/lib/mysql
cd /usr/local/mysql
./bin/mysqld --initialize --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data/
记住生成的密码

## 创建systemctl 自启动文件
cp ./support-files/mysql.server /etc/init.d/mysqld

## 设置mysql路径位置
vim /etc/init.d/mysqld
basedir=/usr/local/mysql
datadir=/usr/local/mysql/data
chmod +x /etc/init.d/mysqld

chkconfig -add mysqld
chkconfig --list mysqld
```
### nginx
```shell
nc -zvw3 139.196.77.225 80

```
https://akynazh.site/posts/2022/11/linux-software-installation-and-configuration-records/#python3