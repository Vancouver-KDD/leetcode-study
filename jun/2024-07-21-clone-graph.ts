function cloneGraph(node: _Node | null): _Node | null {
    if (!node) return null
    const map = new Map()

    function dfs(_node: _Node | null) {
        if (!_node) return
        const output = map.get(_node.val)
        if (output) return output
        const { val, neighbors } = _node
        const newNode = new _Node(val)
        map.set(val, newNode)
        neighbors.forEach((neighbor) => {
            newNode.neighbors.push(dfs(neighbor))
        })
        return newNode
    }
    return dfs(node)
}
