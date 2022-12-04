#Advent of Code #1
#go through a list of numbers, find which two sum to 2020, then
#find the product of these two numbers

a = 0
b = 0
fileList = []
with open('input.txt', 'r') as file:
    for line in file:
        fileList.append(int(line))

for i in range(len(fileList)-1):
    for j in range(i+1, len(fileList)):
        if fileList[i] + fileList[j] == 2020:
            a = fileList[i]
            b = fileList[j]

result = a*b
print("result: " + str(result))
