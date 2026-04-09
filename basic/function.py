def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-5)) # 5

# 5种参数：必选参数、默认参数、可变参数、关键字参数和命名关键字参数

# 可变参数：在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
def calca(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calca(1, 2, 3) # 14
calca() # 0
calca(*[1, 2, 3]) # 14 将ist或tuple元素作为可变参数传入
calca(*(1, 2, 3)) # 14

def person(name, age , **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Adam', 45, gender='M', job='Engineer') # name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}


# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 调用方式如下：
# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
person('Jack', 24, city='Beijing', job='Engineer') #Jack 24 Beijing Engineer


# 递归
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

args = (1, 2, 3, 4)
kw = {'d': 99,'x': '#'}
f1(*args, **kw) # a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))
print(fact(100))