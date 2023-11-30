from copy import deepcopy

with open("11/input", 'r') as f:
    lines = f.read()

lines = [line for line in lines.split('\n\n')] # divides input in paragraphs
lines = [line.split('\n') for line in lines] # divides every paragraph in lines
lines = [[elem.strip() for elem in line] for line in lines] # removes trailing spaces

MONKEYS = []
# [Monkey 0: [[54, 89, 94], 'old * 7', 17, 5, 3], ...]
for line in lines:
    items = [int(i) for i in line[1][16:].split(', ')]
    operation = lambda old, op=line[2][17:]: eval(op)
    test = int(line[3].rsplit(maxsplit=1)[-1])
    if_true = int(line[4].rsplit(maxsplit=1)[-1])
    if_false = int(line[5].rsplit(maxsplit=1)[-1])

    # define monkey as list of the above defined elements
    MONKEYS.append([items, operation, test, if_true, if_false])

# define prime number test0 * test1 * ...
primes = 1
for monkey in MONKEYS:
    primes *= monkey[-3]

def first_part():
    monkeys = deepcopy(MONKEYS)
    inspections = [0 for _ in range(len(monkeys))]
    round_n = 0
    while round_n < 20:
        for idx, monkey in enumerate(monkeys):
            new_items = [monkey[1](old)//3 for old in monkey[0]]
            monkey[0].clear() # remove items from current monkey
            # throw item to next monkey
            for item in new_items:
                inspections[idx] += 1
                if item % monkey[-3] == 0:
                    monkeys[monkey[-2]][0].append(item)
                else:
                    monkeys[monkey[-1]][0].append(item)
        round_n += 1
    inspections.sort()
    most_active_1, most_active_2 = inspections[-2:]
    print(f'Total inspections: {most_active_1 * most_active_2}')

def second_part():
    monkeys = deepcopy(MONKEYS)
    inspections = [0 for _ in range(len(monkeys))]
    round_n = 0
    while round_n < 10000:
        for idx, monkey in enumerate(monkeys):
            new_items = [monkey[1](old)%primes for old in monkey[0]]
            monkey[0].clear() # remove items from current monkey
            # throw item to next monkey
            for item in new_items:
                inspections[idx] += 1
                if item % monkey[-3] == 0:
                    monkeys[monkey[-2]][0].append(item)
                else:
                    monkeys[monkey[-1]][0].append(item)
        round_n += 1
    inspections.sort()
    most_active_1, most_active_2 = inspections[-2:]
    print(f'Total inspections: {most_active_1 * most_active_2}')

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()
