#Advent of Code #3 part 2
#using the same 'map' from part 1, find how many trees would be 
# encountered when traversing each of the following slopes:
#right 1, down 1
#right 3, down 1
#right 5, down 1
#right 7, down 1
#right 1, down 2
#
#to get the solution to the aoc problem, multiply the #trees for each slope

r1 = 0 #right 1, down 1
r3 = 0 #right 3, down 1
r5 = 0 #right 5, down 1
r7 = 0 #right 7, down 1
d1 = 0 #right 1, down 2

with open('input.txt', 'r') as file:
    for i,line in enumerate(file):
        line = line.strip() #get outta here whitespace
        if line[i % len(line) ] == '#':
            r1 += 1
        if line[(i*3) % len(line)] == '#':
            r3 += 1
        if line[(i*5) % len(line)] == '#':
            r5 += 1
        if line[(i*7) % len(line)] == '#':
            r7 += 1
        if (i % 2 == 0) and (line[(int(i/2)) % len(line)] == '#'):
            d1 += 1

result = r1*r3*r5*r7*d1
print('result: ' + str(result))