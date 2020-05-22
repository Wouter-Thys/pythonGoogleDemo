letters = ['a','b','c','d']
letters.append('e')             # ['a','b','c','d','e']
print (letters)

print(len(letters))             # 5

letters = letters[0:3]          # ['a','b','c']
print (letters)

letters.insert(2, 'kat')        # ['a','b','kat','c']
print (letters)

print(letters.index('c'))             # 3

letters.sort()                  # ['a','b','c','kat']
print (letters)

#List slice:
myList = [0,1,2,3,4,5]
print(myList[:4])              # [0, 1, 2, 3]
print(myList[4:])              # [4, 5]
print(myList[2:4])             # [2, 3]
print(myList[1:5:2])           # [1, 3]
print(myList[::-1])            # [5, 4, 3, 2, 1, 0]

#String slice:
word = "Banaan"
print(word[0])             # B
print(word[0:3])           # Ban
print(word[5:2:-1])        # naa