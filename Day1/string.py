
string = 'hello world'

print('字符串长度: %s' % (len(string)))
print('单词首字母大写 %s:' % (string.title()))
print('字符串大写: %s' % string.upper())
print('字符串小写: %s' % string.lower())
print('字符串判断大小写: %s' % string.isupper())
print('字符串开头是不是hello: %s' % string.startswith('hello'))
print('字符串是否是以hello结尾: %s' % string.endswith('hello'))
print('字符串拼接')
str2 = '- \u004e\u0075\u0047\u0065\u006c\u0061\u004c\u0069\u0065\u0073'
str3 = string.title() + ' ' + str2.lower()
print(str3)
