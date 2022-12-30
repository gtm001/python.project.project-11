#import random module
import random
#input range
a=int(input("Enter upper limit: "))
b=int(input("Enter lower limit: "))
#take random number from range
x=random.randint(a,b)
print("Range is ("+str(a)+","+str(b)+") and randomly picked number is",x)
#odd or even
if(x%2==0):
    print(x,"is an even number")
else:
    print(x,"is an odd number")
#+ve or -ve
if (x<0):
    print(x,"is a negative number")
else:
    print(x,"is a positive number")
#prime or composite
r=True
for i in range(2,x):
    if(x%i==0):
        r=False
if(x==1):
    print("1 is netiher a prime number nor composite number.")
elif (r==True):
    print(x,"is a prime number.")
else:
    print(x,"is a composite number.")