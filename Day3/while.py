'''
while 循环

猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

'''

from random import randint

answer = randint(1, 100)
couter = 0
while True:
    couter += 1
    number = int(input('请输入1~100以内的数字:'))
    if number < answer:
        print('小一点')
    elif number > answer:
        print('大一点')
    else:
        print('你猜对了')
        break
    print('你一共猜了%d次' % couter)
if couter > 7:
    print('你的智商余额明显不足，请及时充值')

