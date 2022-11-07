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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        if (head->next == NULL) {
            head = NULL;
            return head;
        }
        
        int length = 1;
        ListNode* p = head;
        
        while (p->next != NULL) {
            p = p->next;
            length++;
        }
        
        p = head;
        ListNode* prev = NULL;
        
        int index = 0;
        while (index < length - n) {
            prev = p;
            p = p->next;
            index++;
        }
        
        if (prev != NULL) {
            prev->next = p->next;
        } else {
            head = p->next;
        }
        delete p;
        
        return head;
    }
};