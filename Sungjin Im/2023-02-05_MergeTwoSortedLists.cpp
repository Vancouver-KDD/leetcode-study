// MergeTwoSortedLists.cpp : This file contains the 'main' function. Program execution begins and ends there.
// :author: SJ
// :date: Feb 05 2023
//
// You are given the heads of two sorted linked lists list1 and list2.
// Merge the two lists in a one sorted list.
// The list should be made by splicing together the nodes of the first two lists.
// Return the head of the merged linked list.
// 
// Example 1 :
// Input: list1 = [1,2,4], list2 = [1,3,4]
// Output: [1, 1, 2, 3, 4, 4]
// 
// Example 2 :
// Input : list1 = [], list2 = []
// Output : []
// 
// Example 3 :
// Input : list1 = [], list2 = [0]
// Output : [0]
//


#include <iostream>

using namespace std;

struct ListNode {
    int val = 0;
    ListNode* next = NULL;
};


ListNode* mergeTwoLists(ListNode* l1, ListNode* l2)
{
    if (l1 == NULL)
    {
        return l2;
    }

    if (l2 == NULL)
    {
        return l1;
    }

    if (l1->val >= l2->val)
    {
        l2->next = mergeTwoLists(l1, l2->next);
    }
    else
    {
        l1->next = mergeTwoLists(l1->next, l2);
        l2 = l1;
    }

    return l2;
}

int main()
{
    ListNode l1_1;
    l1_1.val = 1;

    ListNode l1_2;
    l1_2.val = 2;

    ListNode l1_3;
    l1_3.val = 4;


    ListNode l2_1;
    l2_1.val = 1;

    ListNode l2_2;
    l2_2.val = 3;

    ListNode l2_3;
    l2_3.val = 4;


    l1_1.next = &l1_2;
    l1_2.next = &l1_3;

    l2_1.next = &l2_2;
    l2_2.next = &l2_3;

    ListNode* l1 = &l1_1;
    ListNode* l2 = &l2_1;

    ListNode* l_ans = mergeTwoLists(l1, l2);

    while (l_ans != NULL)
    {
        cout << l_ans->val << ' ';
        l_ans = l_ans->next;
    }

}
