function distanceK(root: TreeNode | null, target: TreeNode | null, k: number): number[] {
    if (!root || !target) return []

    const parentMap = new Map<TreeNode, TreeNode | null>()
    let queue: any[] = [root]
    while (queue.length > 0) {
        const node = queue.shift()!
        if (node.left) {
            parentMap.set(node.left, node)
            queue.push(node.left)
        }
        if (node.right) {
            parentMap.set(node.right, node)
            queue.push(node.right)
        }
    }

    queue = [[target, 0]]
    const visited = new Set<TreeNode>([target])
    const result: number[] = []
    while (queue.length > 0) {
        const [node, depth] = queue.shift()!
        if (depth === k) {
            result.push(node.val)
        } else {
            for (const neighbor of [node.left, node.right, parentMap.get(node)]) {
                if (neighbor && !visited.has(neighbor)) {
                    visited.add(neighbor)
                    queue.push([neighbor, depth + 1])
                }
            }
        }
    }

    return result
}
