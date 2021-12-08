import string
import re

file = open('day4.csv', 'r')
lines = file.readlines()
lines = [line.strip('\n' ',') for line in lines]

fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} #, "cid"}
eye = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def check_fields(entry):
    for field in fields:
        if not entry.__contains__(field):
            return False
    return True

def get_value(entry, field):
    values = entry.split(" ")
    for value in values:
        if value.__contains__(field):
            return value.split(":")[1]

def is_valid(field, value):
    if field == "byr":
        if 1920 <= int(value) <= 2002:
            return True
    elif field == "iyr":
        if 2010 <= int(value) <= 2020:
            return True
    elif field == "eyr":
        if 2020 <= int(value) <= 2030:
            return True
    elif field == "hgt":
        if not (value.__contains__('cm') or value.__contains__('in')):
            return False
        if value.__contains__('cm') and (150 <= int(re.findall("\d+", value)[0]) <= 193):
            return True
        elif value.__contains__('in') and (59 <= int(re.findall("\d+", value)[0]) <= 76):
            return True
    elif field == "hcl":
        if value[0] == "#" and len(value) == 7 and all(c in string.hexdigits for c in value[1:7]):
            return True
    elif field == "ecl":
        if eye.__contains__(value):
            return True
    elif field == "pid":
        if len(value) == 9:
            return True

    return False

def further_processing(entry):
    for field in fields:
        if not is_valid(field, get_value(entry, field)):
            return False

    return True

valids = 0
line_no = 0

while line_no < len(lines):
    if lines[line_no] == "":
        continue

    line = ""
    while line_no < len(lines) and lines[line_no] != "":
        line += lines[line_no] + " "
        line_no += 1

    if check_fields(line):
        if further_processing(line): #remove this line for part 1
            valids += 1


    line_no += 1

print(valids)
