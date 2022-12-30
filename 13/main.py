from functools import cmp_to_key

def first_part():
    signals = [] # contains tuples of packets
    with open("13/input", 'r') as f:
        in_packet1, in_packet2, _ = [f.readline().strip() for _ in range(3)]
        while in_packet1:
            signals.append((map(eval, [in_packet1, in_packet2])))
            in_packet1, in_packet2, _ = [f.readline().strip() for _ in range(3)]
    res = 0
    for idx, signal in enumerate(signals):
        packet1, packet2 = signal
        if compare(packet1, packet2) == -1:
            res += idx+1
    print(f'Total: {res}')

# if elem1 <= elem2 return 0 else return 1
def compare(packet1, packet2):
    # if one list and other val -> make val list
    if isinstance(packet1, list) and isinstance(packet2, int):
        packet2 = [packet2]
    elif isinstance(packet1, int) and isinstance(packet2, list):
        packet1 = [packet1]
    # if both list -> call recursive
    if isinstance(packet1, list) and isinstance(packet2, list):
        return _compare(packet1, packet2)
    # both are values
    if packet1 < packet2:
        return -1
    elif packet2 < packet1:
        return 1
    return 0

def _compare(packet1, packet2):
    idx = 0
    l_len, r_len = len(packet1), len(packet2)
    while idx < l_len and idx < r_len:
        res = compare(packet1[idx], packet2[idx])
        if res == -1:
            return -1
        elif res == 1:
            return 1
        idx += 1
    if idx == l_len:
        if l_len == r_len:
            return 0
        return -1
    return 1

def second_part():
    signals = [[[2]], [[6]]] # packets
    with open("13/input", 'r') as f:
        signals.extend([eval(packet) for packet in f.read().splitlines() if packet])
    sorted_signals = sorted(signals, key=cmp_to_key(compare))
    print(f'Result: {(sorted_signals.index([[2]])+1) * (sorted_signals.index([[6]])+1)}')

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()