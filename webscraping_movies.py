import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url='https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name='Movies.db'
table_name='Top_50'
csv_path='/home/project/top_50_films.csv'
df=pd.DataFrame(columns=["Average Rank","Film","Year"])
count=0

#Read from URL and parse it uing BeautifulSoup
html_page=requests.get(url).text
data=BeautifulSoup(html_page,'html.parser')

#Finding the table position in the webpage, in thsi case its the 1st table
tables=data.find_all('tbody')
rows=tables[0].find_all('tr')

#Now iterate through rows table to extract teh1st 3 columns and insert them into dataframe
for row in rows:
    if count<50:
       col=row.find_all('td')
       if(len(col)!=0):
        data_dict={"Average Rank":int(col[0].text.strip()),
                   "Film":col[1].text.strip(),
                   "Year":col[2].contents[0]}
        df1=pd.DataFrame(data_dict,index=[0]) 
        df=pd.concat([df,df1],ignore_index=True)
        count+=1
    else:
        break              

#Print Dataframe
print(df)

#Export to csv
df.to_csv(csv_path)

#To write the result to a database
conn=sqlite3.connect(db_name)
df.to_sql(table_name,conn,if_exists='replace',index=False)
conn.close()


