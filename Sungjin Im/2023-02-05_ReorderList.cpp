// ReorderList.cpp : This file contains the 'main' function. Program execution begins and ends there.
// :author: SJ
// :date: Feb 05 2023
//
// You are given the head of a singly linked-list.
// The list can be represented as:
// L0 ¡æ L1 ¡æ ¡¦ ¡æ Ln - 1 ¡æ Ln
//
// Reorder the list to be on the following form :
// L0 ¡æ Ln ¡æ L1 ¡æ Ln - 1 ¡æ L2 ¡æ Ln - 2 ¡æ ¡¦
// 
// You may not modify the values in the list's nodes. Only nodes themselves may be changed.
//
// Example 1 :
// Input : head = [1, 2, 3, 4]
// Output : [1, 4, 2, 3]
// 
// Example 2 :
// Input : head = [1, 2, 3, 4, 5]
// Output : [1, 5, 2, 4, 3]
//



#include <iostream>

using namespace std;

struct ListNode {
    int val = 0;
    ListNode* next = NULL;
};

void reorderList(ListNode* head) {
    if (!head || !head->next || !head->next->next)
    {
        return;
    }

    ListNode* penultimate = head;
    while (penultimate->next->next)
    {
        penultimate = penultimate->next;
    }

    penultimate->next->next = head->next;
    head->next = penultimate->next;

    penultimate->next = NULL;

    reorderList(head->next->next);
}


int main()
{
// Output : [1, 4, 2, 3]

    ListNode l1;
    l1.val = 1;
    
    ListNode l2;
    l2.val = 2;
    
    ListNode l3;
    l3.val = 3;
    
    ListNode l4;
    l4.val = 4;

    l1.next = &l2;
    l2.next = &l3;
    l3.next = &l4;

    ListNode* ans = &l1;
    reorderList(ans);

    while (ans != NULL)
    {
        cout << ans->val << ' ';
        ans = ans->next;
    }
}
