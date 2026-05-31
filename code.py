import pandas as pd

# Load data
df = pd.read_csv("/content/netflix_titles.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
for col in df.select_dtypes(include='number'):
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include='object'):
    df[col] = df[col].fillna(df[col].mode()[0])

# Standardize text columns
if 'gender' in df.columns:
    df['gender'] = df['gender'].str.strip().str.title()

if 'country' in df.columns:
    df['country'] = df['country'].str.strip().str.title()

# Convert date columns
if 'join_date' in df.columns:
    df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')

# Fix numeric columns
if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce').astype('Int64')

# Save cleaned file
df.to_csv("cleaned_dataset.csv", index=False)

print("Dataset cleaned successfully!")
