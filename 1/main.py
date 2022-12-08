# find the top Elf
def first_part():
    my_max = 0
    my_index = 0

    with open("1/input", 'r') as f:
        line = f.readline()
        actual_sum = 0
        actual_index = 0
        while line:
            if line == "\n":
                # check if actual_sum > my_max
                if actual_sum > my_max:
                    my_max = actual_sum
                    my_index = actual_index
                # set actual_sum = 0
                actual_sum = 0
                actual_index += 1
            else:
                actual_sum += int(line)
            line = f.readline()
    print(f'Elf {my_index} carrying {my_max} calories')

# find the top 3 Elfs
def second_part():
    top_three = [0 for _ in range(3)]
    with open("1/input", 'r') as f:
        line = f.readline()
        actual_sum = 0
        while line:
            if line == '\n':
                # check if actual_sum > min(top_three)
                my_min = min(top_three)
                if actual_sum > my_min:
                    top_three[top_three.index(my_min)] = actual_sum
                # set actual_sum = 0
                actual_sum = 0
            else:
                actual_sum += int(line)
            line = f.readline()
    # calculate total of list
    total = sum(top_three)
    print(f'Elfs are carrying {total} calories')

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()