from typing import List


def prepare_tests() -> List[List[str]]:
    all_test_intervals = []
    test_count = int(input())
    for _ in range(test_count):
        intervals = []
        intervals_amount = int(input())
        for _ in range(intervals_amount):
            interval = input()
            intervals.append(interval)
        all_test_intervals.append(intervals)
    return all_test_intervals


def validate_intervals(intervals: List[str]):
    intervals_in_seconds = []
    for interval in intervals:
        start, end = interval.split("-")
        start_hours, start_minutes, start_seconds = [int(x) for x in start.split(":")]
        end_hours, end_minutes, end_seconds = [int(x) for x in end.split(":")]

        start_is_valid = (0 <= start_hours < 24 and 0 <= start_minutes < 60 and 0 <= start_seconds < 60)
        end_is_valid = (0 <= end_hours < 24 and 0 <= end_minutes < 60 and 0 <= end_seconds < 60)
        if not all([start_is_valid, end_is_valid]):
            return "NO"

        start_in_seconds = start_hours * 3600 + start_minutes * 60 + start_seconds
        end_in_seconds = end_hours * 3600 + end_minutes * 60 + end_seconds
        if start_in_seconds > end_in_seconds:
            return "NO"

        intervals_in_seconds.append((start_in_seconds, end_in_seconds))

    intervals_in_seconds.sort(key=lambda x: x[0])
    for i in range(1, len(intervals_in_seconds)):
        #  если начало_текущего <= конец_следующего, то есть пересечение
        if not intervals_in_seconds[i-1][1] < intervals_in_seconds[i][0]:
            return "NO"

    return "YES"


if __name__ == '__main__':
    tests = prepare_tests()
    for t in tests:
        print(validate_intervals(t))
