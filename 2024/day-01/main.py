'''
1. Parse input file
2. Create sorted list for left and right list (left side separated by right side by white space)
3. Calculate difference between left and right list
'''

import sys


def parse_input_file(input_file):
    '''
    Parse input file and return list of integers
    '''
    left = []
    right = []

    try:
        with open(input_file, 'r') as f:
            for line in f:
                left_side, right_side = line.strip().split(3*' ')
                left.extend(map(int, left_side.split()))
                right.extend(map(int, right_side.split()))
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)
    return left, right


def calculate_difference(left, right):
    '''
    Calculate difference between left and right list
    '''
    left.sort()
    right.sort()
    total_difference = 0
    for i in range(len(left)):
        total_difference += abs(left[i] - right[i])
    return total_difference


if __name__ == '__main__':
    # Parse input file
    input_file = 'input.txt'
    left, right = parse_input_file(input_file)
    total_difference = calculate_difference(left, right)
    print(f'Total difference: {total_difference}')

