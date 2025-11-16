def binarySearch(arr, item):
    i , j = 0, len(a) - 1
    m = None
    while i <= j:
        m = int((i+j)/2)
        print(i, m, j)

        if item == arr[m]:
            return True
        elif item < arr[m]:
            j = m - 1
        else:
            i = m + 1

    return m



a = [1, 3, 5, 7, 10, 11, 15, 18, 21, 25, 28, 31, 33 ]
#a= [0, 1, 2, 3,  4,  5,  6,  7,  8,  9, 10, 11, 12 ]
"""
assert binarySearch(a, 32) == False
assert binarySearch(a, 33) == True
assert binarySearch(a, 5) == True
assert binarySearch(a, 4) == False
assert binarySearch(a, 14) == False
assert binarySearch(a, 18) == True
"""

print(binarySearch(a, 4))
