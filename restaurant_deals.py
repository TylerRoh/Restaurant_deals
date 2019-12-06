import requests
import datetime
from bs4 import BeautifulSoup



#monday = 0 sunday = 6
now = datetime.datetime.today().weekday()



def hanger45():
	if now < 4:
		site = requests.get("https://www.tastypizzatogo.com/great-upcoming-events")
		hanger45_soup = BeautifulSoup(site.content, 'html.parser')
		hanger45_parsed = hanger45_soup.find('div', {'id': 'tasty_happenings'})
		hanger45_deals = hanger45_parsed.find_all('li')
		print(hanger45_deals[now])
	elif now > 4:
		site = requests.get("https://www.tastypizzatogo.com/great-upcoming-events")
		hanger45_soup = BeautifulSoup(site.content, 'html.parser')
		hanger45_parsed = hanger45_soup.find('div', {'id': 'tasty_happenings'})
		hanger45_deals = hanger45_parsed.find_all('li')
		print(hanger45_deals[now - 1])
	else:
		print('No deals today')





hanger45()