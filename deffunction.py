#a program for choosing ice cream for customers by defining functions
print("welcome to the ice cream parlour")
print("--------------menu----------- --")
print("choose your ice cream")
print("1, vanilla scoop -  Rs40")
print("2, chocolate scoop - Rs50")
print("3, strawberry scoop - Rs45")
print("4, butterscoch scoop - Rs55")
print("----------------------------")
totalbill = 0
ordermore = "yes"
def vanilla():
    return 40*quantity
def chocolate():
    return 50*quantity
def strawberry():
    return 45* quantity
def butterscoch():
    return 55* quantity
while ordermore == "yes":
    choice = int(input(" choose your option : "))
    quantity = int(input("enter the quantity : "))
    if choice == 1:
        totalbill += vanilla()
    elif choice == 2:
        totalbill += chocolate()
    elif choice == 3:
        totalbill += strawberry()
    elif choice == 4:
        totalbill += butterscoch()
    else:
        print("invalid choice")
    ordermore = input("do you want to order more ? (yes/no) : ")

tax = totalbill * 0.08
finalbill = totalbill + tax
print("\n----------------------")
print("total before tax : ", totalbill)
print("tax applied : ", tax)
print("finalbill : ",finalbill)
print("--------------------------")
print("thank you for visiting, come again")


