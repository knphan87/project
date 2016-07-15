text = "X-DSPAM-Confidence:    0.8475"
count = 0
index = 0
while index < len(text):
    if text.find('-') > 0:
        count = count + 1
    index = index + 1
print count

stuff=list()
stuff.append('book')
stuff.append(99)
stuff.append('cookie')
print stuff
print 99 in stuff
print 'cookie' in stuff
print 'magaret' in stuff

numList = list()
while True:
    inp = raw_input("Enter number: ")
    if inp == "DONE!": break
    number = float(inp)
    numList.append(number)
average = sum(numList) / len(numList)
print average