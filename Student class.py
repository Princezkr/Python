class student:
    def __init__(self,name,reg_no):
        self.__name=name
        self.__reg_no=reg_no
    def New(self,New_Name):
        self.__name=New_Name
    def Student_Details(self):
        print("Name: ",self.__name)
        print("Reg_No: ",self.__reg_no)

s1=student("Karma",250263)
s1.Student_Details()
s1.New("Prince")
s1.Student_Details()