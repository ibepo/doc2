### 关键词

- 感知机
- 阶跃函数
- weight(权重)
- bias(偏差) ,也可以理解为基础兴奋值
- perceptron as a NAND Gate(与非门)
- linear classifier(线性分类器)
- sigmoid funciton（S函数）

```

Sigmoid函数是一种数学函数，可以将任意范围的实数映射到0到1之间的值范围内。它常用于人工神经网络中作为激活函数。最常用的Sigmoid函数是逻辑函数，其形式如下：

f(x) = 1 / (1 + e^-x)

其中x为任意实数。

Sigmoid函数具有“S”形曲线，意味着当输入x从负无穷逐渐增大到正无穷时，函数值从0逐渐增大到1。函数在x=0处拐点，曲线的斜率在拐点处最陡峭，并逐渐在极端的x值处变得较平缓。

Sigmoid函数的一些特性包括：

它是一个连续和可微的函数
它是非线性的，这使得它适用于建模变量之间的复杂关系
它可以将任何输入范围转换为0到1之间的输出范围，这可以解释为概率得分或置信度测量。

```

### 参考

https://www.bilibili.com/video/BV1gA4y1Q7Kj/?spm_id_from=333.337.search-card.all.click&vd_source=b92112731015c20054034d26c9ad8a67
[Sigmoid Function clearly explain](https://www.youtube.com/watch?v=TPqr8t919YM)