#wAP to find factorial of n 

n= int(input("enter your number : "))
def fact(b):
    result =1
    for i in range(1,b+1):
        result *= i
    print("factorial of", b, "is", result)
fact(n)

#recrussive method of finding factorial

def fact(n):
    if n==0 or n ==1 :
        return 1
    else:
        return n* fact(n-1)
num = int(input("enter your number : "))
print("factorial of", num,"is",fact(num) )