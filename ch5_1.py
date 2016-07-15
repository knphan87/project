def action():
    try:
        inp = raw_input("Enter hours: ")
        hours = float(inp)
        inp = raw_input("Enter rate: ")
        rate = float(inp)

        print rate,hours
        if hours <= 40:
            pay = rate * hours
        else:
            pay = rate * 40 + ( rate * 1.5 * ( hours - 40))
        print pay

    except:
        print "Error, please enter numeric input!"
        

while True:
    answer = raw_input("Enter your choices of programs - salary, none or quit: ")
    if answer == "salary":
        action()
    elif answer == "none":
        continue
    elif answer == "quit":
        break
print 'Done!'