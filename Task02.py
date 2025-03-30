import math
def mathFun(n):
    print('Square root:', math.sqrt(n))
    print('Logarithm:', math.log(n))
    print('Sine:', math.sin(math.radians(n)))


num = int(input('Enter a number: '))
mathFun(num)
