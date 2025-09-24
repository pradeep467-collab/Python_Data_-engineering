import pandas as pd
import sqlite3
import requests
from bs4 import BeautifulSoup

url='https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
csv_path='/home/project/top_25_films.csv'
retrict_limt=25
df=pd.DataFrame(columns=["Film","Year","RottenTomatoes"])
count=0

html_page=requests.get(url).text
data=BeautifulSoup(html_page,'html.parser')

header=data.find_all('tbody')
rows=header[0].find_all('tr')

for row in rows:
    if count<25:
        col=row.find_all('td')
        if(len(col)!=0 and col[2].contents[0]=='2017'):
            data_dict={"Film":col[1].contents[0],
                       "Year":col[2].contents[0],
                       "RottenTomatoes":col[3].text.strip()
                       }
            df1= pd.DataFrame(data_dict,index=[0]) 
            df=pd.concat([df,df1],ignore_index=True)
            count+=1
    else:
        break

print(df)

df.to_csv(csv_path)
                
