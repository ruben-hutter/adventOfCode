with open("11/input", 'r') as f:
    monkeys = f.read()

monkeys = [monkey for monkey in monkeys.split('\n\n')]
monkeys = [monkey.split('\n') for monkey in monkeys]
monkeys = [[elem.strip() for elem in monkey] for monkey in monkeys]

# [Monkey 0: [[54, 89, 94], 'old * 7', 17, 5, 3], ...]
for monkey in monkeys:
    items = monkey[1][16:].split(', ')
    operation = lambda old, op=monkey[2][17:]: eval(op)
    test = int(monkey[3].rsplit(maxsplit=1)[-1])
    if_true = int(monkey[4].rsplit(maxsplit=1)[-1])
    if_false = int(monkey[5].rsplit(maxsplit=1)[-1])

    # define monkey as list of the above defined elements
    monkey = [items, operation, test, if_true, if_false]

def first_part():
    return

def second_part():
    return

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()