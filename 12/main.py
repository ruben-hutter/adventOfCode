with open("12/test_input", 'r') as f:
    in_file = f.read().splitlines()
    grid = [[ord(letter)-ord('a') for letter in line] for line in in_file]
    # TODO handle case S and E -> save coordinates of nodes and
    # set correct value in grid

print(grid)

# dijkstra algorithm
def first_part():
    return

def second_part():
    return

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()