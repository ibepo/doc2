言简意赅的docker教程.可以迅速的熟悉和学会docker的各种操作.

在linux和mac上安装docker的方式如下:

CentOS
yum -y install yum-utils device-mapper-persistent-data lvm2
yum makecache fast
yum -y install docker-ce
Mac 安装 Docker for Mac 即可
镜像加速
CentOS
默认下载Docker会去国外服务器下载，速度较慢，可以设置为阿里云镜像源，速度更快

yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
Mac
登陆到阿里云找到镜像中心/镜像加速器会看到属于你自己的镜像加速器地址

https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors

# 一般长这个样子
https://xxxxx.mirror.aliyuncs.com
将这个地址填写到docker的Preference的Docker Engine里 json的文件格式

{
  "debug": true,
  "experimental": false,
  "registry-mirrors": [
    "https://xxxx.mirror.aliyuncs.com"
  ]
}
然后重启Docker

Proxy
如果你使用一些proxy 软件例如ssr v2ray等,如果速度还可以的情况可以在终端使用代理的形式.

启动docker
完成上面的操作已经简单的配置好了docker.启动docker.

安装成功后，需要手动启动，设置为开机启动，并测试一下 Docker

#启动docker服务
systemctl start docker
#设置开机自动启动
systemctl enable docker

#Mac 直接省略上面打开docker客户端设置开机启动，当然你可以使用brew services的方式如果你使用brew cask安装的docker
#测试
docker run hello-world
Docker的仓库
Docker官方的中央仓库设置镜像加速后速度就不会很慢推荐使用
https://hub.docker.com/
在公司内部会采用私服的方式拉取镜像（添加配置）一般都是用linux做服务器
//需要创建 /etc/docker/daemon.json，并添加如下内容
{
    "registry-mirrors":["https://registry.docker-cn.com"],
    "insecure-registries":["ip:port"]
}
添加后需要重启docker

#重启两个服务
systemctl daemon-reload
systemctl restart docker
镜像的操作
docke search 查找镜像 当安装和配置好docker 后在本地上是不存在任何镜像的,这时候就需要去镜像仓库拉取需要的镜像,在拉取之前可以通过查找的操作,来查看所需要的镜像是否在仓库之中.

docker search redis
如果查找到了redis镜像的信息,它会输出一些关于该镜像的信息例如名称,描述,star,是否官方等等,如果没有那么仓库就不存在该镜像需要换一个仓库.

--limit 参数可以进行输出镜像的结果数量限制.一般都是使用官方镜像.

docke pull 拉取镜像

从中央仓库拉取镜像到本地 一般不填 tag 会拉去最新的也就是 latest docker pull 镜像名称[:tag]

#例如
docker pull mongo
查看本地镜像 docker images 还可以再后面加入一些参数 -q 只显示镜像id 默认是-a 列出所有镜像

#输出的格式如下
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
mongo               latest              409c3f937574        5 days ago          493MB
hello-world         latest              bf756fb1ae65        7 months ago        13.3kB
镜像ID就是sha256 的字符串. 下载带有tag的镜像例如redis 6系列版本的镜像

docker pull redis:6.0.8
删除镜像 docker rmi (-f) 镜像ID rm 一般*nix的删除前缀 i就是image的i -f 就是强制删除.当镜像在容器中时则需要-f 强制删除

#例如删除mongo
docker rmi 409c3f937574
#如果要删除多个镜像
docker rmi id1 id2
#删除全部的容器
docker rmi -f $(docker images -qa)
查看docker 镜像容器数据卷的占用信息

docker system df
镜像的导入导出

如果因为网络原因可以通过硬盘的方式传输镜像，虽然不规范，但是有效，但是这种方式导出的镜像名称和版本都是null，需要手动修改

#将本地的镜像导出
docker save -o 导出的文件路径 镜像id
#加载本地的镜像文件
docker load -i 镜像文件
#修改镜像文件
docker tag 镜像id 新镜像名称:版本
例如打包mongo镜像(确保先创建你要导出的文件夹)

