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

height = 1.75
weight = 80.5
bmi = weight / (height * height)
if bmi < 18.5:
    print(f'Your BMI is {bmi:.2f}, you are underweight.')
elif bmi < 24:
    print(f'Your BMI is {bmi:.2f}, you are normal weight.')
elif bmi < 28:
    print(f'Your BMI is {bmi:.2f}, you are overweight.')
else:
    print(f'Your BMI is {bmi:.2f}, you are obese.')