with open("10/input", 'r') as f:
    lines = f.read().splitlines()

CRT = [['.' for _ in range(40)] for _ in range(6)]
DRAW = '#'

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
    cycle = 0
    reg_x = 1
    for instruction in lines:
        cmd = instruction[:4]
        if cmd == 'addx':
            cycle += 1
            # check if pixel is drawn
            if (cycle-1)%40 in [reg_x-1, reg_x, reg_x+1]:
                CRT[(cycle-1)//40][(cycle-1)%40] = DRAW
            cycle += 1
            # check if pixel is drawn
            if (cycle-1)%40 in [reg_x-1, reg_x, reg_x+1]:
                CRT[(cycle-1)//40][(cycle-1)%40] = DRAW
            reg_x += int(instruction[4:]) # increse register
        else:
            cycle += 1
            # check if pixel is drawn
            if (cycle-1)%40 in [reg_x-1, reg_x, reg_x+1]:
                CRT[(cycle-1)//40][(cycle-1)%40] = DRAW
    print_crt(CRT)

def print_crt(crt):
    print('CRT result:')
    print(' ' + '-' * 40 + ' ')
    for line in crt:
        print('|' + ''.join(line) + '|')
    print(' ' + '-' * 40 + ' ')

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()