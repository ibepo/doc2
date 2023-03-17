## Nginx

### 安装

```bash
/usr/local/nginx/sbin/nginx #启动 nginx
/usr/local/nginx/sbin/nginx -s reload ##重新加载Nginx配置文件，然后以优雅的方式重启Nginx
/usr/local/nginx/sbin/nginx -s stop #强制停止Nginx服务

nginx -t #检测配置文件是否有语法错误，然后退出
```
![[Pasted image 20230317085850.png]]


### 配置

```nginx
#nginx.conf
user  nobody;
worker_processes  1;

events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;


# root是定位到服务器真实目录的一个目录作为初始目录 再加上location中的目录
# 比如 root是/panghu/s,这个作为basepath+location中的/s/,那么访问localhost/s/,就能访问到该目录下
# 一个server中的优先级是正则表达式>深路径>浅路径
    server {
        server_tokens off;
        listen       80;
        server_name  localhost;
        location  / {
            root   /panghu/work/h5;
            index  index.html index.htm;
        }
        location /s/{
                 root   /panghu/work
                 index  index.html index.htm;
        }
                #location ~\.(gif|jpg|png){
                #   # root   /panghu/work/s;
                #}
    }

}
```



```shell
# Nginx配置文件
/etc/nginx/nginx.conf # nginx 主配置文件
/etc/nginx/nginx.conf.default

# 可执行程序文件
/usr/bin/nginx-upgrade
/usr/sbin/nginx

# nginx库文件
/usr/lib/systemd/system/nginx.service # 用于配置系统守护进程
/usr/lib64/nginx/modules # Nginx模块目录

# 帮助文档
/usr/share/doc/nginx-1.16.1
/usr/share/doc/nginx-1.16.1/CHANGES
/usr/share/doc/nginx-1.16.1/README
/usr/share/doc/nginx-1.16.1/README.dynamic
/usr/share/doc/nginx-1.16.1/UPGRADE-NOTES-1.6-to-1.10

# 静态资源目录
/usr/share/nginx/html/404.html
/usr/share/nginx/html/50x.html
/usr/share/nginx/html/index.html

# 存放Nginx日志文件
/var/log/nginx

```

```shell
# 开机配置
systemctl enable nginx # 开机自动启动
systemctl disable nginx # 关闭开机自动启动

# 启动Nginx
systemctl start nginx # 启动Nginx成功后，可以直接访问主机IP，此时会展示Nginx默认页面

# 停止Nginx
systemctl stop nginx

# 重启Nginx
systemctl restart nginx

# 重新加载Nginx
systemctl reload nginx

# 查看 Nginx 运行状态
systemctl status nginx

# 查看Nginx进程
ps -ef | grep nginx

# 杀死Nginx进程
kill -9 pid # 根据上面查看到的Nginx进程号，杀死Nginx进程，-9 表示强制结束进程


```



### 参考

[前端仔也需要懂的nginx内容](https://juejin.cn/post/7007346707767754765)

[Nginx 的 try_files 指令使用实例 ](https://www.hi-linux.com/posts/53878.html)

[前端部署演化史.op-note/deploy-fe.md at master · shfshanyue/op-note (github.com)](https://github.com/shfshanyue/op-note/blob/master/deploy-fe.md)

[使用apt-get安装Nginx - 快乐的凡人721 - 博客园 (cnblogs.com)](https://www.cnblogs.com/luo630/p/9363478.html)

[万字总结，体系化带你全面认识 Nginx ！ - 掘金 (juejin.cn)](https://juejin.cn/post/6942607113118023710)
