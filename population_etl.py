import pandas as pd

# Step 1: Load the CSV
data = pd.read_csv('us_state_population.csv')
print("\n✅ Full data loaded:")
print(data)

# Step 2: Pivot the data - years become columns
pivot = data.pivot(index='State', columns='Year', values='Population')
print("\n✅ Pivoted data:")
print(pivot)

# Step 3: Check if 2019 and 2020 exist in the columns
if 2019 in pivot.columns and 2020 in pivot.columns:
    # Step 4: Calculate Growth Percentage
    pivot['Growth_%'] = ((pivot[2020] - pivot[2019]) / pivot[2019]) * 100

    # Step 5: Print Growth %
    print("\n✅ Growth % calculated:")
    print(pivot[['Growth_%']])

    # Step 6: Save to CSV
    pivot.to_csv('population_growth.csv')
    print("\n✅ Saved growth data to 'population_growth.csv'.")

else:
    print("\n⚠️ Columns 2019 and 2020 not found. Please check your CSV data.")

