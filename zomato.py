from selenium import webdriver
import getpass,time,string
from bs4 import BeautifulSoup
from pprint import pprint
driver=webdriver.Chrome('chromedriver_linux64/chromedriver')
total=[]
for i in range(1,9):
	total_dict={}
	driver.get('https://www.zomato.com/nagercoil/restaurants?page='+str(i))
	time.sleep(4)
	driver.maximize_window()
	time.sleep(2)
	page=driver.execute_script("return document.documentElement.outerHTML")
	soup=BeautifulSoup(page,'html.parser')
	hotel_name=soup.find_all('div',class_="col-s-12")
	price=soup.find_all('span',class_="col-s-11 col-m-12 pl0")
	timing=soup.find_all('div',class_='res-timing clearfix')
	rating=soup.find_all('div',class_='ta-right floating search_result_rating col-s-4 clearfix')
	page_no=[]
	for j in range(len(price)):
		solo_dict={}
		solo_dict['Hotel Name']=hotel_name[j].find('a').find_next('a').text.strip().strip('\n')
		solo_dict['Price']=price[j].text
		solo_dict['Time']=timing[j]['title']
		ratings=''
		for k in rating[j].text.strip('\n'):
			if k in string.digits or k=='.':
				ratings+=k
			if len(ratings)>=3:
				break
		solo_dict['Rating']=ratings	
		page_no.append(solo_dict)
	total_dict['Page '+str(i)]=page_no
	total.append(total_dict)
	time.sleep(3)
pprint(total)
driver.quit()

