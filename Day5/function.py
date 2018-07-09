'''
函数 function
'''

def factorial(num: int):
    """
    求阶乘
    
    :param num: 非负整数
    
    :return: num的阶乘
    """
    result = 1
    for x in range(1, num + 1):
            result *= x
    return result

x = int(input("请输入一个非负整数: "))



print(factorial(x))
print()

'''
> **说明：**Python的math模块中其实已经有一个factorial函数了，
事实上要计算阶乘可以直接使用这个现成的函数而不用自己定义。下面例子中的某些函数其实Python中也是内置了，
我们这里是为了讲解函数的定义和使用才把它们又实现了一遍，实际开发中不建议做这种低级的重复性的工作。
'''
