class _Node {
    val: number
    left: _Node | null
    right: _Node | null
    next: _Node | null
    constructor(val?: number, left?: _Node, right?: _Node, next?: _Node) {
        this.val = val === undefined ? 0 : val
        this.left = left === undefined ? null : left
        this.right = right === undefined ? null : right
        this.next = next === undefined ? null : next
    }
}

function connect(root: _Node | null): _Node | null {
    if (!root) {
        return root
    }
    const queue = [root]
    let prev
    while (queue.length) {
        const { length } = queue
        for (let i = 0; i < length; i++) {
            const node = queue.shift()
            if (node && prev) {
                prev.next = node
            }
            prev = node
            if (node?.left) {
                queue.push(node.left)
            }
            if (node?.right) {
                queue.push(node.right)
            }
        }
        prev = null
    }
    return root
}
