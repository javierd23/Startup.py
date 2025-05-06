file = open('test.txt')

hours = {}

for lines in file:
    if lines.startswith('From '):
        line = lines.split()
        time = line[5].split(':')
        hours[time[0]] = hours.get(time[0], 0) + 1


hrs = []

for k, v in hours.items():
    hr = (k, v)
    hrs.append(hr)

hrs = sorted(hrs)
for x,y in hrs:
    print(x,y)






















