a=0
Library=["Python","Java","C++"]

while a==0:
    print("#####################################################")
    print("""Enter 1 To Add Book To Library
Enter 2 To Check If Book Is Available
Enter 3 To See All The Books Available
Enter 4 To Remove Book From Library
Enter 5 To Exit Library""")

    n=int(input("Enter Your Choice: "))
    if n==1:
        x=str(input("Enter The Name Of Book: "))
        Library.append(x)
    elif n==2:
        x=str(input("Enter The Book Name: "))
        if x in Library:
                print("The Book Is Available")
        else:
                print("The book Is Not Available")
    elif n==3:
        print(Library)
    elif n==4:
        x=str(input("Enter The Name Of Book: "))
        if x in Library:
                Library.remove(x)
        else:
                print("Book Not Found")
    elif n==5:
          a=1
    else:
          print("Invalid Input")