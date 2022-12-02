def get_words(sline, start, end):
    return " ".join(sline.split()[start:end])

def loop(key, sline, depth):
    if not key in bags:
        return 0

    if sline == "no other bags.":
        return 1

    temp_line = sline
    count = 0
    total_for_current_bag = 0
    while len(temp_line) > 0:
        next_space = temp_line.find(" ")
        if next_space >= 1:
            count = int(temp_line[0:next_space])

        new_key = get_words(temp_line, 1, 3)

        if not new_key in bags:
            return total_for_current_bag

        new_line = get_words(bags[new_key], 0, len(temp_line))
        loop_result = loop(new_key, new_line, depth + 1)
        total_for_current_bag += count*loop_result

        temp_line = temp_line[temp_line.find(",")+2:]
        if not any(char.isdigit() for char in temp_line):
            break

    return total_for_current_bag + 1

file = open('day7.csv', 'r')
lines = file.readlines()

my_bag_found = 0
bags = dict()
my_bag = "shiny gold"

#create dictionary
for line in lines:
    bags[get_words(line, 0, 2)] = get_words(line, 4, len(line))

result = loop(my_bag, bags[my_bag], 0)
print(bags[my_bag])
#result += sum(int(x) for x in bags[my_bag] if x.isdigit())

print(result - 1)
