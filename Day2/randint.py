
"""

投掷骰子 

"""

from random import randint

face = randint(1, 6)

if face == 1:
	result = '唱歌'
elif face == 2:
	result = '跳舞'
elif face == 3:
	result = '举重'
elif face == 4:
	result = '泡妞'
elif face == 5:
	result = '做掌上压'
else:
	result = '玩大冒险'
	
print(result)
