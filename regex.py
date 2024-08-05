import re

fhand = open('httpspy4e-data.dr-chuck.netregex_sum_2028313.txt')

summ = 0
for line in fhand:
    num = re.findall('[0-9]+',line)
    for n in num:
        n = int(n)
        summ = summ + n

print(summ)
