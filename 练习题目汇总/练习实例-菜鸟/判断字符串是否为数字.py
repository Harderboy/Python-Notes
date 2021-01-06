# coding=utf-8
'''
float() 函数用于将数字和字符串转换成浮点数。
>>> float(112)
112.0
>>> float(-123.6)
-123.6
>>> float('123')     # 字符串
123.0

官方手册-内置异常：https://docs.python.org/zh-cn/3/library/exceptions.html#bltin-exceptions

unicodedata 模块
    此模块提供了对 Unicode Character Database (UCD) 的访问，其中定义了所有 Unicode 字符的字符属性。
    该模块使用与 Unicode 标准附件 #44 “Unicode 字符数据库” 中所定义的相同名称和符号
    链接：https://docs.python.org/zh-cn/3/library/unicodedata.html

unicodedata.numeric(chr[, default])
    返回分配给字符 chr 的数值作为浮点数。 如果没有定义这样的值，则返回 default ，如果没有给出，则 ValueError 被引发。

'''


def is_number(s):
    try:
        # float() 函数用于将数字和字符串转换成浮点数。
        float(s)
        return True
    # except ValueError as e:
    except ValueError:
        # print("字符串数值有误：", e)
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    # 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
    except (ValueError, TypeError):
        print("字符串类型或数值有误")

    return False


if __name__ == "__main__":
    s = input("请输入一个需要判断的字符串：")
    print("该字符串是否为数字，结果为：", is_number(s))

'''
测试字符串和数字
    'foo'、'1'、'1.3'、'-1.37'、'1e3'

测试 Unicode
    阿拉伯语 5：'٥'
    泰语 2：'๒'
    中文数字：'四'
    版权号：'©'

'''
