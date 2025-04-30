num = 0
cont = 0
plus = 0

file = open(input('File: '))

for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        num = float(line[20:25 + 1])
        plus += num
        cont = cont + 1

print('Average spam confidence:', plus / cont)



