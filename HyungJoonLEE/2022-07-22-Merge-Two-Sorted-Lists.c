#include "common.h"

struct ListNode {
    int val;
    struct ListNode *next;
};


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode head;
    struct ListNode *temp=&head;
    if(!list1 && !list2) return NULL;

    while(list1 && list2){
        if(list1->val < list2->val) {
            temp->next = list1;
            list1 = list1->next;
            temp = temp->next;
        }
        else {
            temp->next=list2;
            list2 = list2->next;
            temp = temp->next;
        }
    }
    if(list1) temp->next = list1;
    if(list2) temp->next = list2;

    return head.next;
}