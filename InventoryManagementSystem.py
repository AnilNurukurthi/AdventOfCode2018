from functools import reduce
from collections import Counter
from itertools import combinations

inventory_ids_file = open('data\input2.txt', 'r')


def get_three_count(box_ids_count):
    return (1 if max(box_ids_count.values()) == 3 else 0)

def get_two_count(box_ids_count):
    return (1 if (2 in box_ids_count.values()) else 0)


def get_checksum():
    box_ids_counter = list(
        map(lambda x: (get_three_count(Counter(x)), get_two_count(Counter(x))), inventory_ids_file.readlines()))
    threes_count, twos_count = reduce(lambda x, y: tuple(map(sum, zip(x, y))), box_ids_counter)
    print(twos_count * threes_count)

def get_common_letters():
    candidate_combo = ()
    combos = list(combinations(inventory_ids_file.readlines(), 2))
    for combo in combos:
        a, b = combo
        str_len = len(combo[0])
        missing_index = -1
        for i in range(len(combo[0])):
            if a[i] == b[i]:
                str_len = str_len - 1
            else:
                missing_index = i
        if str_len == 1:
            print(combo[0][:missing_index] + combo[0][missing_index+1:])
            break

get_common_letters()

