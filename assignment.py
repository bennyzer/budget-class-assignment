class monthlybudget:
    def __init__(self, category, amount,):
        self.category = category
        self.amount = amount
        

    def deposit(self):
        print(f'{self.category} has {self.amount} allocated at this time')

category_1 = monthlybudget("Food", 20,000)
category_2 = monthlybudget("clothing", 15,000) 
# category_3 = monthlybudget("Entertainment", 10,000)
# category_4 = monthlybudget("Data", 5,000) 

category_1.amount()
category_2.category()
print(category_2.amount)


print(type(monthly_budget))

