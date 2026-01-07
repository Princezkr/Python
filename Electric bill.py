Units=int(input("Enter Units Consumed: "))
if Units<=100:
    Bill=Units*3
elif Units<=300:
    Bill=(100*3)+(Units-100)*5
elif Units>=301:
    Bill=(100*3)+(200*5)+(Units-300)*7
else:
    print("Invalid Input!!!!")
print("Total Elctricity Bill:",Bill)