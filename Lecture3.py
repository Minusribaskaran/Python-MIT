#while loop
n = int(input("Enter a number: "))
while n > 0:
    print(n)
    n = n - 1
  
n = 0
where = input("Go right or left? ")
while (where == 'right'):
    n = n + 1
    if(n>2):
        print(":(")
    where =input("Go right or left? ")
print("You are out of the loop :)")

#Factorial
x = 4
i =1
factorial = 1
while i<=x:
    factorial *= i
    i +=1
print(f'{x} factorial is {factorial}')

x = 4
fact =1
for i in range (1,x+1):
    fact*=i
print(f'{x} factorial is {fact}')

#For loop
for n in range(5):
    print(n)
    
sum =0
for i in range(3,6):
    sum+=i
print(sum)