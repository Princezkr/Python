def Line():
    print("="*100)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def decimal_to_hex(decimal):
    return hex(decimal)[2:].upper()

def decimal_to_bcd(decimal):
    bcd = ""
    for digit in str(decimal):
        bcd += format(int(digit), '04b')
    return bcd

def decimal_to_excess3(decimal):
    excess3 = ""
    for digit in str(decimal):
        excess3 += format(int(digit) + 3, '04b')
    return excess3

def decimal_to_gray(decimal):
    binary = bin(decimal)[2:]
    gray = binary[0]
    for i in range(1, len(binary)):
        gray += str(int(binary[i-1]) ^ int(binary[i]))
    return gray

def binary_to_decimal(binary):
    return int(binary, 2)

def octal_to_decimal(octal):
    return int(octal, 8)

def hex_to_decimal(hex_val):
    return int(hex_val, 16)

def bcd_to_decimal(bcd):
    decimal = ""
    for i in range(0, len(bcd), 4):
        decimal += str(int(bcd[i:i+4], 2) - 3)
    return int(decimal)

def excess3_to_decimal(excess3):
    decimal = ""
    for i in range(0, len(excess3), 4):
        decimal += str(int(excess3[i:i+4], 2) - 3)
    return int(decimal)

def gray_to_decimal(gray):
    binary = gray[0]
    for i in range(1, len(gray)):
        binary += str(int(binary[i-1]) ^ int(gray[i]))
    return int(binary, 2)

def validate_binary(binary_str):
    try:
        num = int(binary_str)
        while num > 0:
            if num % 10 > 1:
                return False
            num //= 10
        return True
    except:
        return False

def validate_octal(octal_str):
    try:
        for digit in octal_str:
            if int(digit) > 7:
                return False
        return True
    except:
        return False

def validate_hex(hex_str):
    try:
        int(hex_str, 16)
        return True
    except:
        return False

def validate_bcd(bcd_str):
    if len(bcd_str) % 4 != 0:
        return False
    for i in range(0, len(bcd_str), 4):
        digit = int(bcd_str[i:i+4], 2)
        if digit > 9:
            return False
    return True

def validate_excess3(excess3_str):
    if len(excess3_str) % 4 != 0:
        return False
    for i in range(0, len(excess3_str), 4):
        digit = int(excess3_str[i:i+4], 2)
        if digit < 3 or digit > 12:
            return False
    return True

def validate_gray(gray_str):
    try:
        int(gray_str, 2)
        return True
    except:
        return False

L = 1
while L != 0:
    Line()
    print('''Enter 1 To Input Decimal Code
Enter 2 To Input Binary Code
Enter 3 To Input Octal Code
Enter 4 To Input HexaDecimal Code
Enter 5 To Input BCD Code
Enter 6 To Input Excess-3 Code
Enter 7 To Input Gray Code
Enter 8 To Exit The Program''')
    Line()
    
    try:
        I = int(input("Enter Your Choice: "))
        
        if I == 1:
            while True:
                try:
                    X = int(input("Enter Decimal Number: "))
                    if X < 0:
                        print("Please enter a non-negative number")
                        continue
                    break
                except ValueError:
                    print("Invalid Input. Please enter a valid decimal number.")
            
            Line()
            print(f'''Enter 1 To Convert Into Binary Code
Enter 2 To Convert Into Octal Code
Enter 3 To Convert Into HexaDecimal Code
Enter 4 To Convert Into BCD Code
Enter 5 To Convert Into Excess-3 Code
Enter 6 To Convert Into Gray Code''')
            Line()
            
            try:
                choice = int(input("Enter Your Choice: "))
                if choice == 1:
                    print(f"Decimal {X} = Binary {decimal_to_binary(X)}")
                elif choice == 2:
                    print(f"Decimal {X} = Octal {decimal_to_octal(X)}")
                elif choice == 3:
                    print(f"Decimal {X} = Hexadecimal {decimal_to_hex(X)}")
                elif choice == 4:
                    print(f"Decimal {X} = BCD {decimal_to_bcd(X)}")
                elif choice == 5:
                    print(f"Decimal {X} = Excess-3 {decimal_to_excess3(X)}")
                elif choice == 6:
                    print(f"Decimal {X} = Gray Code {decimal_to_gray(X)}")
                else:
                    print("Invalid Choice")
            except ValueError:
                print("Invalid Input")
        
        elif I == 2:
            while True:
                X = input("Enter Binary Number: ")
                if validate_binary(X):
                    break
                else:
                    print("Invalid Input. Please enter a valid binary number.")
            
            decimal = binary_to_decimal(X)
            Line()
            print(f"Binary {X} = Decimal {decimal}")
        
        elif I == 3:
            while True:
                X = input("Enter Octal Number: ")
                if validate_octal(X):
                    break
                else:
                    print("Invalid Input. Please enter a valid octal number.")
            
            decimal = octal_to_decimal(X)
            Line()
            print(f"Octal {X} = Decimal {decimal}")
        
        elif I == 4:
            while True:
                X = input("Enter Hexadecimal Number: ")
                if validate_hex(X):
                    break
                else:
                    print("Invalid Input. Please enter a valid hexadecimal number.")
            
            decimal = hex_to_decimal(X)
            Line()
            print(f"Hexadecimal {X} = Decimal {decimal}")
        
        elif I == 5:
            while True:
                X = input("Enter BCD Code: ")
                if validate_bcd(X):
                    break
                else:
                    print("Invalid Input. Please enter a valid BCD code (multiples of 4 bits).")
            
            decimal = excess3_to_decimal(X)
            Line()
            print(f"BCD {X} = Decimal {decimal}")
        
        elif I == 6:
            while True:
                X = input("Enter Excess-3 Code: ")
                if validate_excess3(X):
                    break
                else:
                    print("Invalid Input. Please enter a valid Excess-3 code.")
            
            decimal = excess3_to_decimal(X)
            Line()
            print(f"Excess-3 {X} = Decimal {decimal}")
        
        elif I == 7:
            while True:
                X = input("Enter Gray Code: ")
                if validate_gray(X):
                    break
                else:
                    print("Invalid Input. Please enter a valid Gray code.")
            
            decimal = gray_to_decimal(X)
            Line()
            print(f"Gray Code {X} = Decimal {decimal}")
        
        elif I == 8:
            print("Thank you for using the Code Converter. Goodbye!")
            L = 0
        
        else:
            print("Invalid Choice. Please enter a number between 1 and 8.")
    
    except ValueError:
        print("Invalid Input. Please enter a valid number.")