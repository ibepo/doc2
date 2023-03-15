```shell
yay -S clash-for-windows-bin
```

## 本机的配置地址
`$HOME/dockerVolume/clash:/root/.config/clash`

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
#本机的方式(和上边只是配置位置不同)
docker run -d --name=clash --network=host -v "$HOME/dockerVolume/clash:/root/.config/clash" dreamacro/clash
```

## 参考
https://zhuanlan.zhihu.com/p/423684520
https://akynazh.site/posts/2023/01/clash-linux-configuration-usage-record/
https://zhuanlan.zhihu.com/p/402481568?utm_medium=social&utm_oi=31231790022656&utm_id=0
https://akynazh.site/posts/2023/01/clash-linux-configuration-usage-record/
