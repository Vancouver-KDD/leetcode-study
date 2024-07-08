function rightSideView(root: TreeNode | null): number[] {
    const res: number[] = []
    if (!root) {
        return res
    }
    const queue = [root]
    let node
    while (queue.length) {
        const { length } = queue
        for (let i = 0; i < length; i++) {
            node = queue.shift()
            if (node?.left) queue.push(node.left)
            if (node?.right) queue.push(node.right)
        }
        res.push(node.val)
    }
    return res
}
