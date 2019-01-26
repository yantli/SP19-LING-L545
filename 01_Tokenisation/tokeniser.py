import sys

line = sys.stdin.readline()
abbrev = ['a. m.', 'p. m.', 'Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Prof.']
replacement = []
punctuation = [',', '.', ':', '!', '?', '...']

while line:
    i = 0
    for element in abbrev:
        if element in line:
            line = line.replace(element, '@'+str(i)+'@')
            replacement.append(element)
            i += 1
    line = line.replace('. ', '.\n')


    lines = line.split("\n")
    for l in lines:
        print ('\n')
        if len(l) > 1:
           wordlist = l.split(" ")
           for word in wordlist:
               if len(word) > 1:
                   if word[-1] in punctuation:
                       x = wordlist.index(word)
                       wordlist.pop(x)
                       wordlist.insert((x), word[:-1])
                       wordlist.insert((x+1), word[-1])

           for i in range(0, len(replacement)):
               if '@'+str(i)+'@' in wordlist:
                   y = wordlist.index('@'+str(i)+'@')
                   wordlist.pop(y)
                   wordlist.insert(y, replacement[i])
           for i in range(0, len(wordlist)):
                print (i+1, '\t', wordlist[i])


    line = sys.stdin.readline()



