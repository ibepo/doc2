## np.vstack

`np.vstack` 是NumPy中的一个函数，它会将一组数组在垂直方向（按行）合并。它的输入参数是一个数组组成的元组或列表，输出是一个包含所有输入数组的垂直合并的新数组。

``` python
import numpy as np
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
# 将 x 和 y 垂直堆叠 
z = np.vstack((x, y))
print(z)
-----------------------------
[[1 2 3]
 [4 5 6]]
```

在这个例子中，`np.vstack((x, y))` 就是将 `x` 和 `y` 按垂直方向堆叠，生成一个新的数组 `z`，其中每行分别包含了 `x` 和 `y` 的元素值。

## np.unique 
可以使用numpy中的unique和unique函数来进行去重和统计各个元素出现次数的操作。

假设有一个numpy数组a，我们可以使用以下代码进行去重和记录操作：
```python

import numpy as np

# 创建一个包含重复元素的数组
a = np.array([1, 2, 3, 1, 2, 4, 5, 3, 2, 6, 1])

# 使用unique函数获取唯一值
unique_values = np.unique(a)
print("数组a中的唯一值为：", unique_values)

# 使用unique函数获取唯一值及其出现次数
unique_values, counts = np.unique(a, return_counts=True)
print("数组a中各元素及其出现次数为：")
for i in range(len(unique_values)):
    print(unique_values[i], "出现了", counts[i], "次。")

-------------------

数组a中的唯一值为： [1 2 3 4 5 6]
数组a中各元素及其出现次数为：
1 出现了 3 次。
2 出现了 3 次。
3 出现了 2 次。
4 出现了 1 次。
5 出现了 1 次。
6 出现了 1 次。
```

可以看到，使用numpy的unique和unique函数可以方便地进行数组去重和元素出现次数的记录。