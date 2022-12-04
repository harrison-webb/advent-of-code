#Advent of Code #2 part 2
#a list of passwords is given in the format of position1-position2 char: password
#indcies of password start at 1
#Check a .txt file for the number of valid passwords

numValid = 0

with open('input.txt', 'r') as file:
    for line in file:
        parameters, password = line.split(':') #gives ['lBound-uBound char', 'password']
        position1, parameterSection = parameters.split('-') #gives ['lBound', 'uBound char']
        position2, character = parameterSection.split(' ')
        a = (password[int(position1)] == character) #password index is not altered because
        b = (password[int(position2)] == character) #there is a whitespace char at beginning of string
        if(a and not b) or (b and not a):
            numValid = numValid + 1

print("Number of valid passwords: " + str(numValid))

