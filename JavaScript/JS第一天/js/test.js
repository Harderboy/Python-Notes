console.log('我是在外面的js文件')
// 是否带参数，返回的都是当前时间
// string 类型
// var d1 = Date()
// 不同格式 1996-1-1 输出不同
// object 类型
var d1 = new Date("1996-01-01")
console.log(d1)
// 获取时间
// 设置时间

// 转换成字符串，多种格式
var str = d1.toLocaleString()
console.log(str)

// 时间运算
// 时间相减 类型为 number
var d2 = new Date()
var d3 = new Date(1996, 12, 11)
console.log(d2 - d3)
console.log(typeof(d2 - d3))
// 时间相加 类型为 string
console.log(typeof(d2 + d3))
