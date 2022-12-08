with open("8/input", 'r') as f:
    lines = f.read().split()

height = len(lines)
width = len(lines[0])

# create map as grid
grid = [[int(i) for i in lines[j]] for j in range(height)]

def first_part():
    total_visible = 2*(height-1) + 2*(width-1) # the edge is visible
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
    highest_scenic_score = 0
    for i in range(1, height-1):
        for j in range(1, width-1):
            current = grid[i][j]
            # check how many visible in any direction
            up, down = check_up(current, i, j), check_down(current, i, j)
            left, right  = check_left(current, i, j), check_right(current, i, j)
            actual_scenic_score = up * left * right * down
            if actual_scenic_score > highest_scenic_score:
                highest_scenic_score = actual_scenic_score
    print(f'Highest scenic score: {highest_scenic_score}')

def check_up(current, actual_row, actual_col):
    viewing_distance = 1
    for n in [line[actual_col] for line in grid[:actual_row]][::-1]:
        if current <= n:
            break
        viewing_distance += 1
    return min(viewing_distance, actual_row)

def check_down(current, actual_row, actual_col):
    viewing_distance = 1
    for n in [line[actual_col] for line in grid[actual_row+1:]]:
        if current <= n:
            break
        viewing_distance += 1
    return min(viewing_distance, height-1-actual_row)

def check_left(current, actual_row, actual_col):
    viewing_distance = 1
    for i in grid[actual_row][actual_col-1::-1]:
        if current <= i:
            break
        viewing_distance += 1
    return min(viewing_distance, actual_col)

def check_right(current, actual_row, actual_col):
    viewing_distance = 1
    for i in grid[actual_row][actual_col+1:]:
        if current <= i:
            break
        viewing_distance += 1
    return min(viewing_distance, width-1-actual_col)

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()