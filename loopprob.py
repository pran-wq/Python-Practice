#program to write 1 to 100
p = 1
while p<= 100:
    print(p)
    p +=1

# printing number from 100 to 1

x = 100
while x>=1:
    print(x)
    x -=1

# program to write the table of n
n = int(input("enter your number : "))

x = 1
while x <=10:
    print(f"{n} into", x, "=", n*x)
    x +=1

# program to print a loop

list = [1,4,9,16,25,36,49,64,81,100]
n  = 0
while n<= len(list) -1:
    print(list[n])
    n +=1 

# program to  finding item in tuple

list2 = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter the number you want to find : "))
i = 0
while i<= len(list2) - 1:
    if list2[i] == x:
        print("found at index :",i)
        break
    else:
        print("finding..")
    i +=1





    

