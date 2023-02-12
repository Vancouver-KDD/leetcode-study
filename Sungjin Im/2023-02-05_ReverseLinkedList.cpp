// ReverseLinkedList.cpp : This file contains the 'main' function. Program execution begins and ends there.
// :author: SJ
// :date: Feb 05 2023
//
// Given the head of a singly linked list,
// reverse the list,
// and return the reversed list.
// 
// Example 1 :
// Input: head = [1, 2, 3, 4, 5]
// Output : [5, 4, 3, 2, 1]
// 
// Example 2 :
// Input : head = [1, 2]
// Output : [2, 1]
// 
// Example 3 :
// Input : head = []
// Output : []
//

#include <iostream>
#include <list>

using namespace std;

//ListNode* reverse_list(ListNode* head)
//{
//    reverseList() {
//        ListNode* nextNode, * prevNode = NULL;
//        while (head) {
//            nextNode = head->next;
//            head->next = prevNode;
//            prevNode = head;
//            head = nextNode;
//        }
//        return prevNode;
//    }
//
//}

int main()
{
    list<int> mylist;

    for (int i = 1; i < 16; i++)
    {
        mylist.push_back(i);
    }

    mylist.reverse();
    for (list<int>::iterator it = mylist.begin(); it != mylist.end(); ++it)
        cout << ' ' << *it;

    cout << '\n\n';

    return 0;
}
