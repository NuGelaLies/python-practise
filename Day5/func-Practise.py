
### 练习

#### 练习1：实现计算求最大公约数和最小公倍数的函数。

def gcd(x, y): #最大公约数
	(x, y) = (y, x) if x > y else (x, y)
	for factor in range(x, 0, -1):
		if x % factor == 0 and y % factor == 0:
			return factor

def lcm(x, y): #最小公倍数
	return x * y // gcd(x, y)

#### 练习2：实现判断一个数是不是回文数的函数。


def is_palindrome(x):
	is_prime = True
	num = x[::-1]
	if x == num:
		is_prime = True
	else:
		is_prime = False
	return is_prime

#### 练习3：实现判断一个数是不是素数的函数。

def is_prime(x):
	is_sil = True
	for factor in range(2, x):
		if x % factor == 0 and factor != 1 and factor != x:
			return False
	return is_sil

#### 练习4：写一个程序判断输入的正整数是不是回文素数。

def is_primeAnd_palindrome(x):
	is_priAndpal = False
	if is_palindrome(x) and is_prime(x):
		is_priAndpal = True
	return is_priAndpal

'''

通过上面的程序可以看出，
当我们将代码中重复出现的和相对独立的功能抽取成函数后，
我们可以组合使用这些函数来解决更为复杂的问题，
这也是我们为什么要定义和使用函数的一个非常重要的原因。

'''
