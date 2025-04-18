import pandas as pd

data = pd.read_csv('students.csv')

data['Total'] = data[['Maths', 'Science', 'English']].sum(axis=1)
data['Average'] = data['Total'] / 3

data['Rank'] = data['Total'].rank(ascending=False, method='min').astype(int)

print(" Student Marks Summary:\n")
print(data.sort_values('Rank'))

topper = data.loc[data['Total'].idxmax()]
print(f"\n Class Topper: {topper['Name']} with {topper['Total']} marks")

print("\n Subject-wise Toppers:")
for subject in ['Maths', 'Science', 'English']:
    top_score = data[subject].max()
    topper_name = data.loc[data[subject] == top_score, 'Name'].values[0]
    print(f"{subject} Topper: {topper_name} ({top_score})")

data.sort_values('Rank').to_csv('ranked_students.csv', index=False)
print("\n Ranked data saved to 'ranked_students.csv'")