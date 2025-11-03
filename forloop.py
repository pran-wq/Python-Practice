#program to print a list using for loop

# list = [1,4,9,16,25,36,49,64,81,100]
# for n in list:
#     print(n)
# program to search for a num in a tuple

# tup = (1,4,9,16,25,36,49,64,81,100)
# for x in tup:
#     if x == 16:
#         print("16, found at",tup.index(16))
#         continue
#     print(x)
# else:
#     print("end of search")

#program to print table of n

# n= int(input("enter the number : "))
# for i in range (1,11,):
#     print(n," into ",i, "=", n*i)

#print 100 to 1

# for i in range(100,0,-1):
#     print(i)

# program for sumation of numbers upto n using for loop
# n = int(input("enter your number: "))
# total = 0 
# for i in range(1,n+1):
#     total +=i
# print(total)

# program for summation of numbers upto n using while loop
# n = int(input("enter your number: ")) 
# total = 0
# i =0
# while i < n:
#     i +=1
#     total += i
# print(total)

# program to calculate factorial

n = int(input("enter the number : "))
total = 1
i = 1
for i in range (1, n+1):
    total *= i
print(total)


