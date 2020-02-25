from bs4 import BeautifulSoup

from twilio.rest import Client
import urllib.request
# from htmlpage import url
from distutils.util import strtobool
from var import debug, sendMessage
import time
readLink=''

def main():
 account_sid = "AC4608a11d47e81b63bacf49e971b37a6d"
 auth_token = "fcf596ed60a601fbc910f57c215f0223"
 client = Client(account_sid, auth_token)
 messageBody = ""
 sendMessage=False 
 global readLink
 urlToScrape = 'https://www.amazon.com/Best-Sellers/zgbs'
 f = open('htmlpage.py', mode='a')
 fp = urllib.request.urlopen(str(urlToScrape))
 mybytes = fp.read()
 i = False
 mystr = mybytes.decode("utf8")
 fp.close()
 
 html_doc=mystr
 soup = BeautifulSoup(html_doc, 'html.parser')
 
 
 
 
 
 link = soup.find('a', attrs={'class' : 'a-link-normal'})
 endlink = link['href']
 fulllink = 'amazon.com'+endlink
 # print(link['href'])
 # print(fulllink)
 # print(readLink)
 if fulllink != readLink.lstrip():
   messageBody = 'The number one toy has changed! '
 else:
   messageBody = "The number one toy is the same! "
 f.write("url = '" + fulllink + "'\n") 
 fp = urllib.request.urlopen('https://'+str(fulllink))
 mybytes = fp.read()
 i = False
 mystr = mybytes.decode("utf8")
 fp.close()
 
 html_doc=mystr
 soup2 = BeautifulSoup(html_doc, 'html.parser')
 title = soup2.find('span', attrs={'id' : 'productTitle'}).text
 title = str(title)
 if sendMessage:
  message = client.messages \
                  .create(
                       body="This is the Web-Scraper. " + messageBody + 'The current leader is: '+ title.lstrip().rstrip() +" This can be found here: " + fulllink, 
                       from_='+18607242381',
                       to='+19713419489'
                   )
  print(message.sid)
 if debug:
  print('sendMessage ' + str(sendMessage))
  print('messageBody '+ messageBody)
  print('fulllink '+fulllink)
  print('readlink ' + readLink)
  print('title ' + title.lstrip().rstrip())
 print(messageBody)
 readLink = fulllink
 time.sleep(10)
 main()
main()
