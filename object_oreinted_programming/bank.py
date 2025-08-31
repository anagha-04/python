
class Bank:


    def set_customer_details(self,person_name,acc_no,balance):

        self.bank_name = "SBI"

        self.person_name = person_name

        self.acc_no = acc_no

        self.balance = balance

    def balance_enq(self):

        print(f"Dear {self.bank_name} customer your acc {self.acc_no} avl balance is {self.balance}")

    def deposite(self,amount):

        self.balance+=amount

        print(f"your {self.bank_name} bank account  {self.acc_no} has been cretied with amount {amount} avl balance is {self.balance}")

    def withdraw(self,amount):

        if self.balance<amount:

            print("transaction failed")

        else:

            self.balance -= amount

            print(f"your {self.bank_name} bank account  {self.acc_no} has been cretied with amount {amount} avl balance is {self.balance}")

bank_instance1 = Bank()

bank_instance1.set_customer_details("pranav",4566839,120000)

bank_instance1.deposite(500)

bank_instance1.withdraw(1250000)

bank_instance1.withdraw(100000)

    
bank_instance1.balance_enq()





        

     