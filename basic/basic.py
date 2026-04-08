# print('waaaaaaaaa')

# # input("请输入数字" + "\n")

# var1 = input("请输入数字1" + "\n")
# var2 = input("请输入数字2" + "\n")
# print("输入的数字2是" + var2 * 3)
# print("输入的数字1是" + var1)

# x = 123
# print( f"输入的数字是{x}") # "输入的数字是123"
# print( "输入的数字是" + str(x) ) # "输入的数字是123"

# "xy" in "123xy456" # True
# 'x' not in "123xy456" # False

x = 'abc'
y = 'xyz'
print(x + y) # "abcxyz"
print(x * 3) # "abcabcabc"
print(x) # "abc"

# 切片操作 第三个参数表示每隔几个取一个
print(x[0]) # "a"
print(x[-1]) # "c"
print(x[0:2]) # "ab"
print(x[1:]) # "bc"
print(x[1:2:3]) # "b"
print(x[::2]) # "ac"

# 方法
x.count('a') # 统计字符串中'a'出现的次数
x.isalnum() # 判断字符串是否由字母和数字组成
x.isalpha() # 判断字符串是否由字母组成
x.join('123') # 将字符串'123'中的每个字符用'x'连接起来，返回'x1x2x3'
x.split('b') # 将字符串'x'按照'b'分割成一个列表,返回 ['a', 'c']
'a,b,c,d'.split(',') # 将字符串'a,b,c,d'按照','分割成一个列表，返回['a', 'b', 'c', 'd']
x.startswith('a') # 判断字符串是否以'a'开头

# 类型转换
abc = '123xyz'
xyz = int(abc)
print(type(xyz)) #ValueError: invalid literal for int() with base 10: '123xyz'

# 大小比较
456 > 1234 # False
"456" > "1234" # True 因为字符串比较是按照字典序比较的，'4' > '1'
len("456") > len("1234") # False 因为字符串长度比较是按照字符数比较的，'456'的长度是3，'1234'的长度是4