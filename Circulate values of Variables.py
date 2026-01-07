x=int(input("Enter Value Of x: "))
y=int(input("Enter Value Of y: "))
z=int(input("Enter Value Of z: "))
for i in range(3):
    x,y,z=y,z,x
    print(x,y,z)