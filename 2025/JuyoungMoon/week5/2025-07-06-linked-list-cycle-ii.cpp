// Author: Juyoung Moon

// KDD LeetCode Study Week 5: Linked List
// https://github.com/juyomo/leetcode-study

// LeetCode #142.
// https://leetcode.com/problems/linked-list-cycle-ii/

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
    ListNode *detectCycle(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return nullptr;
        }
        
        unordered_set<ListNode*> seen;
        
        ListNode* curr = head;
        while (curr != nullptr) {
            if (seen.find(curr) != seen.end()) {
                return curr;
            }
            seen.insert(curr);
            curr = curr->next;
        }
        return nullptr;
    }
};
