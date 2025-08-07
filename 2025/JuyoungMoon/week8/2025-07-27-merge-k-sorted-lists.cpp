// Author: Juyoung Moon

// KDD LeetCode Study Week 8: Heap / Priority Queue
// https://github.com/juyomo/leetcode-study

// LeetCode #23.
// https://leetcode.com/problems/merge-k-sorted-lists/

class Solution {
public:
    ListNode* mergeTwo(ListNode* l1, ListNode* l2) {
        if (l1 == nullptr) {
            return l2;
        } else if (l2 == nullptr) {
            return l1;
        }

        if (l1->val < l2->val) {
            l1->next = mergeTwo(l1->next, l2);
            return l1;
        } else {
            l2->next = mergeTwo(l1, l2->next);
            return l2;
        }
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0) {
            return nullptr;
        }
        
        ListNode* res = lists[0];
        
        for (int i = 1; i < lists.size(); i++) {
            res = mergeTwo(res, lists[i]);
        }

        return res;
    }
};
