def binaryTreePaths(self, root):
    res = []

    def dfs(node, path):
        if not node:
            return
        if not node.left and not node.right:
            path.append(node.val)
            res.append(path.copy())
            path.pop()
            return

        path.append(node.val)
        dfs(node.left, path)
        dfs(node.right, path)
        path.pop()

    dfs(root, [])
    return res
