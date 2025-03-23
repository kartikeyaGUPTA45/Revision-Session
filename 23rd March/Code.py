a = 12
b = 4

sum = a+b

if  sum > 50:
    print("Sum is greater than 50")
else :
    print("Sum is less than or equal to 50")


a = 44
print("Number is Even") if a%2 == 0 else print("Number is Odd")

a = 37
rem = a%10

print(rem)

if rem == 0:
    print("Rem is zero")
elif rem%2 == 0:
    print("Rem is a multiple of 2")
else :
    print("Rem is not a multiple of 2")


a = 340
b = 1200
c = 56

if a>b and a>c:
    print("A is the maximum")
elif b>c:
    print("B is the maximum")
else:
    print("C is the maximum")


a = 59
if a%2 == 0:
    print("Number is even")
    if a>100:
        print("Number is greater than 100")
    elif a>50:
        print("Number is greater than 50 but less than 100")
    else :
        print("Number is less than 50")
else :
    print("Number is Odd")
    if (a>50):
        print("Number is greater than 50")
    else:
        print("Number is less than 50")


i = 1
while (i<=10):
    print("******")
    i+=1

i = 10
while (i>=1):
    print("******")
    i-=1


n = 20 
i = 1
sum = 0
while (i<=n):
    sum+=i;
    i+=1

print(sum)

a = 23
b = 67

while (a<=b):
    if a%2 == 0:
        print(a)
    a+=1    


n = 5
i = 1

while (i<=10):
    print(n*i)
    i+=1


n = 24
i=1

while(i<=n):
    if n%i==0:
        print(i)
    i+=1    


