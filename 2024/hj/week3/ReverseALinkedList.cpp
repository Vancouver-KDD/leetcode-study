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
        if (!head) return nullptr;

        ListNode* prev = nullptr;
        ListNode* crnt = head;

        while (crnt) {
            ListNode* temp = crnt->next;
            crnt->next = prev;
            prev = crnt;
            crnt = temp;
        }

        return prev;
    }
};
