# Input = array 
# Time Complexity = O(n^2)
# Space Complexity = O(1) if doing in place

# You create a new array 
# For i in len(array): 
#   insert i to the newly created array
#   do a sort

# BETTER WAY: Do the algorithm IN-PLACE by having a pointer separating the sorted (left side), and unsorted(right side)
import math 
def insertion_sort(elements): 
    for i in range(1, len(elements)): # start with 1 b/c the 1st element is already "sorted"
        anchor = elements[i]
        sorted_index = i - 1

        # Exercise: Print the median of the sorted array
        # median_index = sorted_index / 2
        # print(elements[:i])
        # if median_index == 0: 
        #     median = elements[0]
        # elif (median_index % 1 != 0): # even
        #     median = (elements[math.floor(median_index)] + elements[math.floor(median_index + 1)]) / 2
        # else: # odd
        #     median = elements[math.floor(median_index)]    
        # print(median)  

        # Sorting the left side begins
        while sorted_index >= 0 and anchor < elements[sorted_index]:
            elements[sorted_index + 1] = elements[sorted_index] # Shifting array 
            sorted_index -= 1

        elements[sorted_index + 1] = anchor #sorted_index can run to -1  

    

if __name__ == '__main__':
    elements = [11, 9, 29,7,2,15,28]

    tests = [
        [2,1,5,7,2,0,5]
        # [11, 9, 29,7,2,15,28],
        # [3, 7, 9, 11], 
        # [25, 22, 21, 10], 
        # [29, 15, 28],[6], 
        # [0]
    ]

    for arr in tests: 
        insertion_sort(arr) 
        print(arr)

