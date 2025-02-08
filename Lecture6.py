#Bisection Search:
    
x = float(input("Enter a number: "))
epsilon = 0.01
numguess = 0
if x <= 1:
    low = x
    high = 1
else:
    low = 0
    high = x
guess = (low+high)/2.0
while abs(guess**2-x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (low+high)/2.0
    numguess += 1
print("numguess=", numguess)
print(guess, "is close to the square root of", x)

#Cube:
    
cube = 27
epsilon = 0.01
low = 0
high = cube
guess = (low+high)/2.0
while abs(guess**3-cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (low+high)/2.0
print(guess, "is close to the cube root of", cube)

#Newton Raphson :
    
x = float(input("Enter a number: "))
g = x/2
while abs(g**2 - x) >= 0.01:
    g = g - (((g**2) - x)/(2*g))
print(g, "is close to the square root of", x)