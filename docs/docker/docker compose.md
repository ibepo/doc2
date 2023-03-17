### 概述 

docker-compose的完整命令的用法是：
`docker-compose [-f <arg>...] [options] [COMMAND] [ARGS...]` 
主要分为2段，一是options，二是COMMAND。

常用options有：
- `-f, --file FILE` 指定使用的 Compose 模板文件，默认为 `docker-compose.yml`，可以多次指定。
- `-p, --project-name NAME` 指定项目名称，默认将使用所在目录名称作为项目名。
- `--verbose` 输出更多调试信息。
- `-v, --version` 打印版本并退出。
- `--env-file PATH`设置环境变量

### 常用命令
-  `docker-composse build`：构建（重新构建）项目中的服务容器。
- `docker-compse config`：验证 Compose 文件格式是否正确，若正确则显示配置，若格式错误显示错误原因。
- `docker-compose down`：此命令将会停止 `up` 命令所启动的容器，并移除网络
- `docker-compose exec service名称 COMMAND`：进入指定的容器。
- `docker-compose images`：列出 Compose 文件中包含的镜像。
- `docker-compose logs <service名称>`：查看服务容器的输出。默认情况下，docker-compose 将对不同的服务输出使用不同的颜色来区分。可以通过 `--no-color` 来关闭颜色。
- `docker-compose scale`：通过`service=num` 设置指定服务运行的容器个数。如`docker-compose scale web=3 db=2`
- `docker-compose  up`：将尝试自动完成包括构建镜像，（重新）创建服务，启动服务，并关联服务相关容器的一系列操作。大部分时候都可以直接通过该命令来启动一个项目。默认情况，

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
