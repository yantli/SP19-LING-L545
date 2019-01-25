import sys

line = sys.stdin.readline()
abbrev = ['a. m.', 'p. m.', 'Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Prof.']
replacement = []
while line:
    i = 0
    for element in abbrev:
        if element in line:
            line = line.replace(element, '@'+str(i)+'@')
            replacement.append(element)
            i += 1
    line = line.replace('. ', '.\n')

    for i in range(0, len(replacement)):
        line = line.replace('@'+str(i)+'@', replacement[i])
        print(line)

    line = sys.stdin.readline()
