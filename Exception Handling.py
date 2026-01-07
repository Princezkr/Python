try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Denominator cannot be zero!")
except ValueError:
    print("Error: Please enter valid integers.")

    
numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))
if ZeroDivisionError:
    print("Error: Denominator cannot be zero!")
else:
    result = numerator / denominator
    print("Result:", result)