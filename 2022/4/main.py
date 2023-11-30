def first_part():
    with open("4/input", 'r') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        l, r = line[:-1].split(',')
        l_s, l_e = l.split('-')
        r_s, r_e = r.split('-')
        l_s, l_e, r_s, r_e = [int(i) for i in [l_s, l_e, r_s, r_e]]
        if ((l_s <= r_s and l_e >= r_e) or
            (l_s >= r_s and l_e <= r_e)):
            count += 1
    print(f'Total count: {count}')

def second_part():
    with open("4/input", 'r') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        l, r = line[:-1].split(',')
        l_s, l_e = l.split('-')
        r_s, r_e = r.split('-')
        l_s, l_e, r_s, r_e = [int(i) for i in [l_s, l_e, r_s, r_e]]
        if l_s <= r_e and r_s <= l_e:
            count += 1
    print(f'Total count: {count}')

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()