"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

任意两条边的和大于第三边

"""

'''
判断输入的三条边能否构成三角形
如果能的求出三角形的周长以及面积
if else elif
'''

import math

x = float(input('请输入三角形第一条边的长度:'))
y = float(input('请输入三角形第二条边的长度:'))
z = float(input('请输入三角形第三条边的长度:'))

if x + y > z and x + z > y and y + z > x:
   p = x + y + z
   p2 = p / 2
   area = math.sqrt(p2 * (p2 - x) * (p2 - y) * (p2 - z))
   print('该三角形的周长为: %f' % p)
   print('该三角形的面积为: %f' % area)
else:
   print('不能构成三角形')