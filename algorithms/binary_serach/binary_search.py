from typing import List
def simple_binary_search(sorted_list:List, search_value):
    high = len(sorted_list) - 1
    low = 0
    mid = high // 2
    while True:
        if search_value == sorted_list[mid]:
            return mid
        elif search_value < sorted_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
        mid = (high - low) // 2