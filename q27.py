import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the dataset
data = {
    'Student': ['S1', 'S2', 'S3', 'S4', 'S5',
                'S6', 'S7', 'S8', 'S9', 'S10'],
    'Mathematics': [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
    'Physics':     [72, 88, 70, 92, 75, 79, 68, 90, 74, 85],
    'Chemistry':   [75, 82, 65, 88, 78, 83, 72, 92, 79, 86],
    'English':     [80, 84, 72, 91, 76, 80, 70, 95, 77, 89]
}

df = pd.DataFrame(data)

print("Student Examination Data:")
print(df)

# Set Seaborn style
sns.set_style("whitegrid")

# 1. Subject-wise score distributions
subjects = ['Mathematics', 'Physics', 'Chemistry', 'English']

for subject in subjects:
    plt.figure(figsize=(7, 5))
    sns.histplot(df[subject], kde=True)
    plt.title(f'{subject} Score Distribution')
    plt.xlabel('Score')
    plt.ylabel('Number of Students')
    plt.show()

# 2. Pairwise relationships between subjects
sns.pairplot(df[subjects])
plt.suptitle("Pairwise Relationships Between Subjects", y=1.02)
plt.show()

# 3. Correlation heatmap
plt.figure(figsize=(8, 6))
correlation = df[subjects].corr()

sns.heatmap(correlation,
            annot=True,
            cmap='coolwarm',
            fmt='.2f',
            linewidths=0.5)

plt.title("Correlation Heatmap of Subject Scores")
plt.show()