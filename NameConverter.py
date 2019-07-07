converter = {'a': 'ka', 'b': 'zu', 'c': 'mi', 'd': 'te', 'e': 'ku', 'f': 'lu', 'g': 'ji', 'h': 'ri', 'i': 'ki',
             'j': 'zu', 'k': 'me', 'l': 'ta', 'm': 'rin', 'n': 'to', 'o': 'mo', 'p': 'no', 'q': 'ke', 'r': 'shi',
             's': 'ari', 't': 'chi', 'u': 'do', 'v': 'ru', 'w': 'me', 'x': 'na', 'y': 'fu', 'z': 'su'}
name = input("Enter your name:")
if name.isalpha():
    lowerName = name.lower()
    oldName = list(lowerName)
    newName = []
    for i in oldName:
        newName.append(converter[i])
    japaneseName = ''.join(newName)
    print("Your Japanese name is:", japaneseName)
else:
    print("Try entering a string")
