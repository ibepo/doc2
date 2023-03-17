
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