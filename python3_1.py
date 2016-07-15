import re
hand = open('regex_sum_234024.txt','r')
numList = hand.read()
words = numList.split()
newList = list()

for word in words:
    num = re.findall('[0-9]+',word)
    if len(num) !=1 : continue
    intNum = int(num[0])
    newList.append(intNum)

sum = 0
for nums in newList:
    sum+=nums
print sum
