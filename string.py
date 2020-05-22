firstname = "Jake"
lastname = "Doe"
greeting = "Dag " + firstname + " " + lastname
print(greeting)

firstname = "Jane"
lastname = "Doe"
greeting = "Dag %s %s" % (firstname, lastname)
print(greeting) 

firstname = "John"
lastname = "Doe"
greeting = "Dag {} {}".format(firstname, lastname)
print(greeting)

words = "Dit zijn verschillende woorden."
wordList = words.split()
print(wordList)
newWord = "-".join(wordList)
print(newWord)

def censor(text, word):    
    textsplit = text.split()
    
    for index in range(0, len(textsplit)):
        if(textsplit[index] == word):            
            wordlist = list(word)
            for letter in range(0, len(wordlist)):                
                wordlist[letter] = "*"            
            
            newWord = "".join(wordlist)            
            textsplit[index] = newWord
        
    return" ".join(textsplit)
print(censor("jos loser jos loser", "loser")) # jos ***** jos *****