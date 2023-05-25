from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.is_match(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_match(self, root_part, root_sub):
        if root_part and root_sub:
            return root_part.val == root_sub.val and self.is_match(root_part.left, root_sub.left) and self.is_match(root_part.right, root_sub.right)
        return root_part is root_sub

    #     TRY_3
    #     Failure: NoneType
    #     if not root:
    #         return False
    #     if self.is_match(root, subRoot):
    #         return True
    #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    #
    # def is_match(self, root_part, root_sub):
    #     return root_part.val == root_sub.val and \
    #         self.is_match(root_part.left, root_sub.left) and \
    #         self.is_match(root_part.right, root_sub.right)

    #     TRY_2
    #     1. iterate root
    #     2. if both head of root and subRoot match, iterate a helper function (is_match)
    #     3. iterate is_match function until the end
    #     4. check if the subtree is the right fit part to root
    #     4.1. in case of
    #       Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    #       Output: false
    #       subRoot is a part of the root, but should match until the end
    #     if not root:
    #         return False
    #     if root and not subRoot:
    #         return True
    #     if root.val == subRoot.val:
    #         # print('r', root, 's', subRoot)
    #         return self.is_match(root.left, subRoot.left) and self.is_match(root.right, subRoot.right)
    #     return (self.isSubtree(root.left, subRoot) and self.isSubtree(root.right, subRoot))
    #
    # def is_match(self, root_part, root_sub) -> bool:
    #     print('r:', root_part, 's:', root_sub)
    #     if not root_part and not root_sub:
    #         return True
    #     else:
    #         return False
    #     if root_part.val == root_sub.val:
    #         return self.is_match(root_part.left, root_sub.left) and self.is_match(root_part.right, root_sub.right)

        # TRY_1
        # if not root or not subRoot:
        #     return False
        #
        # def is_match(root_part, root_sub):
        #     # iterate if both heads of root and subRoot match
        #     if root_part.val == root_sub.val:
        #         return is_match(root_part.left, root_sub.left) and is_match(root_part.right, root_sub.right)
        #     else:
        #         return False
        #
        # while subRoot:
        #     if root.val == subRoot.val:
        #         return is_match(root, subRoot)
        #     else:
        #         return self.isSubtree(root.left, subRoot) and self.isSubtree(root.right, subRoot)
        # return True