docker save -o ~/dockerimage/mongo 409c3f937574
#加载本地镜像
docker load -i ~/dockerimage/mongo
#output 加载镜像的layer
c5ff2d88f679: Loading layer  80.33MB/80.33MB
8a9da272b7d2: Loading layer  340.5kB/340.5kB
1380b7095b41: Loading layer  12.19MB/12.19MB
d1e9c181d71c: Loading layer  3.515MB/3.515MB
4dcad5cb53c6: Loading layer  2.048kB/2.048kB
7e48cf4fe2cc: Loading layer   5.12kB/5.12kB
0e190450333c: Loading layer  3.584kB/3.584kB
b7e89712287a: Loading layer  547.4MB/547.4MB
2d3d91132f03: Loading layer  17.41kB/17.41kB
Loaded image ID: sha256:a440572ac3c10fdc02c51d46a2dcbf3760d10faf3f6a2784054e6e1057f0d92a

#然后docker images 查看一下
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
<none>              <none>              409c3f937574        5 days ago          493MB
hello-world         latest              bf756fb1ae65        7 months ago        13.3kB
这个 none 就是加载的已经打包到本地的mongo ID大小都是一样的. none 这个镜像叫做虚悬镜像(dangling iamge)

修改这个虚悬镜像的name 和tag

docker tag ImageID mongo:latest
#再用docker images查看一下 这样就顺眼了
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
mongo               latest              409c3f937574        5 days ago          493MB
hello-world         latest              bf756fb1ae65        7 months ago        13.3kB
容器操作
运行容器需要定制具体镜像，如果镜像不存在，会直接下载

docker run 镜像的ID|镜像的名称[:tag]
常用的参数

-d(daemon):代表后台运行容器
-p(port):宿主机端口:容器端口：为了映射当前Linux的端口和容器的端口
-P随机端口
-i(interactive): 交互启动
-t(tty): 分配一个伪终端一般与 -i一起使用
--name:容器名称:指定容器的名称
docker run -d -p 宿主机端口:容器端口 --name 容器名称 镜像ID 或者 镜像名称[:tag]

#例如启动mysql 之后会看到容器id的输出即为启动容器成功
docker run -d -p 3309:3306 --name mysql 0d
查看全部正在运行的容器信息

-a 查看全部的容器，包括没有运行
-q 只查看容器的标识
-l 显示最近创建的容器
-n 显示最近n个创建的容器
docker ps [-qa]

#会有这样的输出 当前容器的id
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
d00f6136b0d7        bf                  "/hello"            5 seconds ago       Exited (0) 4 seconds ago                       hopeful_poitras

#只显示最近创建的容器
docke ps -l

#只显示1个创建的容器
docker ps -n 1
退出容器

当以交互式的形式启动容器后 dock run -it ubuntu bash. 会进入到容器的bash中.那么如何退出当前的容器两种办法:

输入exit 会停掉正在运行的容器
快捷键ctrl+p+q 退出.不会停掉容器
查看容器日志，以查看容器运行的信息

-f：可以滚动查看日志的最后几行
docker logs -f 容器id
进入容器的内部进行操作，例如进入容器内部的shell(默认是bash) exec是execute的简写执行的意思。记住单词也就记住了。

docker exec -it 容器id bash
进入后可通过输入exit 退出回到当前的环境,并且不会停掉容器

重新连接容器 docker attach

当通过使用交互式启动容器时例如 docker run -it -d ubuntu bash 时,如上所述我们可以使用exit和快捷键退出容器.那么当我们是用快捷键退出容器后如何在进去呢. 可以使用

docker attach 容器id
#注意这里如果继续使用exit 退出容器仍然会停掉容器
查看容器内部运行的进程

docker top 容器id
打印容器信息

docker inspect 容器id
容器的启动，暂停，停止，删除等操作，后续会经常使用到

