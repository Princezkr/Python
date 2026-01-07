n=int(input("Enter The NumberOf Rows: "))
for i in range (1,n+1):
    for j in range (n-i):
        print(" ",end='')
    for j in range (1,2*i):
        print(j,end='')
    print()

for i in range (1,n):
    for j in range (i):
        print(" ",end='')
    for j in range (1,2*(n-i)):
        print(j,end='')
    print()