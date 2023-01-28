# Sungjin Im

# 217. Contains Duplicate
# Given an integer array nums,
# return true if any value appears at least twice in the array,
# and return false if every element is distinct.

def has_duplicates(arr):
    return len(arr) != len(set(arr))

nums = [1,2,3,1]
print(has_duplicates(nums))
# True

nums = [1,2,3,4]
print(has_duplicates(nums))
# False

nums = [1,1,1,3,3,4,3,2,4,2]
print(has_duplicates(nums))
# True
