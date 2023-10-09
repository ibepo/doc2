## Swfit学习

[chaocode 油管](https://www.youtube.com/@ChaoCode)
[chaocode b站](https://www.bilibili.com/video/BV1fS4y1b7h9/?spm_id_from=333.999.0.0&vd_source=b92112731015c20054034d26c9ad8a67)
[b站 实操SwfitUI](https://www.bilibili.com/video/BV1uj411k74e/?spm_id_from=333.999.0.0)
[kavsoft 油管](https://www.youtube.com/@Kavsoft)
[mastering-swiftui 土拨鼠购买的放到gitbook上的电子书](https://ylqylq001.github.io/Mastering-SwiftUI/)

[ Swift 100](https://www.hackingwithswift.com/100/swiftui)
[swiftui thinking](https://www.youtube.com/watch?v=-Yp0LS61Nxk)
[swift basic](https://www.youtube.com/watch?v=PwXgg9adkdM)

## 宣传平台
[producthunt](https://www.producthunt.com/)
[Indie Hackers](https://www.indiehackers.com/)
[一个海外的分析kit](https://superwall.com/?ref=twitter_link_2_follow_la&twclid=28a0fekf9h3pjy08qsxikh3hv)

## app销量分析
[点点数据](https://app.diandian.com/)

## apple 开发者网页 
[App Store Connect](https://appstoreconnect.apple.com/login?targetUrl=%2Fanalytics%2Fapp&authResult=FAILED)
[Apple developer](https://developer.apple.com/)
[Swfit Api](https://developer.apple.com/documentation/imageio/cgimagesource)
[github上一位放电子书的大佬](https://github.com/henryhu712/Developer-Books/tree/master/JavaScript)
[wwdc 关于LiveText的部分 visionKit](https://developer.apple.com/videos/play/wwdc2022/10025/)
[All Video in developer apple](https://developer.apple.com/videos/all-videos/)

## Swift高级特性
### 高阶 函数
### Optional
``` Swift
var str : String?
var str : Optional<String>

str = "123123"
str = nil

print(str!)
print(type(of : str))


//避免str！ 脱开错误的方法

if let newStr=str{
	print(str!)
	print(type(of:(str!)))
} else {
	print("stl is nil")
}

```
有的时候并不是之使用自己产生而资料，有的资料是从网路获取而来的
[[iOS][Swift][中文] 基礎語法#12. 初探Optional](https://www.youtube.com/watch?v=6Dd6_wjvEkA)
### Closeture
#### 尾闭包的应用
在 Swift 中，尾闭包（Trailing Closure）是一种特殊的闭包语法，用于在函数调用中以更简洁的方式传递闭包参数。通常，闭包作为函数的最后一个参数传递给函数，但是使用尾闭包语法，可以将闭包参数写在函数调用的括号外面，使代码更易读。

尾闭包的语法格式如下：

```swift
func someFunction(argument1: Int, argument2: String, closure: () -> Void) {
    // 函数体
}

someFunction(argument1: 10, argument2: "Hello") {
    // 尾闭包的代码
}
```

在上面的例子中，`someFunction` 是一个接受一个整数参数和一个字符串参数的函数，并且接受一个闭包作为最后一个参数。使用尾闭包语法，我们可以将闭包参数写在函数调用的括号外面，使代码更清晰。

尾闭包的优势在于，它可以将闭包的逻辑与函数调用的参数列表分开，使代码更易读和维护。特别是在闭包的代码比较长或复杂时，尾闭包可以提高代码的可读性。

需要注意的是，尾闭包只能在函数调用时使用，而不能在其他地方单独使用。另外，如果函数除了尾闭包外还有其他参数，尾闭包必须是函数参数列表中的最后一个参数。
## SwiftUI
