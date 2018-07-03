"""
输入月收入和五险一金计算个人所得税
"""

salary = float(input('这个月工资:'))
insurance = float(input('五险一金:'))

diff = salary - insurance - 5000
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 4500:
    rate = 0.1
    deduction = 105
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 55000:
    rate = 0.3
    deduction = 2755
elif diff < 80000:
    rate = 0.35
    deduction = 13505
else:
	rate = 0.45
	deduction = 13505
#abs 取绝对值
tax  = abs(diff * rate - deduction)
print('个人所得税: %.2f' % tax)
print('实际到手收人: %.2f' % (diff + 3500 - tax))