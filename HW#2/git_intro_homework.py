from typing import List


def calculate_rooms_number(data: List[List[int]]) -> int:
    if not data:
        return 0
    else:
        room_count = 1
        l = [y for x in data for y in x]
        len1 = len(l)
        len2 = len(set(l))

        return room_count + len1 - len2
