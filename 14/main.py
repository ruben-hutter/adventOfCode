import sys

# define coordinate type
Coordinate = tuple[int, int]

with open("14/test_input", 'r') as f:
    in_file = f.read().splitlines()
    in_file = [[eval(c) for c in l.split(" -> ")] for l in in_file]

POURING_POINT = (500, 0)

coordinates = set()

def first_part():
    # initial rock setup
    for line in in_file:
        for i in range(len(line)-1):
            from_x, from_y = line[i]
            to_x, to_y = line[i+1]
            if from_x == to_x: # vertical line
                for y in range(min(from_y,to_y), max(from_y,to_y)+1):
                    coordinates.add((from_x,y))
            else:
                for x in range(min(from_x,to_x), max(from_x,to_x)+1):
                    coordinates.add((x,from_y))
    # count sand units
    count = 0
    print(f'Sand units: {count}')

def update_coord():
    return

def second_part():
    return

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()