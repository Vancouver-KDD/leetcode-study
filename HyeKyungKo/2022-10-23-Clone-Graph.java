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

//2022.10.21
//Limitations: if node is null, return null
//Time Complexity : O(N + M) <-- 이게 왜 N + M 인지 모르겠따. 
class Solution {
    
    private HashMap<Node, Node> visited = new HashMap<Node, Node>();
    
    public Node cloneGraph(Node node) {
        if(node == null){
            return null;
        }
        
        Node cloneNode = new Node(node.val, new ArrayList<Node>());
        visited.put(node, cloneNode);

        for(Node neighbor : node.neighbors){
            Node nbNode = cloneNeighbor(neighbor);
            cloneNode.neighbors.add(nbNode);
        }
        
        return cloneNode;
    }
    
    private Node cloneNeighbor(Node node){
        
        if(visited.containsKey(node)){
            return visited.get(node); //return cloneNode;    
        }
        
        Node cloneNode = new Node(node.val, new ArrayList<Node>());
        visited.put(node, cloneNode);  
        
        for(Node neighbor : node.neighbors){
            Node nbNode = cloneNeighbor(neighbor);
            cloneNode.neighbors.add(nbNode);
        }
        
        return cloneNode;
    }
    
}