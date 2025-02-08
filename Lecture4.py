#For loop:
#Number of even numbers
even = 0
for i in range(-4,6,2):
    if i%2 == 0:
        even+=1
print("No.of even numbers:",even)

#Number of unique characters
s = "abca"
seen = ''
for i in s:
    if i not in seen:
        seen+=i
print(len(seen))

#Checking square root:
guess = 0
neg = False
x = int(input("Enter a Number: "))
if x < 0:
    neg = True
while guess**2 < x:
    guess+=1
if guess**2 == x:
    print("Perfect square")
else:
    print("Not a perfect square")
    if neg:
        print("Did you mean",-x,"?")

#Secret Number:  
s = 11
found = False
for i in range(11):
    if i == s:
        print("Secret number found")
        found = True
if not found:
    print("Secret number not found")