file = open("FaroesteCaboclo.txt", "r")
dictionary = {}

for lineNumber, line in enumerate(file.readlines()):
    for word in line.strip().split(' '):
        if( len(word) > 2):
            if word not in dictionary:                
                    dictionary.update({word:[lineNumber]})            
            else:
                dictionary[word].append(lineNumber)

for word, lines in dictionary.items():
     print(word, lines)