#暂停容器
docker pause 容器id
#恢复容器
docker unpause 容器id
#重新启动容器
docker restart 容器id
#启动运行的容器
docker start 容器id
#停止指定的容器
docker stop 容器id
#停止全部容器
docker stop $(docker ps -qa)
#删除指定容器
docker rm 容器id
#删除全部容器 -f 就是force 强制删除可以删除正在运行的容器
docker rm (-f) $(docker ps -qa)
#另一种方式使用管道的形式
docker ps -a -q | xargs docker rm
#强制停止容器
docker kill 容器id
例如删除hello-world容器

#查看到ID
docker ps -a 
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
d00f6136b0d7        bf                  "/hello"            5 seconds ago       Exited (0) 4 seconds ago                       hopeful_poitras
#停止容器
docker stop d00
#删除容器
docker rm d00
#查看一下
docker ps -a
#hello-world 容器已经不存在了
#然后就可以删除掉hello-world镜像
docker rmi hello-wolrd的id即可
#再用docker images查看一下
#没有了hello-world的镜像
当然可以通过使用docker rm -f hello-world 强制删除不过在开发时候为了确保不出意外一般都是先停止在删除.

实例启动mysql容器

#例如docker运行mysql
➜ docker pull mysql
#查看镜像
➜ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
mysql               latest              0d64f46acfd1        3 weeks ago         544MB
#后台运行容器 -e 加上初始化的root密码 否则mysql 会启动失败(可通过logs -f查看到日志)
➜ docker run -d -p 3309:3306 -e MYSQL_ROOT_PASSWORD=123456   --name mysql 0d
#输出容器id 即为启动成功
d20bfc8e2eaf35773a911a8e5e3af8b1bce024a16e7687000d9ef476c4fc3f0e
# 查看当前的容器
➜ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
d20bfc8e2eaf        0d                  "docker-entrypoint.s…"   3 seconds ago       Up 3 seconds        33060/tcp, 0.0.0.0:3309->3306/tcp   mysql
# 进入容器的内部shell环境连接mysqlclient
root@d20bfc8e2eaf:/# mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 8.0.21 MySQL Community Server - GPL

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>

#成功运行了mysql
# 退出mysql
mysql> \q
# 退出容器
root@d20bfc8e2eaf:/# exit
可以通过各种数据库的gui客户端进行连接当前的mysql容器,需要注意的是这个例子中使用主机的3309做为映射端口那么在使用客户端连接的时候切记修改默认的3306端口为3309 端口。当然你也可以使用主机的3306端口映射容器的3306端口在启动容器的时候.

在编程的时候连接数据库 例如go中使用docker的mysql

func main() {
	ConnectSQL("localhost", "3309", "root", "123456", "mysql")
}

// ConnectSQL ...
func ConnectSQL(host, port, uname, pass, dbname string) {
	dbSource := fmt.Sprintf(
		"root:%s@tcp(%s:%s)/%s?charset=utf8",
		pass,
		host,
		port,
		dbname,
	)
	d, err := sql.Open("mysql", dbSource)
	if err != nil {
		panic(err)
	}
	err = d.Ping()
	if err != nil {
		panic(err)
	}
	fmt.Println("Connection success")
}
极大的改善了开发体验，你可以简单有快速的安装不同版本和不同类型的数据库。

容器拷贝文件到主机 docker cp 容器id:容器内路径 目标主机路径

首先启动一个Ubuntu容器,然后进入到这个ubuntu容器中

#启动ubuntu容器
docker run -it ubuntu bash
#目前已经在ubuntu容器内了在任何目录创建一个文件
touch a.txt
#使用重定向的方式写入一些字符串
echo 'from ubuntu' > a.txt
#使用cat命令查看是否写入成功
cat a.txt
#正常情况会输出刚写入的字符串 from ubuntu
#使用ctrl+p+q退出这个容器 前面讲过快捷键不会停掉容器
#使用cp命令把刚才创建的a.txt文件拷贝到当前目录下
docker cp 容器id:/a.txt ./
#通过ls 命令查看存在a.txt文件已经拷贝成功了
#cat a.txt 会输出from ubuntu
导出容器 docker export 容器id > 文件名.tar
#注意导出是不会停掉正在运行的容器的
docker export ubuntu容器id > ubuntu.tar
#ubuntu容器仍然在运行
docker  ps -a
导入容器镜像 cat 镜像.tar | docker import - 镜像用户/镜像名:镜像版本号

