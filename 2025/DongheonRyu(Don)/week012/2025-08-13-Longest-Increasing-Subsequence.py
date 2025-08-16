import bisect

def length_of_LIS(nums: list[int]) -> int:
    sub = []
    for x in nums:
        idx = bisect.bisect_left(sub, x)
        if idx == len(sub):
            sub.append(x)
        else:
            sub[idx] = x
    return len(sub)

print(length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]))
