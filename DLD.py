def Line():
    print("=============================================================================================================")

def Binary(X):
    if set(X).issubset({'0','1'}):
        return True
    else:
        print("Invalid Input")

def Octal(X):
    if set(X)<=set('01234567'):
        return True
    else:
        print("Invalid Input")

a=input("Enter")
while Octal(a) is not True:
    a=input("Enter Your Value")
Line()