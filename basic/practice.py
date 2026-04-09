# num1 = input('Enter the first number: ')
# num2 = input('Enter the second number: ')
# op = input('Enter the operator (+, -, *, /): ')
# sum = eval(num1 + op + num2)
# print('The result is: ' + str(sum))

# print('\\\n\\')
# print('\\\t\\') 

# print('Bob!''') # Bob!''  # 字符串连接，输出 'Bob!' + '' = 'Bob!'

# print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# r = 2.5
# s = 3.14 * r ** 2
# print(f'The area of a circle with radius {r} is {s:.2f}') # The area of a circle with radius 2.5 is 19.62  .2f 保留两位小数

# s1 = 72
# s2 = 85
# r = (s2 - s1) / s1 * 100
# print(f'The score increased by {r:.1f}%') # The score increased by 18.1% .1f 保留一位小数

# height = 1.75
# weight = 80.5
# bmi = weight / (height * height)
# if bmi < 18.5:
#     print(f'Your BMI is {bmi:.2f}, you are underweight.')
# elif bmi < 24:
#     print(f'Your BMI is {bmi:.2f}, you are normal weight.')
# elif bmi < 28:
#     print(f'Your BMI is {bmi:.2f}, you are overweight.')
# else:
#     print(f'Your BMI is {bmi:.2f}, you are obese.')

# n1 = 255
# n2 = 1000
# print(hex(n1), hex(n2)) # 0xff 0x3e8 将整数转换为十六进制字符串

# import math

# def quadratic(a, b, c):
#     if a == 0:
#         raise ValueError('a cannot be zero')
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         raise ValueError('no real roots')
#     elif delta == 0:
#         return -b / (2 * a)
#     else:
#         return (-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)
    
# print(quadratic(2, 3, 1)) # (-0.5, -1.0)

# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# calc([1, 2, 3]) # 14 list
# calc((1, 2, 3)) # 14 tuple
# # calc(1, 2, 3) # TypeError: calc() takes 1 positional argument but 3 were given

# # 5种参数：必选参数、默认参数、可变参数、关键字参数和命名关键字参数

# # 可变参数：在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
# def calca(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum

# calca(1, 2, 3) # 14
# calca() # 0
# calca(*[1, 2, 3]) # 14 将ist或tuple元素作为可变参数传入
# calca(*(1, 2, 3)) # 14

# def person(name, age , **kw):
#     print('name:', name, 'age:', age, 'other:', kw)

# person('Adam', 45, gender='M', job='Engineer') # name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}


# # 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# def person(name, age, *, city, job):
#     print(name, age, city, job)
# # 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# # 调用方式如下：
# # 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
# person('Jack', 24, city='Beijing', job='Engineer') #Jack 24 Beijing Engineer

# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# args = (1, 2, 3, 4)
# kw = {'d': 99,'x': '#'}
# f1(*args, **kw) # a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

# def mul(*args, **kw):
#     if len(args) == 0:
#         raise TypeError('mul() takes at least 1 argument (0 given)')
#     product = 1
#     for n in args:
#         product = product * n
#     return product

# # 测试
# print('mul(5) =', mul(5))
# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))
# print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
# if mul(5) != 5:
#     print('mul(5)测试失败!')
# elif mul(5, 6) != 30:
#     print('mul(5, 6)测试失败!')
# elif mul(5, 6, 7) != 210:
#     print('mul(5, 6, 7)测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#     print('mul(5, 6, 7, 9)测试失败!')
# else:
#     try:
#         mul()
#         print('mul()测试失败!')
#     except TypeError:
#         print('测试成功!')

# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         move(1, a, b, c)
#         move(n-1, b, a, c)

# move(4, 'A', 'B', 'C')
# move(2, 'A', 'B', 'C')

# def trim(s):
#     if s == '':
#         return s
#     start = 0
#     end = len(s) - 1
#     while start <= end and s[start] == ' ':
#         start = start + 1
#     while end >= start and s[end] == ' ':
#         end = end - 1
#     return s[start:end+1]

# if trim('hello  ') != 'hello':
#     print('测试失败!')
# else:
#     print('测试成功!')

def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    min = max = L[0]
    for x in L:
        if x < min:
            min = x
        if x > max:
            max = x
    return (min, max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')