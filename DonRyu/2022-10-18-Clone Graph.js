var cloneGraph = function(node) {
    // Nodes we have already copied
    const visited = {};

    // DFS function to copy graph
    const dfs = (node) => {
        if (!node) return node;
        // If we have seen this node before, return it
        if (visited[node.val]!=null) return visited[node.val];

        // Create base for copied node
        const root = new Node(node.val);
        // Add this copied node to group of nodes we hav copied
        visited[node.val] = root;

        // Add copied neighbors to the current copied node
        node.neighbors.forEach(n => root.neighbors.push(dfs(n)))
        return root;
    }

    // Return new copied graph
    return dfs(node);
};
