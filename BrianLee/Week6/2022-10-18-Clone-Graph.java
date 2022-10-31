class Solution {
    public Node cloneGraph(Node node) {
        if(node == null) return null;
        Map<Integer,Node> nodes = new HashMap<>();
        return dfs(node, nodes);
    }

    private Node dfs(Node node, Map<Integer,Node> nodes) {
        if(nodes.containsKey(node.val)) return nodes.get(node.val);

        Node copy = new Node(node.val);
        nodes.put(node.val, copy);

        for(Node child : node.neighbors) {
            copy.neighbors.add(dfs(child, nodes));
        }

        return copy;
    }
}