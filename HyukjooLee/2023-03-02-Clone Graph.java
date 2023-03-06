// Given an m x n grid of characters board and a string word, return true if word exists in the grid.

// The word can be constructed from letters of sequentially adjacent cells,
// where adjacent cells are horizontally or vertically neighboring.
// The same letter cell may not be used more than once.

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

// creating a deep copy of the input graph by traversing the graph and creating a new one 
// to avoid duplicate nodes, we use a visited map to keep track of the original nodes and their corresponding clone nodes
// and adds them to the clone node's neighbor list
// time complexituy is O(N): N is the number of nodes in the input graph.
// space complexity is O(N), where N is the number of nodes in the input graph
class Solution {
    private Map<Node, Node> visited;

    public Solution() {
        visited = new HashMap<Node, Node>();
    }

    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }

        if (visited.containsKey(node)) {
            return visited.get(node);
        }

        Node cloneNode = new Node(node.val);
        visited.put(node, cloneNode);

        for (Node neighbor : node.neighbors) {
            cloneNode.neighbors.add(cloneGraph(neighbor));
        }

        return cloneNode;
    }
}