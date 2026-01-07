n = int(input("Enter the number of variables: "))
Values=[]
for i in range (n):
    x=int(input("Enter Your Value: "))
    Values.append(x)
    i+=1

print(Values)
k=Values.pop()
Values.insert(0,k)
print(Values)