def Condition1():
    while True:
        y=int(input("Enter The Price Of The Item: "))
        if y>=0:
            break
        else:
            print("Enter A Non Negetive Number")
    Append(y)

def Condition2():
    while True:
        z=int(input("How Many To Add: "))
        if z>=0:
            break
        else:
            print("Enter A Non Negetive Number")
    Append(z)

def Space1(i):
     for j in range(10-len(Store[i][0])):
         print(" ",end='')

def Space2(i):
    Num_As_Str=str(Store[i][1])
    for j in range(10-len(Num_As_Str)):
        print(" ",end='')

def Append(x):
    Items.append(x)

def Remove():
    while True:
            x=str(input("Enter The Item to Remove: "))
            if x in Store:
                Store.pop(x)
                break
            else:
                print("Enter A Valid Item")

def Decorate():
    print("====================================================================")

Store={}

a=0
while a==0:
    print('''Enter 1 To Add Items To The Store: 
Enter 2 To Remove Items From The Store: 
Enter 3 To Modify Price Or Ammount Of Items In Store: 
Enter 4 To Check All Items In Store: 
Enter 5 To Buy Items From The Shop: 
Enter 6 To Sell Items To The Store: 
Enter 7 To Exit The Store: ''')
    
    Choice=int(input("Enter Your Choice: "))
    if Choice==1:
        n=int(input("How Many Items U want To Add To the Store: "))
        for i in range(n):
            Items=[]
            x=str(input("Enter Item Name: "))
            Append(x)
            Condition1()
            Condition2()
            Store[x]=Items
            Decorate()

    elif Choice==2:
        n=int(input("How Many Items U want To Remove From the Store: "))
        for i in range(n):
            print("The Item Has Been Removed",Remove())
            Decorate()

    elif Choice==3:
        

    elif Choice==4:
        for i in Store.keys():
            print("Item: ",Store[i][0],end='')
            Space1(i)
            print("Price: ",Store[i][1],end='')
            Space2(i)
            print("Available: ",Store[i][2])
        Decorate()