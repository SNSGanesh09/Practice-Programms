#Import Section

import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?q=iphone&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_1_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_1_na_na_na&as-pos=4&as-type=RECENT&suggestionId=iphone&requestId=e8dc90f4-0db5-4a69-b947-4ade7d5e6ce0&as-searchtext=iphone")
#print(response)

soup=BeautifulSoup(response.content,'html.parser')
#print(soup)

names=soup.find_all('div',class_='KzDlHZ')
name=[]
for i in names[0:12]:
    d=i.get_text()
    name.append(d)
#print(name)


prices=soup.find_all('div',class_="Nx9bqj _4b5DiR")
price=[]
for i in prices[0:12]:
    d=i.get_text()
    price.append(d)
#print(price)


reviews=soup.find_all('span',class_="Wphh3N")
review=[]
for i in reviews[0:12]:
    d=i.get_text()
    review.append(d)
#print(review)


features=soup.find_all('li',class_="J+igdf")
feature=[]
for i in features[0:12]:
    d=i.get_text()
    feature.append(d)
#print(feature)


links=soup.find_all('a',class_="CGtC98")
link=[]
for i in links[0:12]:
    d="https://www.flipkart.com"+i['href']
    link.append(d)
#print(link)


images=soup.find_all('img',class_="DByuf4")
image=[]
for i in images[0:12]:
    d=i['src']
    image.append(d)
#print(image)


df=pandas.DataFrame()
#print(df)

data={"Names":name,
      "Prices":price,
      "Reviews":review,
      "Features":feature,
      "Images":image,
      "Links":link,
      }
#print(data)

df=pandas.DataFrame(data)
print(df)

df.to_csv("mobiles_data.csv")