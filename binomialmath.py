#title
#BinomialExpansionGenerator
from math import *
from time import sleep

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Please enter an integer!")
       continue
    else:
       return userInput
       break

print('Welcome to the Binomial Expansion Generator. I\'m here to help make')
print('solving the laborious Binomial Theorem problems involving Pascal\'s')
print('Triangle and large exponents a lot easier!')
print('Please enter the values for your variables in the formula below.')
print()
print('(a+b(X)^y)^n = ')
print('(nChoosei) * (a^(n-i)) * ((bX^y)^i)')
print()


A = inputNumber('What is your value for variable \'a\'')
B = inputNumber('What is your value for variable \'b\'')
N = inputNumber('What is your value for variable \'n\'')
print('Unless the variable \'y\' is not equal to 1, then what power is \'x\' equal to.')
Y = inputNumber('What is your value for variable \'y\'')
print()

I = 0

def comb(N, I):
    numerator = factorial(N)
    part = N - I
    denominator = factorial(part) * factorial(I)
    equation = int(numerator / denominator)
    return equation

array = []
def calculate(A, B, N, Y):
    I = 0
    while I <= N:
        power = Y * I
        coefficient = ((comb(N, I)) * (A ** (N-I)) * (B ** I))
        coefficient2 = str(coefficient) + ' '
        onespace = '1 '
        if coefficient == 1 and coefficient2 != onespace:
            coefficient = ''
        constant = 'x^' + str(power)
        if constant == 'x^0':
            constant = ''
        else:
            constant == constant
        if constant == 'x^1':
            constant = 'x'
        answer = (str(coefficient) + constant)
        array.append(answer)


        print(answer, end = '')
        if I <= (N - 1):
            print(' + ', end = '')
        elif I == N:
            print()
            break
        I += 1

        sleep(0.5)


calculate(A, B, N, Y)

def rever():
  revi = input('Reverse the order? ')
  if revi == 'yes' or revi == 'y':
    array = array[1:-1]
    print(array.reverse())

rever()


while True:
    sleep(1)
    interest = input('\nWould you like to calculate again? ')
    if interest == 'yes' or interest == 'y':
        print()
        A = int(input('What is your value for variable \'a\': '))
        B = int(input('What is your value for variable \'b\': '))
        N = int(input('What is your value for variable \'n\': '))
        Y = int(input('Unless the variable \'y\' is not equal to 1, then what power is \'x\' to. In other words, what is \'y\'? '))
        calculate(A, B, N, Y)
        rever()
    elif interest == 'no' or interest == 'n':
        print('\nThank you for using Binomial Expansion Generator. Happy calculating!')
        sleep(2)
        exit()
    elif interest != 'yes' or interest != 'y' or interest != 'no' or interest != 'n':
        error = 'Please type \'yes\' or \'no\'.'
        error = error.upper()
        print(error, end ='')
        True
