import pandas as pd

df = pd.read_csv('miniquizzes/data/salary_data.csv')
df.head()
df.columns = ['Name', 'Job', 'Department', 'Salary', 'Date']
print(df.head())

df['Date']=df['Date'].apply(lambda x: pd.to_datetime(x))

df['Salary']=df['Salary'].apply(lambda x: float(x.strip('$')))


groupby_obj=df.groupby('Job').sum()['Salary'].sort_values(ascending=False)
print(groupby_obj.head())
print(df['Job'].str.contains('Police').count())

print(float(df['Job'].str.contains('Police OFFICER').count())/df['Job'].str.contains('Police').count())
groupby_obj.mean()
groupby_obj.max()
groupby_obj.count()
