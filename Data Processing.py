#########################     SQLite操作   #########################

from sqlalchemy import create_engine
import pandas as pd
from pandas.io import sql

# 建立一個 csv 檔資料
data = pd.read_csv('input.csv')
# 先建一個 DB engine
engine = create_engine('sqlite:///:memory:')
# 將建立的 CSV 檔 存入剛剛建立的 DB
data.to_sql('data_table', engine)
# 讀取Data_table的資料
res1 = pd.read_sql_query('SELECT * FROM data_table', engine)
print('\n\n')
print(res1)
# 讀取特定資料
res2 = pd.read_sql_query('SELECT dept,sum(salary) FROM data_table group by dept', engine)
print(res2)
# 插入一筆新增的資料
sql.execute('INSERT INTO data_table VALUES(?,?,?,?,?,?)', engine, params=[('id',9,'Ruby',711.20,'2015-03-27','IT')])
res3 = pd.read_sql_query('SELECT ID,Dept,Name,Salary,start_date FROM data_table', engine)
print(res3)
# 刪除一筆資料
sql.execute('Delete from data_table where name = (?) ', engine,  params=[('Rick')])
res4 = pd.read_sql_query('SELECT ID,Name,Salary,start_date,Dept FROM data_table', engine)
print(res4)

#########################     Date and Time   #########################

import datetime

print("The Date today is : ", datetime.datetime.today())
date_today = datetime.date.today()
no_of_days = datetime.timedelta(days = 7)
before_7_days = date_today - no_of_days
print(before_7_days)

print(date_today)
print('This Year        :', date_today.year)
print('This Month       :', date_today.month)
print('Month Name       :', date_today.strftime('%B'))
print('This Week Day    :', date_today.day)
print('Week Day Name    :', date_today.strftime('%A'))
day1 = datetime.date(2018,2,12)
print("day1",date_today.ctime())

#########################     Data Wrangling   #########################

import pandas as pd

left = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5']
})
right = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5']
})
test = pd.concat([left,right])
print(pd.concat([left,right]))
print("\n")
grouped = test.groupby('subject_id')
print(grouped.get_group("sub2"))
print("\n")
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print(df)
print("\n")
grouped = df.groupby('Rank')
print(grouped.get_group(1))

#########################     Data Aggregation   #########################

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])

print(df)

r = df.rolling(window=3,min_periods=1)
print(r)

#########################  Processing Unstructured Data  #########################

filename = 'input.csv'  

with open(filename) as fn:  

# Read each line
   ln = fn.readline()

# Keep count of lines
   lncnt = 0
   while ln:
       print("Line {}: {}".format(lncnt+1, ln.strip()))
       ln = fn.readline()
       lncnt += 1
       print(lncnt)
           