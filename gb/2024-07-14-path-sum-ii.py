def pathSum(self, root, targetSum):
    res = []

    def dfs(node, path, currSum):
        if not node:
            return
        if not node.left and not node.right:
            currSum += node.val
            path.append(node.val)
            if currSum == targetSum:
                res.append(path.copy())
            path.pop()
            return

        path.append(node.val)
        currSum += node.val

        dfs(node.left, path, currSum)
        dfs(node.right, path, currSum)
        path.pop()

    dfs(root, [], 0)
    return res
