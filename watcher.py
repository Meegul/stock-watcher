import requests
import time
import subprocess

#Clear the terminal
subprocess.call(["clear"], shell=True)

base_url = 'http://www.marketwatch.com/investing/stock/'
stock = 'AMD'
url = base_url + stock

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
last = '0'
while (True):
	r = requests.get(url)
	html = r.text
	parsed_html = BeautifulSoup(html)
	price = parsed_html.body.find('div', attrs={'class':'pricewrap'}).find('p', attrs={'class':'data bgLast'}).renderContents()
	difference = (float(price) - float(last))
	if (difference != 0):
		print stock + ': $' + price + '| $' + str(difference)
	last = price
	time.sleep(1)
