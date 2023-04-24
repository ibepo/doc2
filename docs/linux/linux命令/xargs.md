## xargs

https://ruanyifeng.com/blog/2019/08/xargs-tutorial.html

`cat test.txt | xargs -i echo {}`
`cat test.txt | xargs -I {} echo {}`

大小写i的参数是不一样的效果，小写i默认参数为{}，且不能改变，而大写I参数是自定义的，可以是{}、a...等等。