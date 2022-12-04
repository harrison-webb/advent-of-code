#Advent of Code #2
#a list of passwords is given in the format of lBound-uBound char: password
#lBound and uBound describe the min and max number of occurences of char in the password string
#Objective: determine the number of valid passwords in the list

numValid = 0
lower = None
upper = None
character = None


with open('input.txt', 'r') as file:
    for line in file:
        counter = 0 #counter for tracking #instances of char in each password
        parameters, password = line.split(':') #gives ['lBound-uBound char', 'password']
        lower, parameterSection = parameters.split('-') #gives ['lBound', 'uBound char']
        upper, character = parameterSection.split(' ') #gives ['uBound', 'char']
        for letter in password: #check how many times char is in password
            if letter == character:
                counter += 1

        if counter >= int(lower) and counter <= int(upper): #check if # occurrences of specified num is in range
            numValid = numValid + 1

print("Number of valid passwords: " + str(numValid))



