import pandas as pd
df=pd.read_csv("student.csv")
filtered_df=df[df["Marks"]>50]
print("Students Greater Than 50 Marks")
print(filtered_df)