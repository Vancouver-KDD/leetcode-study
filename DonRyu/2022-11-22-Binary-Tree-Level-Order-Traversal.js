function levelOrder(root) {
    if (!root) return []
    let result = []
    let queue = [root]
    while (queue.length != 0) {
        let subarr = []
        const n = queue.length
        for (let i = 0; i < n; i++) {
            let node = queue.pop()
            subarr.push(node.val)
            if (node.left) queue.unshift(node.left)
            if (node.right) queue.unshift(node.right)
        }
        result.push(subarr)
    }
    return result
}
