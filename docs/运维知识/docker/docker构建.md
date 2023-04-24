## build java服务 

```shell
#dockfile
FROM openjdk:11
ADD ./app /usr/local/bsbdj
WORKDIR /usr/local/bsbdj 
CMD ["java","‐jar", "bsbdj.jar"]
```

comg soon...

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

## 整体解决方案，最佳实践 
ngnix+三个后端服务一键式部署:
![[Pasted image 20230317092157.png]]

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