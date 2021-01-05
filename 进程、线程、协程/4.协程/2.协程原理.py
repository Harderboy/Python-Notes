'''
Python对协程的支持是通过generator实现的
'''


def run():
    print(1)
    # yield 的作用就是把一个函数变成一个 generator，
    # 带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30


'''
yield在函数中的功能类似于return，不同的是yield每次返回结果之后函数并没有退出，
而是每次遇到yield关键字后返回相应结果，并保留函数当前的运行状态，等待下一次的调用。
如果 一个函数需要多次循环执行一个动作，并且每次执行的结果都是需要的，这种场景很适合使用yield实现。
包含yield的函数成为一个生成器，生成器同时也是一个迭代器，支持通过next方法获取下一个值

一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，
但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执
行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。

yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，
不仅代码简洁，而且执行流程异常清晰

在一个 generator function 中，如果没有 return，则默认执行至函数完毕，
如果在执行过程中 return，则直接抛出 StopIteration 终止迭代。
'''

# 协程的最简单风格，控制函数的阶段执行，节约线程或者进程的切换
# 返回值是一个生成器
# 没有yield关键字，函数调用时会执行代码，（执行输出语句）输出信息
m = run()
print(next(m))
print(next(m))
print(next(m))
