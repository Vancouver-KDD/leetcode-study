# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Recursion -> pass parameter: root node, list contaiting their ancester
        # if node is not None -> add the node's value and do left/right sub-tree
        # if node is None -> compare sum of list to targetSum
        # if it is True: return list, otherwise return empty list

        if not root:
            return []

        res = []

        def checkSum(node, ancesters, sum_ancesters: int):
            nonlocal res

            ancesters.append(node.val)
            sum_ancesters += node.val
            if not node.left and not node.right:
                # when this node is leaf
                if ancesters and sum_ancesters == targetSum:
                    res.append(ancesters[:])

            if node.left:
                checkSum(node.left, ancesters, sum_ancesters)
            if node.right:
                checkSum(node.right, ancesters, sum_ancesters)

            ancesters.pop()

        checkSum(root, [], 0)

        return res
