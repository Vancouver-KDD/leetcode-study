const dfs = (root: TreeNode | null, targetSum: number, temp: number[], result: number[][]) => {
    if (!root) return
    temp.push(root.val)
    const val = targetSum - root.val
    if (!root.left && !root.right) {
        if (val === 0) {
            result.push(temp)
        }
        return
    }
    dfs(root.left, val, [...temp], result)
    dfs(root.right, val, [...temp], result)
}

function pathSum(root: TreeNode | null, targetSum: number): number[][] {
    const result: number[][] = []

    dfs(root, targetSum, [], result)
    return result
}
