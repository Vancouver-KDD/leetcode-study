def sumNumbers(root):
    def dfs(node, current_sum):
        if not node:
            return 0

        current_sum = current_sum * 10 + node.val

        if not node.left and not node.right:
            return current_sum

        left_sum = dfs(node.left, current_sum)
        right_sum = dfs(node.right, current_sum)

        return left_sum + right_sum

    return dfs(root, 0)