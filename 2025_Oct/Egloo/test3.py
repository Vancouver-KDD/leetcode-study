from bisect import bisect_left, bisect_right, insort_right

a = [1, 2, 4, 6, 10]
#   [0, 1, 2, 3, 4 ]
r1 = bisect_left(a, 4)
print(r1)


r3 = bisect_left(a, 3)
print(r3)

"""
def getFloor(a, val):
    i = bisect_left(a, val)
    if a[i] == val:

"""

