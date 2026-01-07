import pandas as pd
marks = [55, 67, 45, 78, 60, 72, 58, 90, 84, 69]
df = pd.DataFrame({'Marks': marks})
print("Student Marks DataFrame:")
print(df)
description = df.describe()
print("\nStatistical Summary:")
print(description)
print("Max Marks: ",df['Marks'].max())
print("Min Marks: ",df['Marks'].min())