#首先强制删除刚才的ubuntu镜像
docker rm -f ubuntu容器id
#查看确认已经没有了ubuntu容器
docker ps -a
#导入刚才导出的ubuntu容器镜像 这里就可以随便写一些信息
cat ubuntu.tar | docker import -test/test:0.1.0
#导入完成后会看到sha256的id输出 使用
docker images
#查看全部的镜像会看到刚导入的镜像li dang
镜像
是一种轻量级，可独立的独立软件包，它包含运行某个应用程序所需的所有内容，把应用程序和配置依赖打包成一个可交付的运行环境，这个打包好的运行环境就简称为镜像

分层镜像

当使用pull命令拉取一个新的镜像时经常看到是这样的输出

docker pull mongo
# output
latest: Pulling from library/mongo
b65bcf19d144: Pulling fs layer
83449d568304: Pulling fs layer
20d982b8a1de: Waiting
40b500d3ec7f: Waiting
在上面的输出中会看到许多的fs layer 文件层,一个镜像是由许多个文件构成的.底层的原理就是 Union fs(联合文件系统).

Union Fs (联合文件系统) 是一种分层,轻量级的高性能文件系统,它支持对文件系统的修改作为一次提交来一层层的叠加.同时可以将不同的目录挂载到通一个虚拟文件系统下. Union文件系统是docker镜像的基础.镜像可以通过分层来继承.基于基础的镜像可以制作各种不同应用的镜像.

特性: 一次同时加载多个文件系统,但从外面看起来,只能看到一个文件系统,联合加载会把各层文件叠加起来,这样最终的文件系统会包含所有底层的文件和目录.

Docker镜像加载原理
docker的镜像实际上由一层一层的文件系统组成,这种层级的文件系统叫做UnionFs.

bootfs(boot file system)主要包含bootloader和kernel, bootloader主要是加载kernel,linux刚启动的时候会加载bootfs文件系统,在docker镜像的最底层就是引导文件系统bootfs.这一层与典型的linux或者unix系统是一样的. 当boot加载完成之后整个内核就在内存中了,此时的内存使用权就由boot转交给了kernel,此时系统也会卸载bootfs

rootfs(root file system)在bootfs之上,包含的就是典型的linux或者unix系统中的/dev /proc /bin /etc等标准目录和文件, rootfs就是各种不同操作系统的发行版例如ubuntu centos 等等.

镜像提交
docker commit -m=“提交的信息” -a=“作者” 容器id 要创建的镜像名:tag

之前创建的ubuntu容器使用的官方镜像.这种镜像一般只包含一个linux kernel没有其他任何常用的一些外部程序例如vim等. 尝试安装一个vim然后提交打包这个ubuntu容器成为一个新的带有vim的ubuntu镜像.

ubuntu的包管理器使用的是apt-get。所以先尝试更新下包管理器

#更新
docker run -it ubuntu bash
apt-get update
#安装vim
apt-get -y install vim
#安装完成后打开vim测试一下都正常的.提交这个镜像 用户名要与hub.docker上面一致
docker commit -m="ubuntu with vim" -a="glepnir" 3730 glephunter/myubuntu:0.1.0
#提交镜像到hub.docker去
docker push glephunter/myubuntu:0.1.0
Docker Registry 私服
一般企业内部会因为私密性等原因创建自己的本地docker 镜像服务器.那么就可以使用docker registry.

首先需要拉取registry镜像通过

#拉取registry镜像
docker pull registry
在本地创建一个私有的镜像服务器dockerhub需要用到的命令

docker run -d -p 5000:5000 -v ~/Workspace/dockerlearn/:/tmp/registry --privileged=true registry
为了测试是否成功搭建并且可以正常推送Docker镜像到这个服务器. 魔改一个ubuntu镜像

