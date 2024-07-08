function zigzagLevelOrder(root: TreeNode | null): number[][] {
    const res: number[][] = []
    if (!root) {
        return res
    }
    const queue = [root]
    let flip = false
    while (queue.length) {
        const temp: number[] = []
        const { length } = queue
        for (let i = 0; i < length; i++) {
            const node = queue.shift()
            temp.push(node?.val as number)
            if (node?.left) {
                queue.push(node.left)
            }
            if (node?.right) {
                queue.push(node.right)
            }
        }
        if (flip) temp.reverse()
        res.push(temp)
        flip = !flip
    }
    return res
}
