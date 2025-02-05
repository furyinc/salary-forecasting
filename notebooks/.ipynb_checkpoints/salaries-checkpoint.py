import pandas as pd
import matplotlib.pyplot as plt


# Source: https://www.stat.uz/uz/rasmiy-statistika/labor-market-2


# Load the dataset
file_path = r"C:\Users\Frila\Desktop\pythonx\data_stack\sdmx_data_500.csv"
data = pd.read_csv(file_path)

# Extract year columns
years = ['2017', '2018', '2019', '2020', '2021', '2022', '2023']
salaries = data.loc[0, years].astype(float)

# Calculate percentage growth
growth_rates = salaries.pct_change() * 100

# Line chart for salary trends
plt.figure(figsize=(10, 6))
plt.plot(years, salaries, marker='o', label='Average Monthly Salary')
plt.title('Average Monthly Salary Trend (Uzbekistan)')
plt.xlabel('Year')
plt.ylabel('Salary (UZS)')
plt.grid(True)
plt.legend()
plt.show()

# Bar chart for growth rates
plt.figure(figsize=(10, 6))
plt.bar(years[1:], growth_rates[1:], color='skyblue')
plt.title('Year-on-Year Salary Growth Rates')
plt.xlabel('Year')
plt.ylabel('Growth Rate (%)')
plt.grid(axis='y')
plt.show()
