from bs4 import BeautifulSoup
import requests
import pandas as pd




url="https://www.allrecipes.com/recipes/17057/everyday-cooking/more-meal-ideas/5-ingredients/main-dishes/"

# other_url="https://www.allrecipes.com/4-ingredient-potato-soup-recipe-8744009"


head=( {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})

webpage=requests.get(url,headers=head)


soup=BeautifulSoup(webpage.content,'html.parser')

listitems=soup.find('section', attrs={'class':"comp taxonomysc mntl-taxonomysc"}).find_all('a')
#print(listitems)
urlList=[]
for listitem in listitems:
    href_value = listitem.get('href')
    urlList.append(href_value)
    #print(f"The href value is: {href_value}")
print(urlList)
