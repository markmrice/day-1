input = open('day1input.txt', 'r')
inputList = input.read().split('\n')
outputList = []
for string in inputList:
    firstInt = 0
    lastInt = 0
    index = 0
    for char in string:
        if char.isnumeric():
            firstInt = char
            lastInt = char
            index = string.index(char)
            break
    for i in range(index, len(string)):
        if string[i].isnumeric():
            lastInt = string[i]
    outputList.append(int(str(firstInt) + str(lastInt)))
print(sum(outputList))


