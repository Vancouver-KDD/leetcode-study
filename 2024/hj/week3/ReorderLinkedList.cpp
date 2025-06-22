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
    void reorderList(ListNode* head) {
        if (!head->next) return;

        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* prev = nullptr;
        ListNode* crnt = slow;
        while (cur) {
            ListNode* temp = crnt->next;
            crnt->next = prev;
            prev = crnt;
            crnt = temp;
        }

        ListNode* l1 = head;
        ListNode* l2 = prev;
        while (l2->next) {
            ListNode* n1 = l1->next;
            ListNode* n2 = l2->next;

            l1->next = l2;
            l1 = n1;

            l2->next = l1;
            l2 = n2;
        }
    }
};