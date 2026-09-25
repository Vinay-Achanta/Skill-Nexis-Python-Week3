import pandas as pd

data = pd.read_csv("students.csv")

print("Average Marks:", data["Marks"].mean())
print("Highest Marks:", data["Marks"].max())
print("Lowest Marks:", data["Marks"].min())