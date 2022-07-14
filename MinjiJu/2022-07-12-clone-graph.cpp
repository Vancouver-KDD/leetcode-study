/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    vector<Node*> v;
    
    Solution(){
        for(int i=0; i<=100; i++) v.push_back(nullptr);
    }
    
    Node* cloneGraph(Node* node) {

        if(!node) return nullptr;
        if(v[node->val]) return v[node->val];
        
        Node* root = new Node(node->val);
        v[node->val] = root;
        
        for(int i=0; i<node->neighbors.size(); i++){
            root->neighbors.push_back(cloneGraph(node->neighbors[i]));
        }
        return root;
    }
};