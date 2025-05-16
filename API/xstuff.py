import urllib.request
import xml.etree.ElementTree as ET
#here we work with XML to parse from the nums in it and sum them.
web = input('Enter a URL: ')
uh = urllib.request.urlopen(web).read()
root = ET.fromstring(uh)


nums =[]
count = root.findall('comments/comment')
for item in count:
    num = item.find('count').text
    if num not in nums:
        nums.append(int(num))

print(sum(nums))

