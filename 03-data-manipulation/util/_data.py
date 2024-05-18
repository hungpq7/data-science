import numpy as np
import pandas as pd

df_aqua = pd.DataFrame(
    columns=['Year', 'Month name', 'Month number', 'Product Name', 'PROFIT', 'Company Name'],
    data = [
        (2020, 'Jan', 1, 'Fish', 7415, 'Pandas'),
        (2020, 'Jan', 1, 'Shrimp', 3239, 'Pandas'),
        (2020, 'Jun', 6, 'Fish', 7280, 'Pandas'),
        (2020, 'Jun', 6, 'Shrimp', 2007, 'Pandas'),
        (2020, 'Jul', 7, 'Fish', 3574, 'Pandas'),
        (2020, 'Jul', 7, 'Shrimp', 9285, 'Pandas')
    ]
)

df_athlete = pd.DataFrame(
    columns=['year', 'date', 'time', 'medal', 'name', 'left_handed'],
    data=[
        (2019, '20191103', '145509', 'Gold', 'Wayne', 1),
        (2019, '20190812', '135433', 'Bronze', 'Robert', 0),
        (2020, '20200125', '214412', 'Silver', 'Ashley', 0),
        (2020, '20200129', '124254', 'Bronze', 'Jamie', 0),
        (2020, '20200412', '123349', 'Silver', 'Jessie', 1),
        (2020, '20200220', '233517', 'Silver', 'Sergio', 0)
    ]
)

df_job = pd.DataFrame(
    columns=['worker', 'age', 'job', 'years_on_job'],
    data = [
        ('Wayne', 8, 'Student', 0),
        ('Robert', 37, 'Data Scientist', 12),
        ('Ashley', 25, 'DATA ANALYST', 2),
        ('Jamie', 26, 'data engineer', 6),
        ('Jessie', 80, 'Retired', 0),
        ('Sergio', 30, 'Business Intelligence', 18),
        ('Harry', 20, 'Student', 12),
        ('Johnny', 31, 'Data Analyst', 2),
        ('Aaron', 28, 'AI Engineer', 8),
    ],
)

df_trade = pd.DataFrame(
    columns=['year', 'country', 'export', 'import'],
    data = [
        (2017, 'United\nKingdom  ', 5466, 1546),
        (2018, '  United\nKingdom', 8558, 3546),
        (2019, 'United    Kingdom', 8435, 2007),
        (2020, ' United Kingdom\n', 8435, 3574)
    ]
)

df_shrimp = pd.DataFrame(
    columns=['date', 'commodity', 'price', 'unit'],
    data=[
        ('2020-01-01', 'Shrimp, frozen, chem free', 10, 'usd/kg'),
        ('2020-01-02', 'Shrimp, frz, chemical-free', 13, 'USD/KG'),
        ('2020-01-03', 'Prawn, frz, chemical-free', 14, 'USD/kg')
    ]
)

df_info = pd.DataFrame(
    columns=['customer_id', 'phone', 'name', 'information'],
    data=[
        (3, 363334444, 'Jack', 'England Male'),
        (423, 913334444, 'James', 'Colombia Male'),
        (5464, 123334444, 'Gabriel', 'France Female')
    ]
)

df_football = pd.DataFrame(
    columns=['first_name', 'last_name', 'position'],
    data=[
        ('Wayne', 'Rooney', 'Second Striker'),
        ('Cristiano', 'Ronaldo', 'Left Winger'),
        ('Lionel', 'Messi', 'Right Winger')
    ]
)

df_report = pd.DataFrame(
    columns=['year', 'company', 'sales', 'profit'],
    data=[
        (2019, 'Pandas', 5466, 1546),
        (2019, 'Numpy', 8558, 3546),
        (2020, 'Pandas', 8435, 3574),
        (2020, 'Numpy', 7280, 3352),
        (2020, 'Numpy', 9285, 4678),
        (2020, 'Pandas', 6650, 2007)
    ]
)

df_covid_full = pd.DataFrame(
    columns=['country', 'cases', 'deaths', 'recovered', 'area'],
    data = [
        ('USA', 4169991, 147333, 1979617, 'North America'),
        ('Brazil', 2289951, 84207, 1570237, 'South America'),
        ('India', 1288130, 30645, 817593, 'Asia'),
        ('Russia', 795038, 12892, 580330, 'Europe'),
        ('South Africa', 408052, 6093, 236260, 'Africa'),
        ('Peru', 371096, 17645, 255945, 'South America'),
        ('Mexico', 370712, 41908, 236209, 'North America'),
        ('Chile', 338759, 8838, 311431, 'South America'),
        ('Iran', 284034, 15074, 247230, 'Asia'),
        ('Italy', 245338, 35029, 197842, 'Europe'),
    ],
)

df_covid_missing = df_covid_full.copy()
df_covid_missing.loc[[1, 2, 4, 5, 7, 9], 'recovered'] = None
df_covid_missing.loc[[0, 4], 'deaths'] = None
df_covid_missing.loc[[3, 8], 'area'] = None

df_student = pd.DataFrame(
    columns=['student_id', 'gender'],
    data=[
        ('010001', 'Male'),
        ('030001', 'Female'),
        ('070001', 'Female'),
        ('080001', 'Female'),
        ('110001', 'Male'),
        ('120001', 'Female')
    ]
)

df_sales = pd.DataFrame(
    columns=['color', '2000 Q1', '2000 Q2', '2000 Q3', '2000 Q4'],
    data=[
        ['red', 1000, 1200, 1500, 1700],
        ['green', 1500, 1500, 1575, 1800],
        ['blue', 2000, 2200, 2000, 2800]
    ]
)

df_long = pd.DataFrame(
    columns=['Market', 'Color', 'Size', 'Price', 'Sales'],
    data=[
        ('Asian', 'Red', 'Large', 17, 68000),
        ('Asian', 'Red', 'Small', 11, 44000),
        ('Asian', 'Blue', 'Large', 19, 57000),
        ('Asian', 'Blue', 'Small', 13, 52000),
        ('Europe', 'Red', 'Large', 18, 81000),
        ('Europe', 'Red', 'Small', 12, 72000),
        ('Europe', 'Blue', 'Large', 20, 90000),
        ('Europe', 'Blue', 'Small', 14, 77000)
    ]
)

df_sales_2000 = pd.DataFrame(
    columns=['year', 'quarter', 'target', 'sales'],
    data=[
        (2000, 1, 40000, 35000),
        (2000, 2, 50000, 38000),
        (2000, 3, 70000, 78000),
        (2000, 4, 85000, 90000)
    ]
)

df_sales_2001 = pd.DataFrame(
    columns=['year', 'quarter', 'target', 'sales', 'profit'],
    data=[
        (2001, 1, 50000, 60000, 20000),
        (2001, 2, 60000, 65000, 21000),
        (2001, 3, 70000, 82000, 27000),
        (2001, 4, 85000, 94000, 35000)
    ]
)

df_income = pd.DataFrame(
    columns=['name', 'income_before_tax', 'tax_band'],
    data=[
        ('Hannah', 12000, 'Allowance'),
        ('James', 30000, 'Basic'),
        ('Gabriel', 7000, 'Allowance'),
        ('Smith', 20000, 'Basic'),
        ('Alex', 100000, 'Higher')
    ]
)

df_tax = pd.DataFrame(
    columns=['band', 'income_range', 'tax_rate'],
    data=[
        ('Allowance', 'Up to 12,500', 0),
        ('Basic', '12,501 to 50,000', 0.2),
        ('Higher', '50,001 to 150,000', 0.4),
        ('Additional', 'Over 150,000', 0.45)
    ]
)
