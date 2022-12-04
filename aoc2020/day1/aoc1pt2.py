#Advent of Code #1 part two
#go through a list of numbers, find which three sum to 2020, then
#find the product of these three numbers

a = 0
b = 0
c = 0
fileList = []
with open('input.txt', 'r') as file:
    for line in file:
        fileList.append(int(line))

for i in range(len(fileList)-2):
    for j in range(i+1, len(fileList)-1):
        for k in range(j+1, len(fileList)):
            if fileList[i] + fileList[j] + fileList[k] == 2020:
                a = fileList[i]
                b = fileList[j]
                c = fileList[k]

result = a*b*c
print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))
print("a*b*c = " + str(result))  