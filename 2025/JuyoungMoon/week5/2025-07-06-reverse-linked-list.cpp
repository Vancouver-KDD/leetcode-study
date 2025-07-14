// Author: Juyoung Moon

// KDD LeetCode Study Week 5: Linked List
// https://github.com/juyomo/leetcode-study

// LeetCode #206.
// https://leetcode.com/problems/reverse-linked-list/

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
        if (head == nullptr) {
            return head;
        }

        ListNode* curr = head;
        ListNode* prev = nullptr;
        ListNode* next = head->next;

        while (curr != nullptr) {
            curr->next = prev;
            
            prev = curr;
            curr = next;
            if (curr != nullptr) {
                next = curr->next;
            }
        }
        
        return prev;
    }
};
