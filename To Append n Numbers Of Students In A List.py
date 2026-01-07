Class=[]
n=int(input("Enter The Number Of Students: "))
for i in range (n):
    x=str(input("Enter The Name Of Student:"))
    Class.append(x)
print(Class)
Class[1]="Amit"
print(Class)