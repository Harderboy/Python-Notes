// console.log("<h1>sunck</h1>")
// alert("<h1>sunck</h1>")
// document.write("<h1>sunck</h1>")
var num;
num = 2;
// typeof 为操作符，不叫函数
console.log(typeof(num));
console.log(typeof num);
console.log(num);

var num1 = 10;
var num2 = 15;
var sum = num1 + num2;
// console.log('sum = ' + sum)
// 会自动将sum 从数字转为字符串
console.log('sum = ' + sum.toString())


// 数字类型中的两种特殊值
var num5 = 1e308
console.log(num5)
var num6 = 1e309
console.log(num6)
var num3 = Infinity
console.log(Infinity + 1)
console.log(Infinity - Infinity)
// NAN不表示数字，但属于数字类型，特殊的数字
var num4 = NaN
console.log(typeof(NaN))

console.log(NaN + 1)
// false
console.log(NaN == NaN)
// true
console.log(isNaN(NaN))


// 字符串
var str1 = "sunck"
console.log(str1)
console.log(str1 + "!")
console.log(typeof(str1))

// 布尔值
var a = false
var b = true
console.log(a)
// 为假的类型：0，0.0，NaN, "", undefined, null, false

var a = "12+3"
// '12a3', 'a123', '   123'
// 转换失败为NaN
// 其他各类转换自行查阅，转Number、String、Boolean
var num7 = parseInt(a)
console.log(num7)
console.log(typeof(num7))
console.log("-----")

// 字符串类型
// var num8 = prompt("请输入一个数字：")
// console.log(typeof(num8))
// console.log(typeof(parseInt(num8)))

// 运算符
var num9 = 10
var num10 = 3
console.log(num9 / num10)
console.log(parseInt(num9 / num10))

// 字符串拼接时的类型转换

// 自增自减 python无
// num++, ++num （num--, --num）有区别
// num++ 先(取)赋值后加1
// var a = num++
// 加分号的作用，为了避免压缩文件，js代码位于一行，解析不了
// var num = 10;var c = "dfa";console.log("---")

// if
// if (表达式){语句}
// var num11 = parseInt(prompt("请输入一个数字"))
// if (num11 % 2 == 0) {
// 	console.log('偶数')
// } else {
// 	console.log("奇数")
// }

// 关系运算符 多了绝对相等“===”
console.log(1 == 1)
//  值相等，类型可以不同
console.log(1 == '1')
// 绝对相等，值相等 类型相同
console.log(1 === '1')


// ?:
// 表达式？表达式1:表达式2
var d = 1 ? 2 : 3
console.log(d)

// and or not
// && || !

// if (表达式){
// 	语句1
// }else if(表达式2){
// 	语句2
// }
// else{
// 	语句3
// }
if (d) {
	console.log('true')
} else if (!d) {
	console.log('false')
}

// switch语句
/*
switch (表达式1){
	case 标号1：
		语句1
	case 标号2：
		语句2
		
	...
	default :
		语句n
	
}
*/
//  default 语句可有可无

// var num12= parseInt(prompt("数字"))
// switch (num12){
// 	case 1:
// 		console.log('周一')
// 		break;
// 	case 2:
// 		console.log('周二')
// 		break;
// 	default:
// 		console.log("周末")
// }


// while 
/*python
while 表达式：
	语句1
else：
	语句2
*/
/*
while(表达式){
	语句
}
*/
/*do while语句
do{
	语句
}while (表达式)

*/

/* for语句
for (语句1;表达式;语句3){
	语句2
}
*/
sum = 0
for (var a = 1; a <= 10; a++) {
	sum += a
}
console.log(sum)

// 死循环
// for (;;){
// 	console.log("aaa")
// }

console.log("--------------")
//  for in 语句
var arr = [1, 2, 3, 4]
for (var i in arr) {
	console.log('arr[%s] = %d', i, arr[i])
	// console.log(typeof i)
	// console.log(arr[i])
	// console.log(typeof arr[i])
}
console.log("--------------")


// 函数
// 函数声明后不会立即执行，调用才会执行。
/*
function myFunction(var1,var2)
{
	代码
	return 表达式；
}
*/
console.log('-------')

function myFunction(num1, num2) {
	// console.log(num1+num2)
	console.log(arguments.length)
	for (var i = 0; i < arguments.length; i++) {
		console.log(arguments[i])
	}
	return num1 + num2
}
// 传多个实参
myFunction(1, 2, 3, 4, 5)

console.log('-------')
a = myFunction(1, 2, 3, 4, 5)
console.log(a)

console.log('-------')

function func() {
	// 变量提升
	// var num
	console.log(numb)
	var numb = 20
	console.log(numb)
	// js中没有用var定义的变量默认为全局变量
	p = 30

}
func()
console.log(p)

console.log('-------')

// 函数也是数据
function mysum(num1, num2) {

	return num1 + num2
}

mysum(6, 7)
var f = mysum
console.log(f(4, 5))

// 将函数当参数传递
function myfunc(s, a, b) {
	return s(a, b)
}
console.log(myfunc(mysum, 1, 2))

console.log('-------')
// 匿名函数 当参数传递
// var f = function(a, b) {
// 	return a * b
// }
// console.log(f(3,4))

function fun(fc, num1, num2) {
	return fc(num1, num2)
}
var num66 = fun(function(a, b) {
	return a * b
}, 3, 4)
console.log(num66)
