import numpy as np
import pandas as pd

df_aqua = pd.DataFrame({
    'Year': pd.Series([2020, 2020, 2020, 2020, 2020, 2020]),
    'Month name': pd.Series(['Jan', 'Jan', 'Jun', 'Jun', 'Jul', 'Jul']),
    'Month number': pd.Series([1, 1, 6, 6, 7, 7]),
    'Product Name': pd.Series(['Fish', 'Shrimp', 'Fish', 'Shrimp', 'Fish', 'Shrimp']),
    'PROFIT': pd.Series([7415, 3239, 7280, 2007, 3574, 9285]),
    'Company Name': pd.Series(['Pandas', 'Pandas', 'Pandas', 'Pandas', 'Pandas', 'Pandas'])
})

df_athlete = pd.DataFrame({
    'year': [2019, 2019, 2020., 2020, 2020, 2020],
    'date': ['20191103', '20190812', '20200125', '20200129', '20200412', '20200220'],
    'time': ['145509', '135433', '214412', '124254', '123349', '233517'],
    'medal': ['Gold', 'Bronze', 'Silver', 'Bronze', 'Silver', 'Silver'],
    'name': ['Wayne', 'Robert', 'Ashley', 'Jamie', 'Jessie', 'Sergio'],
    'left_handed': [1, 0, 0, 0, 1, 0]
})

df_job = pd.DataFrame({
    'worker': [
        'Wayne', 'Robert', 'Ashley',
        'Jamie', 'Jessie', 'Sergio',
        'Harry', 'Johnny', 'Aaron'
    ],
    'age': [8, 37, 25, 26, 80, 30, 20, 31, 28],
    'job': [
        'Student', 'Data Scientist', 'DATA ANALYST',
        'data engineer', 'Retired', 'Business Intelligence',
        'Student', 'Data Analyst', 'AI Engineer'
    ],
    'years_on_job': [0, 12, 2, 6, 0, 18, 12, 2, 8]
})

df_trade = pd.DataFrame({
    'year': pd.Series([2017, 2018, 2019, 2020]),
    'country': pd.Series([
        'United\nKingdom  ',
        '  United\nKingdom',
        'United    Kingdom',
        ' United Kingdom\n']),
    'export': pd.Series([5466, 8558, 8435, 8435]),
    'import': pd.Series([1546, 3546, 2007, 3574])
})

df_shrimp = pd.DataFrame({
    'date': ['2020-01-01', '2020-01-02', '2020-01-03'],
    'commodity': ['Shrimp, frozen, chem free', 'Shrimp, frz, chemical-free', 'Prawn, frz, chemical-free'],
    'price': [10, 13, 14],
    'unit': ['usd/kg', 'USD/KG', 'USD/kg']
})

df_info = pd.DataFrame({
    'customer_id': [3, 423, 5464],
    'phone': [363334444, 913334444, 123334444],
    'name': ['Jack', 'James', 'Gabriel'],
    'information': ['England Male', 'Colombia Male', 'France Female']
})

df_football = pd.DataFrame({
    'first_name': ['Wayne', 'Cristiano', 'Lionel'],
    'last_name': ['Rooney', 'Ronaldo', 'Messi'],
    'position': ['Second Striker', 'Left Winger', 'Right Winger']
})

df_report = pd.DataFrame({
    'year': pd.Series([2019, 2019, 2020, 2020, 2020, 2020]),
    'company': pd.Series(['Pandas', 'Numpy', 'Pandas', 'Numpy', 'Numpy', 'Pandas']),
    'sales': pd.Series([5466, 8558, 8435, 7280, 9285, 6650]),
    'profit': pd.Series([1546, 3546, 3574, 3352, 4678, 2007])
})

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