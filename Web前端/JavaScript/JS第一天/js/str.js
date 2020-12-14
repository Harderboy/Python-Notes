var str1 = "sunck is good凯"
var str2 = new String("sunck is good")

// 字符串创建之后不可变
// 变的是变量的引用
// str1 = "good"

str1[1] = 'k'

console.log(str1)
console.log(str2)

console.log(typeof str1)
console.log(typeof str2)

// 按（各个国家）字符计算长度 而非字节
console.log(str1.length)
console.log(str2.length)

// charAt(index) :取下标字符
console.log(str1.charAt(1))

// charCodeAt(index): 转对应下标字符ascii值
// String.fromCharCode(ascii值)

// 转大小写

// 字符串是否相同、比大小

// str1.localeCompare(str2)
console.log(str1 > str2)
// console.log(str1.localeCompare(str2))
var res = str1.localeCompare(str2)
// if (res >0){}

// indexOf：查找单词，返回第一个字母下标
// lastIndexOf

console.log(str1.indexOf('good'))

// replace() 替换，全部替换需要用正则

var str3 = str2.replace("good", "nice")
console.log(str3)

// substring()、substr() 区别：最后第二个参数含义不同
var res1 = str2.substring(9, 13)
console.log(res1)

// 字符串分割
// split()

// 拼接（数组）
// join


// x-y
// parseInt(Math.random() * (y - x + 1) + x)
console.log(Math.random())
// 0-100
console.log(parseInt(Math.random() * (100 - 0 + 1) + 0))
