filled_dict = {
    'firstname': 'Joske',
    'lastname': 'Vermeulen',
    'age': 42,
    'gender': 'male'
    }

    #nieuwe value toevoegen
filled_dict['School'] = 'KdG'
    #value veranderen
filled_dict['age'] = 22
    #value verwijderen
del filled_dict['gender']
    #volledige dicitonary verwijderen
#del filled_dictionary
    #verwijder alle entries in de dictionary
#filled_dictionary.clear()

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    }
for key in prices:
    print ("food = ", key)
    print ("price = ", prices[key])
    print ("stock = ", stock[key])

print(filled_dict['School'])