/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;

        unordered_map<Node*, Node*> um;

        Node* crnt = head;
        while (crnt) {
            Node* node = new Node(crnt->val);
            um[crnt] = node;
            crnt = crnt->next;
        }

        crnt = head;
        while (crnt) {
            um[crnt]->next = um[crnt->next];
            um[crnt]->random = um[crnt->random];
            crnt = crnt->next;
        }

        return um[head];
    }
};
