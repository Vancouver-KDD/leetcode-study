class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // base case: 비어있거나 마지막 노드일 때
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        // 나머지 리스트를 역순으로 만들기
        ListNode* newHead = reverseList(head->next);

        // 현재 노드를 뒤로 연결
        head->next->next = head;
        head->next = nullptr;

        return newHead;
    }
};
