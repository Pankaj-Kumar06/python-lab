import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

print("Original Dataset:")
print(df)

# 1. Display missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 2. Remove duplicate rows
df = df.drop_duplicates()

# 3. Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["CGPA"] = df["CGPA"].fillna(df["CGPA"].mean())
df["Department"] = df["Department"].fillna("Unknown")

# 4. Remove extra spaces from string columns
df["Name"] = df["Name"].str.strip()
df["Department"] = df["Department"].str.strip()

# 5. Convert CGPA to numeric
df["CGPA"] = pd.to_numeric(df["CGPA"], errors="coerce")

# 6. Remove invalid CGPA values
df = df[(df["CGPA"] >= 0) & (df["CGPA"] <= 10)]

# 7. Reset index
df = df.reset_index(drop=True)

print("\nCleaned Dataset:")
print(df)

# 8. Save cleaned dataset
df.to_csv("cleaned_students.csv", index=False)

print("\nCleaned dataset saved successfully.")