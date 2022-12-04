#Advent of Code #4
#input is a batch file containing list of 'passports' and their information
#Passports have 8 expected fields:
#
# byr(Birth Year), iyr(Issue Year), eyr(Expiration Year), hgt(Height),
# hcl(Hair Color), ecl(Eye Color), pid(Passport ID), cid(Country ID)
#
#Passports in the batch file are represented as a sequence of key:value fields
# separated by spaces or newlines, and passports are separated by blank lines
#Consider a passport missing any field, except cid, as invalid
passportContainer = []
numValid = 0

def isValidPassport(passport):
    if (('byr' in passport) and ('iyr' in passport) and ('eyr' in passport)
        and ('hgt' in passport) and ('hcl' in passport)
        and ('ecl' in passport) and ('pid' in passport)):
        return True
    else:
        return False

with open('input.txt', 'r') as file:
    for line in file:
        if line != '\n':
            for i in line.strip():          #get outta here whitespace
                passportContainer.append(i) #add contents of lines not separated by \n to the list
        if line == '\n':                    #passports are separated by newlines; this condition denotes end of a passport
            if isValidPassport(''.join(passportContainer)): #turn the list holding passports back into string
                numValid += 1

            passportContainer = [] # 'reset' the list holding the passports

print("Number of valid passports: " + str(numValid))