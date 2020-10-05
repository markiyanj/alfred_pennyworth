from typing import List


def calculate_rooms_number(data: List[List[int]]) -> int:
    if not data:
        return 0
    else:
        room_count = 1
        all_room = len(data) - 1
        for i in range(all_room):
            if data[i + 1][0] - data[i][0] <= 1:
                room_count += 1

        return room_count
