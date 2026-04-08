age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('your age is', age)
    print('kid')


age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')

sum = 0
for x in range(101):
    sum = sum + x
print(sum) # 5050

L = ['Bart', 'Lisa', 'Adam']

for name in L:
    print('Name:', name)