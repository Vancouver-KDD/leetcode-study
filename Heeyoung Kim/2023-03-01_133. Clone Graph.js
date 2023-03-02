let cloneGraph = (graph) => {
    let map = {};
    return traverse(graph);

    let traverse = (node) => {
        if(!node) return node;
        if(!map[node.label]) {
            map[node.label] = new UndirectedGraphNode(node.label);
            map[node.label].neighbors = node.neighbors.map(traverse);
        }

        return map[node.label];

    }
}