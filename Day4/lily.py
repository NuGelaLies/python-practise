'''
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

'''

for x in range(100 , 1000):
    z = x % 10          #个位
    y = x // 10 % 10    #十位
    q = x // 100        #百位
    if z ** 3 + y ** 3 + q ** 3 == x:
        print(x , end = " ")
print()