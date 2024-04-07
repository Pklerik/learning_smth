import binary_search
from typing import List
def test_binary_search_case_1():
    sorted_list:List = [i for i in range(1, 100)]
    search_value = 6
    assert binary_search.simple_binary_search(sorted_list, search_value) == 5
    
def test_binary_search_case_2():
    sorted_list:List = [i for i in range(1, 100)]
    search_value = 4
    assert binary_search.simple_binary_search(sorted_list, search_value) == 3
    
def test_binary_search_case_4():
    import string
    sorted_list:List = [i for i in string.ascii_lowercase]
    search_value = 'c'
    assert binary_search.simple_binary_search(sorted_list, search_value) == 2