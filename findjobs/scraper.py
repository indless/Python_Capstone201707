import requests
from bs4 import BeautifulSoup

url = 'https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Oklahoma+City%2C+OK'
#url = "https://levelupdigitalmarketing.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content)
links = soup.find_all('a')
'''
for link in links:
    if 'http' in link.get('href'):
        print(link.text, link.get('href'))
'''
g_data = soup.find_all('div', {'class': 'info'})
for item in g_data:
    print(item.contents[0].find_all('a', {'class': 'business-name'})[0].text)
    # print(item.contents[1].find_all('p', {'class': 'adr'})[0].text)

    try:
        print(item.contents[1].find_all('span', {'itemprop': 'streetAddress'})[0].text)
    except:
        pass

    try:
        print(item.contents[1].find_all('span', {'itemprop': 'addressLocality'})[0].text.replace(',', ''))
    except:
        pass

    try:
        print(item.contents[1].find_all('span', {'itemprop': 'addressRegion'})[0].text)
    except:
        pass

    try:
        print(item.contents[1].find_all('span', {'itemprop': 'postalCode'})[0].text)
    except:
        pass

    try:
        print(item.contents[1].find_all('li', {'class': 'primary'})[0].text)
    except:
        pass
