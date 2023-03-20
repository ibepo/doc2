## clash本地部署
```shell
yay -S clash-for-windows-bin
```


## clash容器部署 
```shell
docker pull dreamacro/clash
docker run --name Clash -d -v ~/clash/config.yaml:/root/.config/clash/config.yaml --network="host" --privileged dreamacro/clash
```

```shell
#本机的方式(和上边只是配置位置不同)
docker run -d --name=clash --network=host -v "$HOME/dockerVolume/clash:/root/.config/clash" dreamacro/clash
```

## 获取订阅链接并配置
1. `$HOME/dockerVolume/clash:/root/.config/clash`
2. 导入自己的飞机配置，这里从相关网站，**选择下拉选择clash协议**，获取订阅地址`link`

```shell
cd $HOME/dockerVolume/clash:/root/.config/clash
wget -O config.yaml link
```

## 部署可视化clash dashboard容器
```shell
docker pull haishanh/yacd
docker run -p 1234:80 -d haishanh/yacd
```

## 参考
https://zhuanlan.zhihu.com/p/423684520
https://akynazh.site/posts/2023/01/clash-linux-configuration-usage-record/
https://zhuanlan.zhihu.com/p/402481568?utm_medium=social&utm_oi=31231790022656&utm_id=0
https://akynazh.site/posts/2023/01/clash-linux-configuration-usage-record/
[Fetching Title#ihcq](https://github.com/Dreamacro/clash/wiki/configuration#introduction)