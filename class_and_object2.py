#a program for class and objects 

# class Student:
#     def __init__(self):
#         self.name = input("Enter your name :")
#         self.marks =[]
#         for i in range(1,4):
#             mark = float(input("Enter the marks of the subject " + str(i) + ": "))
#             self.marks.append(mark)
#     def get_percentage(self):
#         percentage = sum(self.marks)/3
#         print("\nyou got ", percentage," % percent in these subjects" )
#         if percentage >78:
#             print("\nHey, " + self.name + " you did great in these subjects")
#         elif percentage > 60:
#             print("\nHey, " + self.name + " you need to improve in these subjects")
#         else :
#             print("\nHey, " + self.name + " you did very poor in these subjects")
            

        
# student1 = Student()
# student1.get_percentage()

#another class and objects program for banking 
class Account:
    def __init__ (self, account_number, balance):
        self.account = account_number
        self.balance = balance 

    def debit (self):
        debit_amount = float(input ("Enter the amount to be debited : "))
        self.balance -= debit_amount
        print("\nYour current balance is : ", self.balance )
    def credit(self):
        credit_amount = float(input("\nEnter the amount to be credited : "))
        self.balance += credit_amount
        print("\nYour current balance is : ", self.balance)
customer1 = Account(37837, 70000)
customer1.debit()
customer1.credit()


        
