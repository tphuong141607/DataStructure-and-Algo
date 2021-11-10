# Input = array 
# Time complexity = O(n)
# Space complexity = O(1)

def find_n (list, target):
    """ 
    Returns the index position of the target if found, else returns None 
    """

    if len(list) == 0: return None
    for index, n in enumerate(list): 
        if n == target: 
            return index
    return None

if __name__ == '__main__':
    arr = [1, 3, 4, 5, 10, 3, 99] 
    print(find_n(arr, 999))