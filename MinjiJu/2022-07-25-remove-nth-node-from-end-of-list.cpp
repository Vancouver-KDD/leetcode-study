// Using recursion
// Backtracking and rebuilding list
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
        if(!head) return head;
        ListNode *node = removeNthFromEnd(head->next, n);
        if((--n)==0) return node;
        head->next = node;
        return head;
    }
};

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
        
        // if end of list
        if(head == NULL) return NULL;
        
        // set to next node
        head->next = removeNthFromEnd(head->next, n);
        
        // check if node needs to be removed
        if((--n) == 0) return head->next;
        
        // return head
        return head;
    }
};

// two pointers method
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
        
        ListNode *t1 = head;
        ListNode *t2 = head;
        
        while(t1 && n--) t1 = t1->next; // t1 at (n+1)th node
                                        // (t2 - t1 = n)
        
        if(!t1) return head->next;      // first node needs to be removed
        
        // find node before n-th node from the end
        while(t1->next){
            t1 = t1->next;
            t2 = t2->next;
        }
        t2->next = t2->next->next;
        return head;
    }
};

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

// find length
// find node before n-th from the end
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
        int length = 0;
        ListNode *node = head;
        
        // get length of list
        while(node){
            length++;
            node = node->next;
        }
        
        // first node needs to be removed
        if(n==length) return head->next;
        
        length-=n;
        length--;
        
        node = head;
        
        // node before n-th from the end
        while(length--){
            node = node->next;
        }
        // move the node
        node->next = node->next->next;
        
        // return head
        return head;
    }
};