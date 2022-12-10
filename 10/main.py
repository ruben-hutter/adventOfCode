with open("10/input", 'r') as f:
    lines = f.read().splitlines()

def first_part():
    signal_strength = 0
    cycle = 0
    reg_x = 1
    for instruction in lines:
        cmd = instruction[:4]
        if cmd == 'addx':
            cycle += 1
            if cycle % 40 == 20:
                signal_strength += cycle * reg_x
            cycle += 1
            if cycle % 40 == 20:
                signal_strength += cycle * reg_x
            reg_x += int(instruction[4:]) # increse register
        else:
            cycle += 1
            if cycle % 40 == 20:
                signal_strength += cycle * reg_x
    print(f'Signal strength: {signal_strength}')

def second_part():
    return

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()