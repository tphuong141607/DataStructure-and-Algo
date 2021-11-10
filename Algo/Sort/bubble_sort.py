# Input = array 
# Time Complexity = O(n^2)
# Space Complexity = O(1)


# You bubble up the largest number at each iteration
# So the array will be sorted starting with the right side (biggest number)
def bubble_sort(arr): 
    total_iterations = len(arr) - 1 
    # - 1 because we are comparing a pair, not a single value
        # For example [a, b, c, d]: 
        #   if value: we need to loop 4 times
        #   if pair: we need to loop (a,b), (b,c), (c,d) 3 times

    # after adding the swapped, the time complexity is O(n) for SORTED array
    # These 2 loops, where the inner decay over each iteration, is the example of the Sum of integer O(n^2)
    for i in range(total_iterations):             
        swapped = False 
        for y in range(total_iterations - i): 
            if (arr[y] > arr[y + 1]):  
                arr[y], arr[y + 1] = arr[y + 1], arr[y] #swap
                swapped = True
                # print(arr)
        if not swapped: 
            return arr 
    return arr
                
if __name__ == "__main__": 
    arr = [38, 9, 29, 7, 2, 15, 28]
    arr = [9,8,7,6,5,4,3,2,1]
    print(bubble_sort(arr))

           