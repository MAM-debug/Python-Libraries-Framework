# 🐼 My Pandas Learning Journey

## ✅ Completed Topics

### 1. DataFrame Basics
- ✅ Import pandas library
- ✅ Create DataFrame from dictionary
- ✅ View DataFrame structure
- ✅ Understand rows and columns

### 2. Selecting Data
- ✅ Select single column: `df['NAME']`
- ✅ Select multiple columns: `df[['NAME', 'GPA']]`
- ✅ Iterate through columns using for loop

### 3. Filtering & Sorting
- ✅ Filter rows with conditions: `df[df['GPA'] > 3.5]`
- ✅ Sort DataFrame: `df.sort_values(by='GPA', ascending=False)`

### 4. Modifying DataFrames
- ✅ Add new columns: `df['GRADES'] = ['A', 'A+', 'B+', 'A']`
- ✅ Drop columns: `df.drop('AGE', axis=1)`

### 5. Statistics & Analysis
- ✅ Full statistics: `df.describe()`
- ✅ Column-specific stats: `df['GPA'].describe()`
- ✅ Individual functions: `.mean()`, `.max()`, `.min()`

### 6. Advanced Indexing
- ✅ Access row by position: `df.iloc[2]`
- ✅ Access multiple rows: `df.iloc[1:3]`
- ✅ Access row by label: `df.loc[1]`
- ✅ Access specific cell: `df.loc[1, 'NAME']`
- ✅ Select row + columns: `df.loc[1, ['NAME', 'GPA']]`
- ✅ Select all rows + columns: `df.loc[:, ['NAME', 'GPA']]`

---

## 📚 Next Topics to Learn

### Working with Files
- ⬜ Read CSV files: `pd.read_csv()`
- ⬜ Save to CSV: `df.to_csv()`
- ⬜ Read Excel files
- ⬜ Handle file encodings

### Multiple Conditions
- ⬜ AND operator: `(condition1) & (condition2)`
- ⬜ OR operator: `(condition1) | (condition2)`
- ⬜ NOT operator: `~condition`

### Data Cleaning
- ⬜ Handle missing values: `.isnull()`, `.fillna()`, `.dropna()`
- ⬜ Remove duplicates: `.drop_duplicates()`
- ⬜ Replace values: `.replace()`
- ⬜ Data type conversion: `.astype()`

### Grouping & Aggregation
- ⬜ GroupBy operations: `.groupby()`
- ⬜ Aggregation functions: `.sum()`, `.count()`, `.mean()`
- ⬜ Pivot tables: `.pivot_table()`

### Advanced Operations
- ⬜ Apply custom functions: `.apply()`
- ⬜ Map values: `.map()`
- ⬜ Merge DataFrames: `.merge()`
- ⬜ Concatenate: `.concat()`

---

## 💻 Practice Code

```python
import pandas as pd

# Create DataFrame
data = {
    'NAME': ['Abdullah', 'Azfar', 'Shaham', 'Ghulam Qadir'],
    'AGE': [20, 19, 21, 20],
    'GPA': [3.5, 3.8, 3.2, 3.6]
}
df = pd.DataFrame(data)

# What I've learned:
# - Select columns: df['NAME'] or df[['NAME', 'GPA']]
# - Filter: df[df['GPA'] > 3.5]
# - Sort: df.sort_values(by='GPA', ascending=False)
# - Add columns: df['GRADES'] = values
# - Drop: df.drop('AGE', axis=1)
# - Stats: df.describe()
# - Access: df.iloc[2] or df.loc[1, 'NAME']
```

---

## 🎯 Current Status
**Level:** Beginner ✨  
**Completed:** 6/15 core topics  
