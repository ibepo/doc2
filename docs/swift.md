## Swfit学习

[chaocode 油管](https://www.youtube.com/@ChaoCode)
[chaocode b站](https://www.bilibili.com/video/BV1fS4y1b7h9/?spm_id_from=333.999.0.0&vd_source=b92112731015c20054034d26c9ad8a67)
[b站 实操SwfitUI](https://www.bilibili.com/video/BV1uj411k74e/?spm_id_from=333.999.0.0)
[kavsoft 油管](https://www.youtube.com/@Kavsoft)
[mastering-swiftui 土拨鼠购买的放到gitbook上的电子书](https://ylqylq001.github.io/Mastering-SwiftUI/)

[ Swift 100](https://www.hackingwithswift.com/100/swiftui)
[swiftui thinking](https://www.youtube.com/watch?v=-Yp0LS61Nxk)
[swift basic](https://www.youtube.com/watch?v=PwXgg9adkdM)
[SwiftUI b站丰原天下](https://www.bilibili.com/video/BV12A4y1R73K/?spm_id_from=333.337.search-card.all.click&vd_source=b92112731015c20054034d26c9ad8a67)
[Swift语言解释](https://www.swift.org/documentation/)
[README - SwiftGG](https://swiftgg.gitbook.io/swift)
[属性 - SwiftGG](https://gitbook.swiftgg.team/swift/swift-jiao-cheng/10_properties)
[iOS新知/ 掘金](https://juejin.cn/user/2234652427553742)
[Learning SwiftUI | Apple Developer Documentation](https://developer.apple.com/tutorials/swiftui-concepts#app-principles)
[Maintaining the adaptable sizes of built-in views | Apple Developer Documentation](https://developer.apple.com/tutorials/swiftui-concepts/maintaining-the-adaptable-sizes-of-built-in-views)
[一个闪屏展示效果](https://github.com/lascic/UIOnboarding)
## 宣传平台
[producthunt](https://www.producthunt.com/)
[Indie Hackers](https://www.indiehackers.com/)
[一个海外的分析kit](https://superwall.com/?ref=twitter_link_2_follow_la&twclid=28a0fekf9h3pjy08qsxikh3hv)

## app销量分析
[点点数据](https://app.diandian.com/)

## 点子
- double clip 翻动iphone屏幕
- <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Here&#39;s what&#39;s happening today in design: <a href="https://t.co/1o1bm4aSoR">pic.twitter.com/1o1bm4aSoR</a></p>&mdash; Cole (@colderoshay) <a href="https://twitter.com/colderoshay/status/1711396106850967621?ref_src=twsrc%5Etfw">October 9, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 实时动态的发生的事

## 有趣的app
[通过截图提取社交信息等支持导出](https://apps.apple.com/us/app/username-screenshot-livelink/id1570152672)
 - 截图功能
 - ocr识别
 - coreml
 - 数据训练集合
 - gridlayout
 - 点击跳转到相关页面
 
 [Mind Depot on the Mac App Store](https://apps.apple.com/us/app/mind-depot/id6452800893)

## apple 开发者网页 
[App Store Connect](https://appstoreconnect.apple.com/login?targetUrl=%2Fanalytics%2Fapp&authResult=FAILED)
[Apple developer](https://developer.apple.com/)
[Swfit Api](https://developer.apple.com/documentation/imageio/cgimagesource)
[github上一位放电子书的大佬](https://github.com/henryhu712/Developer-Books/tree/master/JavaScript)
[告诉我同值多选xcode快捷键的小哥的网站swfit](https://swiftsenpai.com/development/lottie-advance-animation-playback/)
[wwdc 关于LiveText的部分 visionKit](https://developer.apple.com/videos/play/wwdc2022/10025/)
[All Video in developer apple](https://developer.apple.com/videos/all-videos/)
[ios版本分布](https://mixpanel.com/trends/#report/ios_frag/)
[关于ios内购](https://www.revenuecat.com/blog/engineering/ios-in-app-subscription-tutorial-with-storekit-2-and-swift/)
[网易云音乐 iOS 14 小组件实战手册 - 掘金](https://juejin.cn/post/6887759096506744840?searchId=2023101812495719429A6F21A94D8FC73F)
## Swift高级特性
### basic
#### 字符串插值
在Swift中，使用反斜杠（\）和圆括号（()）来进行字符串插值。字符串插值是一种将常量、变量、表达式或者字面量插入到字符串字面量中的方式，以便于在字符串中包含变量或表达式的值。
在给定的代码示例中，(名字) 是一个字符串插值的语法，其中名字是一个变量或常量，它会被替换为其对应的值。所以，当执行 `print("\(名字)：旺旺～")` 时，会将名字的值插入到字符串字面量中，输出类似于 "某个名字：旺旺～" 的结果。
### struct
#### mutating
```
struct Dog{
var 名字 ： String
var 年纪 = 0
let 品种 ： String
func 叫（）{
	print("\(名字)：旺旺～")
}

}
```




### 高阶函数
### Optional
有的时候并不是之使用自己产生而资料，有的资料是从网路获取而来的
这个时候数据有可能是确定值，有可能是nil
####  强制解包（Force Unwrapping）

``` Swift
//非闭包的写法
var str : String?
var str : Optional<String>

str = "123123"
str = nil

if str != nil {
	print(str!) // 强制解包 
    print(type(of: str!)) 
} else { 
	 print("str is nil") 
}

//通过惊叹号进行了强制解包
```

#### 可选绑定（Optional Binding）
``` Swift
//完整的闭包写法
var str : String?
var str : Optional<String>

str = "123123"
str = nil

print(str!)
print(type(of : str))


if let newStr=str{
	print(newStr)
	print(type(of:(newStr)))
} else {
	print("stl is nil")
}

// if let newStr=str 是可选绑定的语法,用于判断str是否为可选类型，
// 并将其解包赋值给newStr,如果str不为nil,进入if语法块，否则进入else语法块

```
在这段代码中，`str` 后面的大括号 `{}` 表示一个闭包（Closure）。闭包是一种自包含的函数代码块，可以在代码中被传递和使用。

在这个特定的代码中，大括号内的闭包用于定义 `if let` 语句块的内容。闭包内部的代码会在 `str` 不为 `nil` 时执行。这种用法常见于 Swift 中的可选绑定，可以在 `if let` 或 `guard let` 语句中使用闭包来处理可选类型的值。

闭包的语法由大括号 `{}` 包围，可以包含参数列表、返回类型和函数体。在这个代码中，闭包没有参数列表和返回类型，只有一个函数体。


#####  guard let 和 if let
`guard let` 语句用于在代码块中进行可选绑定，并在绑定失败时执行特定的代码块。它的语法如下：

```swift
guard let constantName = optionalExpression else {
    // 当 optionalExpression 为 nil 时执行的代码
    // 通常是提前退出或处理错误的逻辑
    // return 或者抛出异常等
}
// 当 optionalExpression 不为 nil 时执行的代码
// 可以使用 constantName
```

`guard let` 语句与 `if let` 语句类似，都是用来处理可选类型的值。但是它们有一些区别：

- `guard let` 通常用于提前退出函数或方法，以避免嵌套过多的代码块。
- `guard let` 必须在代码块的开头使用，而 `if let` 可以在任何地方使用。
- `guard let` 必须有一个与可选类型绑定的常量或变量，并且在绑定失败时执行特定的代码块。
- `guard let` 语句的代码块结束后，绑定的常量或变量在后续代码中仍然可用。

以下是一个使用 `guard let` 语句的示例：

```swift
func processString(str: String?) {
    guard let newStr = str else {
        print("str is nil")
        return
    }
    // 当 str 不为 nil 时执行的代码
    print(newStr)
    print(type(of: newStr))
}

processString(str: "Hello, World!") // 输出: Hello, World!，String
processString(str: nil) // 输出: str is nil
```

在上面的示例中，`guard let` 语句用于检查传入的 `str` 是否为 `nil`。如果 `str` 为 `nil`，则会打印 "str is nil" 并提前退出函数。如果 `str` 不为 `nil`，则会将其绑定到常量 `newStr` 上，并执行后续的代码块。

希望这个解释对您有帮助！如果您还有其他问题，请随时提问。

[[iOS][Swift][中文] 基礎語法#12. 初探Optional](https://www.youtube.com/watch?v=6Dd6_wjvEkA)
### Closeture
####  理解
简单来讲，js中的箭头函数就是闭包的一种，可以作为参数传递之，
是面向函数编程的一大体现
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
