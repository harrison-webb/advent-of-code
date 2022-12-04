

#d = {1:1, 2:2}
#d.update({3:3})
#print(d)

d = {}
numValid = 0

def has_required_fields(passport):
    if (('byr' in passport) and ('iyr' in passport) and ('eyr' in passport)
        and ('hgt' in passport) and ('hcl' in passport)
        and ('ecl' in passport) and ('pid' in passport)):
        return True
    else:
        return False

def is_valid_passport(passport):
    if has_required_fields(str(passport)):
        byrValid = int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002
        iyrValid = int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020
        eyrValid = int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030
        eclValid = ('amb' or 'blu' or 'brn' or 'gry' or 'grn' or 'hzl' or 'oth') in passport['ecl']
        pidValid = len(passport['pid']) == 9

        if passport['hcl'][0] == '#' and len(passport['hcl']) == 7:
            hclValid = True
        else: 
            hclValid = False

        if 'cm' in passport['hgt']:
            if int(passport['hgt'].split('c')[0]) >= 150 and int(passport['hgt'].split('c')[0]) <= 193:
                hgtValid = True 
        elif 'in' in passport['hgt']:
            if int(passport['hgt'].split('i')[0]) >= 59 and int(passport['hgt'].split('i')[0]) <= 76:
                hgtValid = True
        else:
            hgtValid = False

        if byrValid and iyrValid and eyrValid and eclValid and pidValid and hclValid and hgtValid:
            return True
    return False

with open('input.txt', 'r') as file:
    for line in file:
        if line != '\n':
            for i in line.split():
                a, b = i.split(':')
                d.update({a:b})
        if line == '\n':
            if has_required_fields(str(d)):
                print(d)
            if is_valid_passport(d):
                numValid += 1
            d = {} #reset the dictonary for the next passport

print("Number of valid passports: " + str(numValid))

    