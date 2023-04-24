# Git 配置多个 ssh key

有时，您需要多个帐户才能访问Github或Gitlab以及类似工具。例如，您可以在家/github上为您的项目创建一个帐户，为您的公司/gitlab拥有第二个帐户。

有时您需要多个帐户才能访问 Github 或 Gitlab 和类似工具。例如，您可以在 home/github 上为您的项目设置一个帐户，在您的公司/gitlab 上设置第二个帐户。

## 生成第一个密钥

```
ssh-keygen -t rsa -C "youremail@example.com"
```

当您看到此消息时

```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user_name/.ssh/id_rsa):
```

输入唯一名称，例如：

```
id_rsa_gitlab
```

接下来，系统会要求您输入密码。

因此，您已经为您的家庭/ github帐户创建了SSH密钥，现在您可以为您的公司/ gitlab帐户生成SSH密钥。

## 生成第二个密钥

使用第二封邮件再次调用 SSH 密钥生成器。

```
ssh-keygen -t rsa -C "your_another_email@example.com"
```

输入 github 的名称

```
id_rsa_github
```

完成所有步骤后，您可以检查是否已创建所有密钥。

```
$ ls ~/.ssh
```

您应该会看到类似的文件列表：

```
id_rsa_gitlab id_rsa_github id_rsa_gitlab.pub id_rsa_github.pub
```

## 创建配置文件

现在你需要一个配置文件来组织这些键。在下创建一个文件`config``~/.ssh/`

```
$ vim config
```

将以下内容添加到配置文件：

```
#gitlab
Host gitlab.com
  HostName gitlab.com
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/id_rsa_gitlab

#github
Host github.com
  HostName github.com
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/id_rsa_github
```

## 检查连接

接下来您可以检查连接

```
$ ssh -T git@github.com
Hi einverne! You've successfully authenticated, but GitHub does not provide shell access.

$ ssh -T git@gitlab.com
Welcome to GitLab, Ein Verne (einverne)!
```

到目前为止，一切似乎都很好。

## 问与答

问题 1.一个 SSH 密钥可以推送到不同的 Git 远程吗？

是的，假设您在所有开发工作站上使用一个或以其他方式命名的公钥以及您的私钥，那么只需将该公钥上传到多个 Git 主机即可获得与当前从多个密钥获得的相同访问权限。 这也将使您的生产生活变得有点`id_rsa.pub`容易，而无需管理多个密钥，并确保每次与服务器. 如果您使用多个工作站（即家庭和办公室），您还可以选择在每个本地工作站上使用相同的公钥/私钥对。这进一步减少了您需要跟踪的不同密钥的数量。

问题 2.我们必须为不同的远程生成多个SSH密钥的目的是什么服务器?

没有理由必须为多个远程 Git 存储库服务器生成多个密钥，如第一个问题的答案所示。 正如 Jan Hudec 所提到的，人们可能选择对不同的 Git 存储库使用不同密钥的原因是为了附加安全层或管理控制层。

问题 3.如果遇到权限问题，可能是新建的 config 文件权限问题

```
ssh -T git@gitlab.com
Bad owner or permissions on /home/einverne/.ssh/config
```

比如遇到上述问题，需要修改一下 config 文件权限

```
chmod 600 ~/.ssh/config
chown $USER ~/.ssh/config

```

## 参考
[Fetching Title#t6iw](https://einverne.github.io/post/2015/08/git-with-multi-ssh-key.html)