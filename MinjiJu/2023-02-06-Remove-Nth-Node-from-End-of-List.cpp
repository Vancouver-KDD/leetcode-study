// Stack
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int &n) {
        
        stack<ListNode*> s;
        int length = 0;
        
        ListNode *node = head;
        
        // push all nodes into stack
        // count length of list
        while(node){
            s.push(node);
            node = node->next;
            length++;
        }
        
        // first node needs to be removed
        if(length==n) return head->next;
        
        // (n-1)th node from the end
        while(n--) s.pop();
        node = s.top();
        
        // remove the node
        node->next = node->next->next;
        
        return head;
    }
};