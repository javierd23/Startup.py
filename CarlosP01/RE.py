#this is for regular expression.
import re

file = open('regex_sum_2209539.txt')
sun = []
sun2 = 0
for line in file:
    line = line.strip()
    nums = re.findall('([0-9]+)', line)
    for num in nums: #to be able to only print the number I need to do a for to go thr each one of them.
        sun.append(int(num))


for digit in sun:
    if digit >= 0:
        sun2 += digit

print(sun2)

