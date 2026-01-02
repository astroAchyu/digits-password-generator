#digits password generator
n=int(input("enter how many digits password needed "))
n=10**n
l=n//10
u=n-1
import random
p=random.randint(l,u)
print("your password is",p)
