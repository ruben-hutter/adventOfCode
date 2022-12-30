signals = [] # contains tuples of packets

with open("13/test_input", 'r') as f:
    in_packet1, in_packet2, _ = [f.readline().strip() for _ in range(3)]
    while in_packet1:
        signals.append((map(eval, [in_packet1, in_packet2])))
        in_packet1, in_packet2, _ = [f.readline().strip() for _ in range(3)]

def first_part():
    res = 0
    for idx, signal in enumerate(signals):
        packet1, packet2 = signal
        cmp_res = compare(packet1, packet2, 0)
        if cmp_res == 0:
            res += idx+1
            print(idx+1)
        else:
            print()
    print(f'Total: {res}')

# if elem1 <= elem2 return 0 else return 1
def compare(packet1, packet2, idx):
    # if list empty
    if not packet1:
        return 0
    elif packet1 and not packet2:
        return 1
    l_len, r_len = len(packet1), len(packet2)
    if idx >= l_len:
        return 0
    elif idx >= r_len:
        return 1
    # if one list and other val -> make val list
    if isinstance(packet1[idx], list) and isinstance(packet2[idx], int):
        packet2[idx] = [packet2[idx]]
    elif isinstance(packet1[idx], int) and isinstance(packet2[idx], list):
        packet1[idx] = [packet1[idx]]
    # if both list -> call recursive
    if isinstance(packet1[idx], list) and isinstance(packet2[idx], list):
        if compare(packet1[idx], packet2[idx], 0) == 1:
            return 1
    # both are values
    if packet1[idx] > packet2[idx]:
        return 1
    if compare(packet1, packet2, idx+1) == 1:
        return 1
    return 0

def second_part():
    return

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()