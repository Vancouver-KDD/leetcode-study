
/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new List<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new List<Node>();
    }

    public Node(int _val, List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

public class Solution {
    public Node CloneGraph(Node node) {
        Dictionary<Node, Node> d = new Dictionary<Node, Node>();
        return Clone(node);

        Node Clone(Node n) {
            if (n == null)
                return null;
            
            if (d.ContainsKey(n))
                return d[n];

            d[n] = new Node(n.val);

            foreach(var v in n.neighbors) {
                d[n].neighbors.Add(Clone(v));
            }

            return d[n];
        }

    }
}
