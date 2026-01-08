### Subscribe
```shell
mqttx sub -t 'mqttx/cli' -h 'broker.emqx.io' -p 1883
mqttx sub -t '/client/product/704A0E261897/running/info' -h 'mqtt-ws.lhehs.com' -p 443 

```

### publish
```shell
mqttx pub -t 'mqttx/cli' -h 'broker.emqx.io' -p 1883 -m 'hello ibepo!'
```

### 参考
https://mqttx.app/docs/cli/get-started#connection
https://www.emqx.com/zh/blog/powerful-and-easy-to-use-mqtt-5-command-line-tool