eten = ['spaghedtti', 'frieten','lasagne']
for item in eten:
    print (item)
    if"d"in item:
        print ("Er zit een d in het woord {}".format(item))
        break
else: 
    print ("Alle woorden zijn overlopen en er zat nergens een d in.")

count = 0 
while count <=10:
    print ("ik ben aan ronde: {}".format(count))
    count += 1
else:
    print ("Ik tel niet meer.")