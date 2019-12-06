import requests
import datetime
from bs4 import BeautifulSoup


#monday = 0 sunday = 6
now = datetime.datetime.today().weekday()
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def hangar45():
    print("Hangar 45:")
    site = requests.get("https://www.tastypizzatogo.com/great-upcoming-events")
    hangar45_soup = BeautifulSoup(site.content, 'html.parser')
    hangar45_parsed = hangar45_soup.find('div', {'id': 'tasty_happenings'})
    hangar45_deals = hangar45_parsed.find_all('li')
    if now < 4:
        if hangar45_deals[now].find('p') == None:
            print(hangar45_deals[now].find('h5').text)
        else:
            print(hangar45_deals[now].find('h5').text)
            print(hangar45_deals[now].p.text)
    elif now > 4:
        if hangar45_deals[now - 1].find('p') == None:
            print(hangar45_deals[now - 1].find('h5').text)
        else:
            print(hangar45_deals[now - 1].find('h5').text)
            print(hangar45_deals[now - 1].p.text)
    else:
        print('None')
    print('')

def betty_dangers():
    print("Betty Dangers:")
    if now < 5:
        site = requests.get("https://bettydangers.com/happy-hour/")
        betty_soup = BeautifulSoup(site.content, 'html.parser')
        betty_parsed = betty_soup.find('div', {'class': 'entry-content'})
        betty_time = betty_parsed.h5.string   #string contains the time of their happy hour
        betty_deals = betty_parsed.find_all('p')
        print(betty_time)
        for i in betty_deals:
            if i.string != None:
                print(i.string)
    else:
        print('None')
    print('')

def unofficial():
    print("The Unofficial:")
    site = requests.get("https://www.theunofficialdb.com/events")
    unofficial_soup = BeautifulSoup(site.content, 'html.parser')
    if now == 0:
        unofficial_parsed = unofficial_soup.find('div', {'id': 'comp-jmwu61dninlineContent-gridContainer'})
        unofficial_divs = unofficial_parsed.find_all('span')
        print(unofficial_parsed.find('h5').string)
        for i in unofficial_divs[0:-2]:
            print(i.string)

    elif now == 1:
        unofficial_parsed = unofficial_soup.find('div', {'id': 'comp-jhmkw4b1inlineContent-gridContainer'})
        unofficial_divs = unofficial_parsed.find_all('span')
        print(unofficial_parsed.find('h5').string)
        for i in unofficial_divs:
            if i.string != None:
                print(i.string)

    elif now == 2:
        unofficial_parsed = unofficial_soup.find('div', {'id': 'icdrs1yh'})
        unofficial_divs = unofficial_parsed.find('span')
        print(unofficial_divs.string)

    elif now == 3:
        unofficial_parsed = unofficial_soup.find('div', {'id': 'comp-jhmkvzsxinlineContent-gridContainer'})
        unofficial_divs = unofficial_parsed.find_all('p')
        #print(unofficial_parsed.prettify())
        print(unofficial_parsed.find('h5').string)
        print(unofficial_divs[-1].string)

    elif now == 6:
        unofficial_parsed = unofficial_soup.find('div', {'id': 'WRchTxtw-12gn'})
        print(unofficial_parsed.find('h5').string)
        unofficial_parsed = unofficial_soup.find('div', {'id': 'WRchTxt1r'})
        unofficial_spans = unofficial_parsed.find_all('span')
        print(unofficial_spans[-1].string)

    print("3-6 and 9-Midnight\n$3 select drinks\n$5 select apps")
    print('')

def grumpys():
    print("Grumpys:")
    site = requests.get("https://www.grumpys-bar.com/northeast")
    grumpys_soup = BeautifulSoup(site.content, 'html.parser')
    grumpys_div = grumpys_soup.find('section')
    grumpys_div2 = grumpys_div.find_all('div', {'class': 'items'})
    grumpys_when = grumpys_div2[0].find_all('div', {'class': 'when'})
    grumpys_desc = grumpys_div2[0].find_all('div', {'class': 'desc'})
    for i in grumpys_when:
        print(i.string)
        print(grumpys_desc[grumpys_when.index(i)].string)
    print('')

def indeed():
    print('Indeed:')
    if now <= 1:
        print('$2 off pours 8-10pm')
    elif now == 3:
        print('$2 off pours 3-6pm')
    elif now == 4:
        print('$2 off pours 12-6pm')
    else:
        print('None')
    print('')




def show_all():
    unofficial()
    betty_dangers()
    hangar45()
    grumpys()
    indeed()



if __name__ == '__main__':
    show_all()
