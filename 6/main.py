with open("6/input", 'r') as f:
    line = f.readline()
    
def first_part():
    count = 4
    i = 0
    my_set = set(line[i:i+4])
    while len(my_set) < 4:
        i += 1
        count += 1
        my_set = set(line[i:i+4])
    print(f'Start-of-packet: {count}')

def second_part():
    count = 14
    i = 0
    my_set = set(line[i:i+14])
    while len(my_set) < 14:
        i += 1
        count += 1
        my_set = set(line[i:i+14])
    print(f'Start-of-packet: {count}')

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()