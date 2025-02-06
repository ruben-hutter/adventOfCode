with open("14/input", 'r') as f:
    in_file = f.read().splitlines()
    in_file = [[eval(c) for c in l.split(" -> ")] for l in in_file]

POURING_POINT = (500, 0) # where sand starts

filled = set() # coordinates that are filled

# initial rock setup
for line in in_file:
    for i in range(len(line)-1):
        from_x, from_y = line[i]
        to_x, to_y = line[i+1]
        if from_x == to_x: # vertical line
            for y in range(min(from_y,to_y), max(from_y,to_y)+1):
                filled.add((from_x,y))
        else:
            for x in range(min(from_x,to_x), max(from_x,to_x)+1):
                filled.add((x,from_y))

max_y = max([c[1] for c in filled]) # terminating condition -> part 1

def first_part():
    # count sand units
    count = 0
    running = sand_sim_1()
    while running:
        count += 1
        running = sand_sim_1()
    print(f'Sand units: {count}')
    return count

def sand_sim_1():
    '''
    Simulates sand placement in part 1.

    Returns:
        bool: True if sand is placed, False otherwise.
    '''
    global filled
    x, y = POURING_POINT

    while y <= max_y:
        if (x,y+1) not in filled:
            y += 1
            continue
        if (x-1,y+1) not in filled:
            x -= 1
            y += 1
            continue
        if (x+1,y+1) not in filled:
            x += 1
            y += 1
            continue
        # sand to set
        filled.add((x,y))
        return True
    return False

def second_part(first_count):
    # count sand units
    count = 1
    while True:
        coord = sand_sim_2()
        # sand to set
        filled.add(coord)
        if coord == POURING_POINT:
            break
        count += 1
    print(f'Sand units: {count + first_count}')

def sand_sim_2():
    '''
    Simulates sand placement in part 2.

    Returns:
        bool: True if sand is placed, False otherwise.
    '''
    global filled
    x, y = POURING_POINT

    if (x,y) in filled:
        return (x,y)
    
    while y <= max_y:
        if (x,y+1) not in filled:
            y += 1
            continue
        if (x-1,y+1) not in filled:
            x -= 1
            y += 1
            continue
        if (x+1,y+1) not in filled:
            x += 1
            y += 1
            continue
        break
    return (x,y)

def main():
    first_count = first_part()
    second_part(first_count)

if __name__ == '__main__':
    main()