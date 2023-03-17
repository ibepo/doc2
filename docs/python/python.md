查看 python 的安装路径

```
python -m site
```

查看 pip 本地安装的依赖包列表

```shell
pip list
```

with关键字
下面是一个使用“with”关键字和“open”函数打开文件并指定写入模式的示例：

Copy code
with open("example.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is an example file.\n")
    f.write("It is used to demonstrate file I/O in Python.\n")
在这个例子中，我们打开了一个名为“example.txt”的文件，它处于写入模式。“with”关键字在代码块结束时自动关闭文件，从而防止意外的文件句柄泄漏，并在写入完所有数据后刷新缓冲区。然后使用“write”方法向文件中写入三个字符串。 注意，在这个例子中，“write”方法不会自动添加换行符。因此，每个字符串后都要加了“\ n”以手动添加换行符。
参考：
https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python
https://pep8.org/
talk about image in python
https://www.youtube.com/watch?v=LGYOgJWCINM
https://pillow.readthedocs.io/en/stable/handbook/concepts.html
