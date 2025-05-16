import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter URL: ')

url = url.strip()
address = {}
address['f'] = url

enter = urllib.parse.urlencode(address)

file = urllib.request.urlopen(url)
data = file.read().decode()

js = json.loads(data)

data_split = js['comments']
sm = []
for item in data_split:
     nums = item['count']
     if nums >= 0:
         sm.append(int(nums))
print(sum(sm))