import pandas as pd

# Create a DataFrame directly in code
data = {
    "StudentID": [1, 2, 3, 4, 5],
    "Name": ["Aarav", "Isha", "Rohan", "Meera", "Kabir"],
    "Math": [88, 92, 75, 64, 55]
}

df = pd.DataFrame(data)

# Print the DataFrame
print("All data:")
print(df)

# Show only names and marks
print("\nNames and Math marks:")
print(df[["Name", "Math"]])

# Calculate and print the average mark
average_mark = df["Math"].mean()
print("\nAverage Math mark:", average_mark)
