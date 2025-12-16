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

class Solution {

    /*
        let N = total num of nodes in graph
        let E = total num of edges in graph
        Time Compleity:
            O(N + E)

        Space Complexity: O(N)
     */
    public Node cloneGraph(Node node) {
        if (node == null) return null;

        // Map to store already cloned nodes
        Map<Node, Node> visited = new HashMap<>();

        // Queue to store neibors
        Queue<Node> queue = new LinkedList<>();

        // Start with the given node
        queue.offer(node);
        visited.put(node, new Node(node.val));

        while (!queue.isEmpty()) {
            Node original = queue.poll();
            Node clone = visited.get(original);

            for (Node neighbor : original.neighbors) {
                // Visit neighbor is has not visited yet and add to queue for bfs
                if (!visited.containsKey(neighbor)) {
                    visited.put(neighbor, new Node(neighbor.val));
                    queue.offer(neighbor);
                }

                clone.neighbors.add(visited.get(neighbor));
            }
        }
    return visited.get(node);
    }
}