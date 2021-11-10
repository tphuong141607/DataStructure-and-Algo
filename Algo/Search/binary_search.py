# Input = Sorted array 
# Time complexity = O(logn)
# Space complexity = O(1)
import sys
sys.path.append('../')
from util import time_it

# Do not try to do min_index = ((max_length - 1) / 2), then enter a half of the array 
# Instead, keep the original array and only playing with indexes (pointers: left and right)

@time_it
def binary_search(sorted_arr, value):
    left_index = 0
    right_index = len(sorted_arr) - 1

    while left_index <= right_index: 
        mid_index = (right_index + left_index) // 2 #  "//" only gets the integer part; also mean taking the floor value
        mid_value = sorted_arr[mid_index]

        if (value == mid_value):
            return mid_index
            
        # Excluding the mid_index, because we already checked it
        if (value > mid_value):
            left_index = mid_index + 1
        if (value < mid_value):
            right_index = mid_index - 1
    return -1

@time_it
def recursive_binary_search (sorted_arr, value, left_index, right_index):
    if (left_index > right_index): 
        return -1

    mid_index = (right_index + left_index) // 2 #  "//" only gets the integer part; also mean taking the floor value
    mid_value = sorted_arr[mid_index]

    if (value == mid_value):
        return mid_index
    if (value > mid_value): 
        left_index = mid_index + 1
    if (value < mid_value):
        right_index = mid_index - 1

    return recursive_binary_search(sorted_arr, value, left_index, right_index) 
        
# EXERCISE: Find indexes of all the occurances of a number from sorted list
# O(log n + r + l) We know that (r + l) =< n
def find_all_occurances(sorted_array, value): 
    found_index = binary_search(sorted_array, value) # O(logn)
    if found_index == -1: return -1
    found_indexes = [found_index]

    for i in range(found_index + 1, len(sorted_array)): # O(r)
        if(sorted_array[i] == value):
            found_indexes.append(i)
        else:
            break
    
    idx = found_index - 1

    while (idx >= 0): # O(l)
        if(sorted_array[idx] == value):
            found_indexes.append(idx)
            idx -= 1
        else:
            break
    return found_indexes


if __name__ == '__main__':
    arr = [4, 9, 11, 17, 21, 25, 29, 32, 38] # len = 9 
    
    # Always check corner cases: 4, 38 
    # n_to_find = 38
    # print(binary_search(arr, n_to_find))
    # print(recursive_binary_search(arr, n_to_find, 0, len(arr) - 1))

    # Example Walk thru: Find 17
    # iter 1: [4, 9, 11, 17, 21, 25, 29, 32, 38]
    #      left_index = 0 | right_index = 8
    #      mid_index = (8 + 0) // 2 = 4
    #      mid_value = 21, which is > 17 
    # iter 2: [4, 9, 11, 17] 21, 25, 29, 32, 38
    #      left_index = 0 | right_index = 3
    #      mid_index = (3 + 0) // 2 = 1
    #      mid_value = 9, which is < 17 
    # iter 3: 4, 9, [11, 17] 21, 25, 29, 32, 38
    #      left_index = 2 | right_index = 3
    #      mid_index = (2 + 3) // 2 = 2
    #      mid_value = 11, which is < 17 
    # iter 4: 4, 9, 11, [17] 21, 25, 29, 32, 38
    #      left_index = 3 | right_index = 3
    #      mid_index = (3 + 3) // 2 = 3
    #      mid_value = 17, which is = 17 FOUND!

    
    # EXERCISE: 
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15
    indices = find_all_occurances(numbers, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")
  