#启动一个ubuntu镜像
docker run -it ubuntu bash
#安装vim
apt-get update
apt-get install -y vim
镜像修改成功后，通过curl查询私服上的镜像列表

curl -XGET http://127.0.0.1:5000/v2/_catalog
因为什么都没上传过所以是空的。然后上传魔改后的自己的ubuntu镜像.先通过docker tag修改一下镜像名称为私服地址/镜像名称:版本号

docker tag vimubuntu:0.1.0 127.0.0.1:5000/vimubuntu:0.1.0
修改配置docker的配置文件 linux下是/etc/docker/daemon.json 添加私服的ip地址

{
  "insecure-registers": ["ip address:port"]
}
当docker挂在主机目录访问如果出现permission denied提示权限不够时需要加上 --privileged = true

数据卷
为什么要用数据卷因为镜像往往都是很纯净的甚至都没有vi，还需要去下载一个vi才能使用。如果使用docker部署不推荐在容器内部维护项目。

数据卷：将宿主机的一个目录映射到容器的一个目录中。可以在宿主机中操作目录中的内容，那么容器内部映射的文件，也会跟着一起改变。

通过-v 本机目录:容器目录:rw参数将本机目录同步挂载到容器。读写权限默认是rw所以可以写也可以不写.

创建数据卷后，默认会存放在一个目录下/var/lib/docker/volumes/数据卷名称/_data

docker volume create 数据卷名称

#创建一个go微服务数据卷
➜ docker volume create go-microservices
go-microservices
# 查看数据卷
➜ docker volume ls
DRIVER              VOLUME NAME
local               3e1a82bbf69dc086edf161d5f5737c108d82f04a1c07fa24be77a48d6f7bd0de
local               55f0f0294ae7096d461ffc0319c8e52064856d18ce9ceb194794d39420b2c76a
local               460487207e610918020e8435d071e6127c98f33eb0292433a38a8c8bedaf4f38
local               dd189a79766f32b8da90ff16a7cc4bf97ef662fcd9387e322232cd60de791a36
local               go-microservices
查看全部数据卷信息

docker volume ls
#查看数据卷的详细信息，可以查询到存放的路径，创建时间等等
docker volume inspect 数据卷名称
删除指定的数据卷

docker volume rm 数据卷名称
容器映射数据卷通过数据卷名称映射，如果数据卷不存在。Docker会帮你自动创建，会将容器内部自带的文件，存储在默认的存放路径中。

docker run -v 数据卷名称:容器内部的路径 镜像id

#通过路径映射数据卷，直接指定一个路径作为数据卷的存放位置。但是这个路径下是空的。手动添加内容，推荐这种方式
docker run -v 路径(/root/自己创建的文件夹):容器内部的路径 镜像id
容器卷之间的继承 --volumes-from Parent

# 启动一个ubuntu容器 名字是ubuntu-1
docker run -it --privileged=true -v ~/dockerdata/u:/tmp/u --name ubuntu-1 bash
# 进入到容器后创建一个测试文件a.txt
cd /tmp/u
touch a.txt
echo 'from docker' > a.txt
启动第二个容器将ubuntu-1的数据卷挂载到第二个容器上

docker run -it --privileged=true --volumes-from ubuntu-1 --name ubuntu-2 ubuntu bash
这样就让第二个容器使用了来自ubuntu-1的数据卷

# 进入第二个容器ubuntu-2之后进入tmp/u下查看是否有a.txt文件
cd /tmp/u
ls
# 此时就会看到a.txt 通过cat查看文件的内容
此时的容器ubuntu-2和ubuntu-1公用一个数据卷/dockerdata/u 当我们在容器2中创建文件同样也会同步到容器1中.

# 在容器ubunut-2中创建一个b.txt
touch b.txt
echo 'this if from ubuntu-2' > b.txt
# 输入ctrl+p+q 退出容器ubuntu-2
docker attach ubuntu-1的容器id
# 查看是否存在b.txt
cd /tmp/u
# 使用ls并用cat打印b.txt
Dockerfile自定义镜像
创建自定义镜像就需要创建一个Dockerfiler,如下为Dockerfile的语言

