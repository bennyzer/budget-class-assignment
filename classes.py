class Budget:  
    
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
    
    def deposit(self):
        new_deposit = int(input("How much would you like to deposit? \n"))
        new_balance = new_deposit + 10
        print(new_balance)


    def check_balance(self):
         print("this is the balance method")

    def withdraw(self):
        pass

    def transfer(self): 
        pass


category_1 = Budget("Food", 10999)
category_2 = Budget("clothing", 10999) 


print(category_1.check_balance())  

def adeposit:
    new_deposit = int(input("How much would you like to deposit? \n"))
        new_balance = new_deposit + 10
        print(new_balance)
