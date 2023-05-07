# 1. Comparing sizes after adding to the set, which is a data structure that removes duplicates

def contains_duplicate(nums: List[int]) -> bool:
    nums_to_set = set(nums)
    # nums:[1,2,3,1]
    # nums_to_set:set([1, 2, 3])
    return True if len(nums_to_set) != len(nums) else False

# 2. Using hashmap to compare duplicates