from：指定当前自定义镜像依赖的环境
copy：将相对路径下的内容复制到自定义镜像中
workdir：声明镜像的默认工作目录
run：执行的命令，可以编写多个
cmd：需要执行的命令（在workdir下执行的，cmd可以写多个，只以最后一个为准）
生成镜像

#编写完Dockerfile后需要通过命令将其制作为镜像，并且要在Dockerfile的当前目录下，之后即可在镜像中查看到指定的镜像信息
# 点意味着生成在当前目录下
docker build -t 镜像名称[:tag] .
DockerCompose
以上面的方式运行一个容器需要添加许多参数。为了更加的方便使用Docker-Compose编写配置文件把参数写进去。 Docker-Compose也可以批量的管理容器所以你只需要编写并维护一个docker-compose.yaml文件即可 地址 docker-compose,可以在github的release下载已经打包好的

Linux 环境
下载好docker-compose然后将DockerCompose文件的名称修改一下，给予DockerCompose文件一个可执行的权限

mv docker-compose-Linux-x86_64 docker-compose
chmod 777 docker-compose
#方便后期操作，配置一个环境变量
#将docker-compose文件移动到了/usr/local/bin，修改了/etc/profile文件，给/usr/local/bin配置到了PATH中

mv docker-compose /usr/local/bin
vi /etc/profile
#添加内容：export PATH=/usr/local/bin:$PATH
source /etc/profile
#测试
docker-compose -v
Mac 下如果你安装过了docker for mac app就可以直接使用了
DockerCompose 管理
编写docker-compose.yml文件yml文件以key:value方式来指定配置信息 多个配置信息以换行+缩进的方式来区分在docker-compose.yml文件中，不要使用制表符

version: '3.1'
services:
  mysql:           # 服务的名称
    restart: always   # 代表只要docker启动，那么这个容器就跟着一起启动
    image: daocloud.io/library/mysql:5.7.4  # 指定镜像路径
    container_name: mysql  # 指定容器名称 docker ps 看到的名称
    ports:
      - 3309:3306   #  指定端口号的映射
    environment:
      MYSQL_ROOT_PASSWORD: root   # 指定MySQL的ROOT用户登录密码
      TZ: Asia/Shanghai        # 指定时区
    volumes:
     - ~/docker_mysql/mysql_data:/var/lib/mysql   # 映射数据卷
  go:
    restart: always
    image: go:1.14.7
    container_name: go
    ports:
      - 8080:8080
    environment:
      TZ: Asia/Shanghai
    volumes:
      #填数据卷
  #如果还有镜像容器可以一直往下写
DockerCompose 命令
在使用docker-compose的命令时，默认会在当前目录下找docker-compose.yml文件
 
#1.基于docker-compose.yml启动管理的容器
docker-compose up -d
 
#2.关闭并删除容器
docker-compose down
 
#3.开启|关闭|重启已经存在的由docker-compose维护的容器
docker-compose start|stop|restart
 
#4.查看由docker-compose管理的容器
docker-compose ps
 
#5.查看日志
docker-compose logs -f
DockerCompos配合Dockerfile一起使用
docker-compose配合Dockerfile使用，就可以使用docker-compose管理自定义的镜像，它会帮你build然后启动。更加方便

version: '3.1'
services:
  ssm:
    restart: always
    build:            # 构建自定义镜像
      context: ../      # 指定dockerfile文件的所在路径
      dockerfile: Dockerfile   # 指定Dockerfile文件名称
    image: your_image_name:1.0.1 #指定你镜像的名称和版本
    container_name: 容器名称
    ports:
      - 8081:8080
    environment:
      TZ: Asia/Shanghai
运行

#可以直接基于docker-compose.yml以及Dockerfile文件构建的自定义镜像
docker-compose up -d
# 如果自定义镜像不存在，会自动构建出自定义镜像，如果自定义镜像已经存在，会直接运行这个自定义镜像
#重新构建自定义镜像
docker-compose build
#运行当前内容，并重新构建
docker-compose up -d --build
DOCKER
