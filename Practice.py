days=int(input("Enter number of days:  "))
if days<=0:
    print("Invalid input")
elif days<=5:
    fine=days*2
elif days<=10:
    fine=5*2+(days-5)*3
else:
    fine=5*2+5*3+(days-10)*5
print("The fine is: ",fine)