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
#### 命令
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

​￼- up：将尝试自动完成包括构建镜像，（重新）创建服务，启动服务，并关联服务相关容器的一系列操作。大部分时候都可以直接通过该命令来启动一个项目。默认情况，

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