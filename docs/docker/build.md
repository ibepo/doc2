## build 

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