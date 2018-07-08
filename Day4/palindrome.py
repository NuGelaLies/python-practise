"""

判断输入的正整数是不是回文数

回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

算法一般采取196， 

回文数: 121, 222, 131 等等

"""

#取巧玩法

x = str(input('请输入一个正整数: '))

y = x[::-1] #倒叙排列

if x == y: 
    print('%s 是一个回文数' % x)
else:
    print('%s 不是一个回文数' % x)

#一般玩法

x = int(input('请输入一个正整数: '))

temp = x
num = 0

while temp > 0:
    num *= 10
    num += temp % 10
    temp //= 10
    print(temp)
if x == num:
    print('这是一个回文数 num = %d' % num)
else:
    print('这不是一个回文数 num = %d' % num)