def merge_sort(list):
    """ 
    Sorts a list in ascending order 
    Returns a new sorted list 

    Takes O(n log n) time
    """
    if (len(list) <= 1):
        return list

    # O(1)
    left_list, right_list = divide_to_halves(list)

    left = merge_sort(left_list)
    right = merge_sort(right_list) 

    # O(n)
    return merge(left, right)

def divide_to_halves(list): 
    """
    Divide the unsorted list at midpoint into sublists
    Returns 2 sublists 

    Big O: (1)
    """
    middle = len(list) // 2
    left_list = list[:middle] 
    right_list = list[middle:]
    return left_list, right_list


def merge(list1, list2): 
    """ 
    Merges 2 lists, sorting them in the process
    Returns a new merged sorted list 

    Runs in overall O(n) time 
    """
    # O(a + b) where a = b (assuming equal size) = 2n/2, 4n/4, 8n/8
    # O(n)
    sorted_list = []
    i = 0
    j = 0

    while (i < len(list1) and j < len(list2)):
        if (list1[i] <= list2[j]):
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j]) 
            j += 1 

    # O(arrLen)
    sorted_list.extend(list1[i:]) 
    sorted_list.extend(list2[j:])

    return sorted_list

def verify_sorted(list):
    # O(n)
    n = len(list)

    if n == 0 or n == 1: 
        return True 

    return list[0] <= list[1] and verify_sorted(list[1:])
 

if __name__ == "__main__": 
    arr = [38, 9, 29, 7, 2, 15, 28]
    # arr = [9,8,7,6,5,4,3,2,1]
    print(merge_sort(arr))
    print(verify_sorted(merge_sort(arr)))

           

