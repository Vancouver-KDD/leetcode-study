/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        
        if(head==NULL || head->next==NULL) return false;
        
        while(head->next!=NULL || head->val!=INT_MIN){
            if(head->val==INT_MIN) return true;
            if(head->next==NULL) return false;
            head->val = INT_MIN;
            head = head->next;
        }
        return false;
    }
};

// (lol)
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    const int MAX_VAL = 10000;
    
    bool hasCycle(ListNode *head) {
        if(head==NULL) return false;
        int count = 0;
        while(head){
            count++;
            if(count>MAX_VAL) break;
            head = head->next;
        }
        return count>MAX_VAL ? true : false;
    }
};