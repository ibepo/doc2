https://zhuanlan.zhihu.com/p/423684520

## 部署可视化clash dashboard容器
```shell

docker pull haishanh/yacd
docker run -p 1234:80 -d haishanh/yacd

```

## 部署clash容器
```shell
docker pull dreamacro/clash
docker run --name Clash -d -v ~/clash/config.yaml:/root/.config/clash/config.yaml --network="host" --privileged dreamacro/clash
```

```shell
docker run -d --name=clash --network=host -v "$HOME/dockerVolume/clash:/root/.config/clash" dreamacro/clash
```