"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
 of all the values of the nodes in the tree.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def combinationSum(self, candidates, target: int):
        def backtrack(start, target, combination):
            if target == 0:
                results.append(combination)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if target - candidates[i] < 0:
                    break
                backtrack(i, target - candidates[i], combination + [candidates[i]])

        candidates.sort()
        results = []
        backtrack(0, target, [])
        return results


def main():
    s = Solution()


if __name__ == "__main__":
    main()
