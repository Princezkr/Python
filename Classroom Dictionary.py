Class={}
n=int(input("Enter How Many Students You Want To Enter: "))
for i in range(1,n+1):
    Student=[]
    w=str(input("Enter The Name: "))
    x=str(input("Enter The Course: "))
    y=str(input("Enter The Address: "))
    z=int(input("Enter The Phone No: "))
    Student.append(w)
    Student.append(x)
    Student.append(y)
    Student.append(z)
    Class[i]=Student
print(Class)
