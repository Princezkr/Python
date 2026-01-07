try:
    mark = float(input("Enter student mark (0-100): "))
    if mark < 0 or mark > 100:
        raise ValueError("Mark must be between 0 and 100.")
    print("Valid mark:", mark)
except ValueError as e:
    print("Error:", e)