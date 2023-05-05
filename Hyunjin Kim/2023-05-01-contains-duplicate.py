class Solution(object):
    def containsDuplicate(self, nums):
        # create set instead of list. list stores unnecessary indices.
        storage = set()

        for n in nums:
            if n in storage:
                return True
            else:
                storage.add(n)
        return False

