arr = [45, 54, 56, 78, 85, 95, 355, 4555, 8000, 35545454]


# assuming the array is sorted
def BS(low, high, searchitem):
    # find the midppoint of the array
    mid = (low + high) // 2
    
    # base case
    if arr[mid] == searchitem:
        return mid
    
    # general case
    if searchitem > arr[mid]:
        return BS(mid, high, searchitem)
    elif searchitem < arr[mid]:
        return BS(low, mid, searchitem)
    else:
        # special case (value not found)
        return -1

if __name__ == '__main__':
    print(arr)
    print(f'index of item in array(56): {BS(0, len(arr), 56)}')
    print(f'index of item in array(78): {BS(0, len(arr), 78)}')
    #  print(f'index of item in array(108): {BS(0, len(arr), 108)}')
    print(f'index of item in array(8000): {BS(0, len(arr), 8000)}')
