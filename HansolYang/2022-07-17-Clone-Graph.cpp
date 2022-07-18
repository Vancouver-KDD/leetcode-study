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
    Node* cloneGraph(Node* node) {
        
        if (node == NULL) {
            return NULL;
        }
        
        Node* head = new Node();
        head->val = node->val;
        
        vector<Node*> visited;
        vector<vector<Node*>> togo;
        
        for (Node* i : node->neighbors) {
            vector<Node*> each = {head, i};
            togo.push_back(each);
        }
        
        visited.push_back(head);
        
        while (!togo.empty()) {
            vector<Node*> curr = togo[0];
            Node* prev = curr[0];
            Node* toCopy = curr[1];
            togo.erase(togo.begin());
            
            int idx = -1;
            for (int i = 0; i < visited.size(); i++) {
                if (visited[i]->val == toCopy->val) {
                    idx = i;
                    break;
                }
            }
            
            if (idx != -1) {
                Node* temp = visited[idx];
                prev->neighbors.push_back(temp);
            } else {
                Node* temp = new Node();
                temp->val = toCopy->val;
                
                for (Node* i : toCopy->neighbors) {
                    vector<Node*> each = {temp, i};
                    togo.push_back(each);
                }
                
                visited.push_back(temp);
                prev->neighbors.push_back(temp);
            }
        }
        
        return head;
    }
};