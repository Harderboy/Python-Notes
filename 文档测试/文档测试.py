import doctest


# doctest 模块可以提取注释中的代码执行
# doctest 严格按照python交互模式的输入提取（格式严谨）
def mySum(x, y):
    '''
    get the sum of two numbers
    :param x: first num
    :param y: second num
    :return: sum

    example
    注意有空格
    >>> print(mySum(1,2))
    3

    '''
    return x + y


print(mySum(1, 2))

# 进行文档测试
doctest.testmod()
