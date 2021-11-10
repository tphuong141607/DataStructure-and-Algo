
# Input = array 
# Time complexity = O(nlogn)
# Space complexity = O(logn): Quicksort with in-place uses only constant additional space before making any recursive call. 
# Quicksort must store a constant amount of info for each nested recursive call, thus O(logn)

# Partitioning process: putting the number (aka. pivot) in the correct position (numbers on the left < n < numbers on the right)
# 2 popular partition shemes:
#     1. Hoare Partition
#     2. Lomuto Partition

# HOARE (What we implement here)
# 1. Pick a pivot (let's do the 1st element)
# 2. Compare start to pivot until start > pivot --> Found
# 3. Compare end to pivot until end < pivot     --> Found
# 4. Swap start and end, repeat the process 
# 5. Repeat the process (recursive section)
# 6. When end crosses start, swap end and pivot -- DONE the partitioning process

# LOMUTO 
# 1. Pick a pivot (usually pick the last one)
# 2. The 1st index = The partition index (called p index)
# 3. Compare p with pivot until you find a value that is greater than pivot 
# 4. Add another index i and continue to compare i to pivot to find a value that is less than pivot
# 4. ???? Rewatch the video

def swap(idx1, idx2, arr): 
    if idx1 != idx2:
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    
# O(n)
def partition(elements, start, end): 
    pivot_index = start
    pivot_value = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot_value: 
            start += 1
        
        while elements[end] > pivot_value: 
            end -= 1
        
        if (start < end):
            # We found a value less than pivot and a value more than pivot
            swap(start, end, elements) 
    
    swap(end, pivot_index, elements)
    return end

def quick_sort(elements, start, end):
    # In an ideal case, where we break down the array into 2 equal sub arrays, we will have MAXIMUM:
    # log(n) partitioning levels, excluding the 1st partition
    #   for example, the original array's length is 8, the best you can do is: 
    #   level 1:                original array length 8 
    #   level 2:            arr(4)                           arr(4)
    #   level 3:        arr(2) arr(2)                    arr(2) arr(2)
    #   level 4: arr(1) arr(1) arr(1) arr(1)       arr(1) arr(1) arr(1) arr(1)
    #   log2(8) = 3, which is level 2, 3, 4. We don't count the original array level 1.

    if start < end:
        pivot_index = partition(elements, start, end)
        quick_sort(elements, start, pivot_index - 1) # Left partition
        quick_sort(elements, pivot_index + 1, end)  # Right partition
    


if __name__ == '__main__': 
    elements = [11, 9, 29,7,2,15,28]

    tests = [[3, 7, 9, 11], [25, 22, 21, 10], [29, 15, 28],[6], [0]]
    for arr in tests: 
        quick_sort(arr, 0, len(arr) - 1) 
        print(arr)


