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
    ListNode* reverseList(ListNode* head) {
        
        if (head == NULL || head->next == NULL) {
            return head;
        }
        
        ListNode* p = head;
        ListNode* prev = NULL;
        
        while (p != NULL) {
            if (head->next != NULL) {
                head = head->next;
            }
            ListNode* temp = p;
            p = p->next;
            temp->next = prev;
            prev = temp;
        }
        
        return head;
    }
};