#EXAMPLE
#Type this in console-- String
a='me'
b='myself'
c=a+b
d=a+" "+b
silly=a*3

s='abc'
len(s)


############## YOU TRY IT ###############
#Type this in console-- Slicing
s="abcdefgh"
s[3:6]
s[3:6:2]
s[:]
s[::-1]
s[4:1:-2]

#EXAMPLE
#Immutable String
s="car"
print(s)
s='b'+s[1:len(s)]
print(s)

#EXAMPLE
#Printing Example
a="the"
b=3
c="musketeers"
print(a,b,c)
print(a+str(b)+c)

############## YOU TRY IT ###############
# Write a program that: 
# * Asks the user for a verb.
# * Prints "I can _ better than you" where you replace _ with the verb.
# * Then prints the verb 5 times in a row separated by spaces.
# For example, if the user enters run, you print:
#     I can run better than you!
#     run run run run run
verb=input("Enter a verb: ")
print("I can",verb,"better than you")
print((verb+" ")*5)

#EXAMPLE
#F string
num=300
fraction=1/3
print(num*fraction,'is',fraction*100,'% of',num)
#to eliminate space between fraction*100 and % 
print(num*fraction,"is",str(fraction*100)+'% of',num)
#using F string
print(f'{num*fraction} is {fraction*100}% of {num}')

#EXAMPLE
#comparison example
pset_time=15
sleep_time=8
print(sleep_time>pset_time)
derive=True
drink=False
both =drink and derive
print(both)

############## YOU TRY IT ###############
#save secret number in variable
#asks user for a numerical guess
#print bool output depending on whether guess matches the secret
secret_number=10
guess_number=int(input("Type a guess number:"))
print(secret_number==guess_number)

#EXAMPLE
#Branching example
pset_time=22
sleep_time=2
if(pset_time+sleep_time)>24:
    print("impossible")
elif(pset_time+sleep_time)>=24:
    print("full schedule!")
else:
    leftover=abs(24-(pset_time+sleep_time))
    print(leftover,"h of free time!")
print("end of day!")

############## YOU TRY IT ###############
#semantic structure fix bug
x=int(input("Enter a number for x:"))
y=int(input("Enter a different number for y:"))
if x==y:
    print(x,"is the same as",y)
    print("these are equal!")
else:
    print("these are not equal")

#EXAMPLE 
#Indentation and nested branching
x=float(input("Enter a number for x:"))
y=float(input("Enter a number for y:"))
if x==y:
    print("x is equal to y")
    if(y!=0):
        print("therefore,x/y is",x/y)
elif x<y:
    print("x smalller than y")
else:
    print("y smaller than x")
print("Thanks!")


############## YOU TRY IT ###############
#write a program that
  #save secret number and ask user guess number
  #print whether the guess is too low ,too hig , or same as secre
secret=5
guess=int(input("Enter a guess number:"))
if guess==secret:
    print("They are equal!")
elif secret>guess:
    print("X is greater!")
else:
    print("Y is greater!")
print("The program ended!")



























    












