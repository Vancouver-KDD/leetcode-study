class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        res = []
        while queue:
            subArray = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    subArray.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if subArray:
                res.append(subArray)

        return res
