import sqlite3
import pandas as pd

#use SQLite3 to create and connect your process to a new database STAFF
conn=sqlite3.connect('STAFF.db')

table_name='Instructor'
attribute_list=['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

#to read the CSV using Pandas, you use the read_csv() function. Since this CSV does not contain headers, you can use the keys of the attribute_dict
file_path='/home/project/INSTRUCTOR.csv'
df=pd.read_csv(file_path,names=attribute_list)

#to load data to table we use to_sql with additonalatributes if_exists can take (fail,replace,append)
df.to_sql(table_name,conn,if_exists='replace',index=False)
print("table is ready")

#SQL queries can be executed on the data using the read_sql function in pandas.
query_statement=f"Select * from {table_name}"
query_output=pd.read_sql(query_statement,conn)
print(query_statement)
print(query_output)

query_statement=f"select count(1) from {table_name}"
query_output=pd.read_sql(query_statement,conn)
print(query_statement)
print(query_output)


#Adding data to table
data_dict={
            'ID':[100],    
            'FNAME':['Pradeep'],
            'LNAME':['Kumar'],
            'CITY':['Vizag'],
            'CCODE':['VSKP']
            }
data_append=pd.DataFrame(data_dict)

data_append.to_sql(table_name,conn,if_exists='append',index=False)
print("Data appended succefully")

query_statement=f"select count(1) from {table_name}"
query_output=pd.read_sql(query_statement,conn)
print(query_statement)
print(query_output)

#Practise code
table_name2='Departments'
table_attrib=['DEPT_ID','DEP_NAME','MANAGER_ID','LOC_ID']
file_path2='/home/project/Departments.csv'

read_data=pd.read_csv(file_path2,names=table_attrib)

read_data.to_sql(table_name2,conn,if_exists='replace',index=False)
print("Table created")

sql_state=f"select * from {table_name2}"
sql_output=pd.read_sql(sql_state,conn)
print(sql_state)
print(sql_output)

data_dict2={'DEPT_ID':[9],
            'DEP_NAME':['Quality Assurance'],
            'MANAGER_ID':[30010],
            'LOC_ID':['L010']
            }
data_append=pd.DataFrame(data_dict2)
data_append.to_sql(table_name2,conn,if_exists='append',index=False)
print('Appended to department table sucesfully')

sql_state=f"select * from {table_name2}"
sql_output=pd.read_sql(sql_state,conn)
print(sql_state)
print(sql_output)



conn.close()
