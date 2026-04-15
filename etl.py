import pandas as pd

# EXTRACT
print("Reading data from CSV file")

df = pd.read_csv("data.csv", encoding='utf-8')

print("\nOriginal Data:")
print(df.head())


# TRANSFORM
print("\nCleaning data...")

# 1.Remove duplicates 
df = df.drop_duplicates()

# 2. Handling  missing values here we fill missing values with default values
df['product'] = df['product'].fillna("Unknown")
df['price'] = df['price'].fillna(0)
df['quantity'] = df['quantity'].fillna(1)

# 3. Converting  data types
df['price'] = df['price'].astype(float)
df['quantity'] = df['quantity'].astype(int)

# 4. Create new column
df['total_price'] = df['price'] * df['quantity']

# 5.Standardize text columns
df['product'] = df['product'].str.title()
df['category'] = df['category'].str.title()



# LOAD

print("\nSaving cleaned data...")

df.to_csv("cleaned_data.csv", index=False)



# VALIDATION

print("\nValidation:")

print("Total rows after cleaning:", len(df))
print("Missing values:\n", df.isnull().sum())


print("\nCleaned Data Preview:")
print(df.head())

print("\nETL Process Completed Successfully so far!")