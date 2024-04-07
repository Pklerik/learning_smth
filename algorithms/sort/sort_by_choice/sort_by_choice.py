def sort_by_choice(array:list):
    new_array:list = []
    for _ in array:
        smallest_index = find_smallest(array)
        new_array.append(array.pop(smallest_index))
    
def find_smallest(array:list):
    smallest = array[0]
    smallest_index:int = 0
    for index, item in enumerate(array):
        if item < smallest:
            smallest = item
            smallest_index = index
    return smallest_index
