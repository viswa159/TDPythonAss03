def factorial(i):
    if i<2:
        return 1
    return i * factorial(i-1)

num = int(input('Enter a number: '))
print('Factorial of',num,'is:',factorial(num) )
