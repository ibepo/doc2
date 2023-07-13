## 为什么要使用`this`

`this`提供了一种更为优雅的方式来隐式的传递一个`对象引用`，因此可以将一个`API`设计的更为简洁
随着你使用的模式越来越复杂，显示的传递上下文对象会让代码变得越来越复杂。
在对象和原型中，你就会明白函数可以自动引入合适的上下文对象多么重要。

## 对`this`的两个误解
### ~~`this`指向函数自身~~
javascript中所有函数都是对象
所以函数中是可以存放属性值（即状态）,但是除了函数对象本身，还有其他更合适的地方。

⭐`this.`没办法调用函数本身的属性
```js
function foo(sum){
	console.log{"foo:"+sum}
	//记录this下边的count
	this.count++
}
foo.count=0

var i;
for(i=0,i<10;i++){
	if(i>5){
		foo(i)
	}
}

-----output------
//foo:6
//foo:7
//foo:8
//foo:9

console.log(foo.count)
//0

```

输出`foo：5`...等4次，证明调用了`foo（）`四次，（windows调用的）
但是foo对象上的属性`count`还是0,
其实这里的操作是`this`指向了`window`,
所以是在`window`上默认添加了一个`count`属性,换句话说创建了一个`全局变量`

**证明:`this`并不是指向函数本身,而是指向的调用函数的，这里是`window`,我称为`执剑人`**

⭐ 回到词法作用域
一种逃避`this`的解决方法是回到`词法作用域`
1.在函数内部调用自身属性，用一个指向函数对象的`词法标识符`(变量)来引用它
```js
function foo(sum){
	console.log{"foo:"+sum}
	foo.count++ //将this替换成foo
}
foo.count=0

var i;
for(i=0,i<10;i++){
	if(i>5){
		foo(i)
	}
}

-----output------
//foo:6
//foo:7
//foo:8
//foo:9

console.log(foo.count)
//0

```

2.创建另一个带有count属性的对象，另起炉灶，不用函数对象属性
```js
function foo(sum){
	console.log{"foo:"+sum}
	foo.count++ //将this替换成foo
}
var data={
  count=0
}
var i;
for(i=0,i<10;i++){
	if(i>5){
		foo(i)
	}
}

-----output------
//foo:6
//foo:7
//foo:8
//foo:9

console.log(data.count)
//0
```