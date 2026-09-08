import pandas as pd

df = pd.read_csv("student_performance.csv")

print(df)

print("\nFirst 5 Students:")
print(df.head())