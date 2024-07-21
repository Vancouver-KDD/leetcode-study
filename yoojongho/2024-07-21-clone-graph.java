/**
 * Leetcode
 * problem: 133
 * link: https://leetcode.com/problems/clone-graph/description/
 * tag: Hash Table, Depth-First Search, Breadth-First Search, Graph
 * ---
 * Definition for a Node.
 * class Node {
 *     public int val;
 *     public List<Node> neighbors;
 *     public Node() {
 *         val = 0;
 *         neighbors = new ArrayList<Node>();
 *     }
 *     public Node(int _val) {
 *         val = _val;
 *         neighbors = new ArrayList<Node>();
 *     }
 *     public Node(int _val, ArrayList<Node> _neighbors) {
 *         val = _val;
 *         neighbors = _neighbors;
 *     }
 * }
 * ---
 * goal: Make a deep copy function for Node
 */
class Solution {
    Map<Integer, Node> store = new HashMap<>();
    public Node cloneGraph(Node node) {
        if(node == null) return null;
        Node clone = new Node(node.val);
        store.put(node.val, clone);

        for(Node neighbor: node.neighbors) {
            if(!store.containsKey(neighbor.val)){
                cloneGraph(neighbor);
            }
            clone.neighbors.add(store.get(neighbor.val));
        }

        return clone;
    }
}