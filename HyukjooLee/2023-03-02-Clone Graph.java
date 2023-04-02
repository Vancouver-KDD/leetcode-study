// Given a reference of a node in a connected undirected graph.

// Return a deep copy (clone) of the graph.

// Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

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
// 간단하게 그래프가 주어지고, 그래프를 순회하면서 카피본을 만드는 문제
// 
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

// 2. recursion
// The time complexity of the cloneGraph function is O(N+E), 
// where N is the number of nodes in the graph and E is the number of edges.
// This is because we visit each node and each edge exactly once
// while performing the cloning operation.

// The space complexity of the cloneGraph function is also O(N+E), 
// because we create a new node and add it to the map for each node in the graph,
// and we create a new edge for each edge in the graph.
// This means that the space used by the map, the cloned nodes,
// and the cloned edges all scale linearly with the size of the graph.

public Node cloneGraph(Node node) {
    // Create a new HashMap to keep track of which nodes have already been cloned
    Map<Integer, Node> map = new HashMap<>();
    // Call the private helper method cloneGraph to recursively clone the graph
    return cloneGraph(node, map);
}

private Node cloneGraph(Node node, Map<Integer, Node> map) {
    // If the current node has already been cloned, return a reference to the cloned node
    if(map.containsKey(node.val)) return map.get(node.val);
    // Otherwise, create a new Node object with the same value as the original node
    Node copy = new Node(node.val);
    // Add the new node to the map, with the original node's value as the key and the new node as the value
    map.put(node.val, copy);
    // Loop through each of the original node's neighbors
    for(Node neighbor : node.neighbors) {
        // Recursively call the cloneGraph method on each neighbor to create a clone of that neighbor
        Node clonedNeighbor = cloneGraph(neighbor, map);
        // Add the resulting cloned neighbor node to the "copy" node's list of neighbors
        copy.neighbors.add(clonedNeighbor);
    }
    // Return the "copy" node, which now represents a clone of the original node and all of its neighbors
    return copy;
}
