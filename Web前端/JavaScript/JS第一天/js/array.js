// 即时函数
// (function(a){
// 	console.log('a = ' + a);
// 	console.log(typeof a)
// })(123);

(function(a) {
	console.log(a)
	console.log(typeof a)
})("123");


// 数组
console.log('---------')
var arr = [1, 2, 3]
console.log(typeof(arr))

for (var i = 0; i < arr.length; i++) {
	console.log('arr[%d] = %d', i, arr[i])
}
// 另外一种遍历方式
for (var i in arr) {
	// console.log(typeof i)
	console.log("arr[%s] = %d", i, arr[i])
}

// 数组对象
var arr1 = new Array(2)
arr1[0] = 0
arr1[1] = 1
arr1[2] = 2
console.log(arr1)

arr1[1] = 3
console.log(arr1)

arr1.length = 5
console.log(arr1)

arr1[10] = 10
console.log(arr1)

delete arr1[0]
console.log(arr1)
console.log(arr1[0])

console.log('---------')
arr2 = [0, 1, 2, 3]

// forEach()函数，不支持break和continue
arr2.forEach(function(item) {
	console.log(item)
})

console.log('---------')
// 数组常用方法

//尾部插入
arr2.push(10)
console.log(arr2)
// 头部插入
arr2.unshift(7)
console.log(arr2)
// 取尾部元素pop()
console.log(arr2.pop())
console.log(arr2)
// 不同于python 不支持指定下标，默认取尾部元素
console.log(arr2.pop(3))
console.log(arr2)
// 取头部
console.log(arr2.shift())
console.log(arr2)

console.log(arr2.join("-"))

// 分片
var a = arr2.slice(0, 2)
console.log(a)

// splice()
// reverse()
// concat()
var a = arr2.concat([10, 20, 30])
console.log(a)

// indexof()

// lastIndexOf()

// 排序
// sort()

var arr3 = new Array()
arr3[0] = "dfa"
arr3[1] = "dsadfjk"
arr3[2] = "jkljkldsfa"
arr3[3] = "khjjk"

// 自定义排序顺序
arr3.sort(function(x, y) {
	return x.length < y.length
})
console.log(arr3)


//
