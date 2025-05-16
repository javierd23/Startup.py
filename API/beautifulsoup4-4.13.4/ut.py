import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Darya.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
links = []
#count =  0

for tag in tags:
    link = (tag.get('href', None))
    link = link.split()
    links.append(link)

    #print(urllib.request.urlopen(links[18], context=ctx).read())

print(links[17])



