#Advanced Guess and Check:
x = int(input("Enter a number to find square root: "))
epsilon = 0.01
guess = 0.0
increment = 0.00001
num_guess = 0
while abs(guess**2-x) >= epsilon and (guess**2) <= x:
    guess += increment
    num_guess += 1
print('Number of guesses =', num_guess)
if abs(guess**2-x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(guess, 'is close to square root of', x)

#Binary:    
x = int(input('Enter an integer: '))
result = ''
negflag = False
if x < 0:
    negflag = True
    x = abs(x)
elif x == 0:
    result = 0
while x > 0:
    result = str(x%2) + result
    x = x//2
if negflag:
    result = '-' + result
print(result)