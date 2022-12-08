with open("8/input", 'r') as f:
    lines = f.read().split()

height = len(lines)
width = len(lines[0])

def first_part():
    total_visible = 2*(height-1) + 2*(width-1) # the edge is visible
    grid = [[int(i) for i in lines[j]] for j in range(height)]
    for i in range(1, height-1):
        for j in range(1, width-1):
            # TODO optimise by not calculating max if current <= actual_max
            current = grid[i][j]
            left_max, right_max = max(grid[i][:j]), max(grid[i][j+1:])
            up_max, down_max = (max([line[j] for line in grid[:i]]),
                                max([line[j] for line in grid[i+1:]]))
            if (current > left_max or current > right_max or
                current > up_max or current > down_max):
                total_visible += 1
    print(f'Total visible: {total_visible}')

def second_part():
    return

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()