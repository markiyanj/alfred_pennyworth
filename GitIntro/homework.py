from typing import List


def calculate_rooms_number(data: List[List[int]]) -> int:
    """
    There is a list of meetings for office.
    Each meeting should have free room.
    Calculate how many rooms we need to prevent conflicts.

    Args:
        data: List of meetings with time of start and time of end

    Returns: Number of rooms

    Examples:
        calculate_rooms_number([[1, 2], [2, 4]])
        >>> 2
        calculate_rooms_number([[1, 2], [3, 4]])
        >>> 1
        calculate_rooms_number([[1, 2], [3, 4], [1, 5], [6, 7]])
        >>> 2
    """
    if not data:
        return 0
    else:
        room_count = 1
        all_room = len(data) - 1
        for i in range(all_room):
            if data[i + 1][0] - data[i][0] <= 1:
                room_count += 1

        return room_count
