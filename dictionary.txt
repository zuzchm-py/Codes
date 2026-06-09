abreviations = {'SMH': 'shaking my head',
'TY': 'thank you',
'DW': 'do not worry',
'LOL': 'laughing out loud',
'HRU': 'how are you',
'BTW': 'by the way',
'YH': 'yeah'}
while True:
    word = input("Write the abreviation you don't understand here(ALL CAPS!!)")
    if word in abreviations.keys():
        print(abreviations[word])
    else:
        print('We are sorry. The word you searched is not in our database')
