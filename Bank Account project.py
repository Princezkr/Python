class Bank_Account:
    def __init__(self,Acc_Num,Acc_Holder,Balance):
        self.__Acc_Num=Acc_Num
        self.__Acc_Holder=Acc_Holder
        self.__Balance=Balance
    
    def Deposit(self,Amount):
        if Amount>0:
            self.__Balance+=Amount
            print(f"{Amount} Deposited Successfully")
        else:
            print("Deposite More Than Zero")
    
    def Withdraw(self,Amount):
        if Amount<=0:
            print("Withdraw More Than Zero")
        elif self.__Balance<Amount:
            print("Insufficient Balance")
        else:
            self.__Balance-=Amount
            print(f"{Amount} Withdrawn Successfully")
    
    def Check_Balance(self):
        print(f"Available Balance: {self.__Balance}")
    
    def Account_Details(self):
        print("Account Details")
        print("Account Number: ",self.__Acc_Num)
        print("Account Holder: ",self.__Acc_Holder)
        print("Balance: ",self.__Balance)

Account=Bank_Account("abc123","Karma",5000)
Account.Account_Details()
Account.Deposit(5000)
Account.Check_Balance()
Account.Withdraw(5000)
Account.Check_Balance()