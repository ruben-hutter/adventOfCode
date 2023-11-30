ASCII_LOWER_CASE_A = 97
ASCII_UPPER_CASE_A = 65

def first_part():
    with open("3/input", 'r') as f:
        lines = f.readlines()

    total_score = 0
    for line in lines:
        left = line[:len(line)//2]
        right = line[len(line)//2:-1]
        hashset = set(left)
        for c in right:
            if c in hashset:
                total_score += convert_priority(c)
                break
    print(f'Priorities sum: {total_score}')

def convert_priority(char):
    # read ASCII value of char
    num = ord(char)
    if char.islower():
        return num - ASCII_LOWER_CASE_A + 1
    return num - ASCII_UPPER_CASE_A + 27

def second_part():
    with open("3/input", 'r') as f:
        lines = f.readlines()
    
    total_score = 0
    for i in range(0 ,len(lines), 3):
        hashset1 = set(lines[i][:-1])
        hashset2 = set(lines[i+1][:-1])
        hashset3 = set(lines[i+2][:-1])
        badge = hashset1.intersection(hashset2).intersection(hashset3).pop()
        total_score += convert_priority(badge)
    print(f'Badges priorities sum: {total_score}')

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()