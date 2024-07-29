const clone = new Map();
var cloneGraph = function(node) {
    if (!node) return null;
    if (clone.has(node)) return clone.get(node);

    const newNode = new Node(node.val);
    clone.set(node, newNode);
    newNode.neighbors = node.neighbors.map(x => cloneGraph(x));

    return newNode;
};
