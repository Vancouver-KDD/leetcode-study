#include "common.h"

struct ListNode {
    int val;
    struct ListNode *next;
};


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode* list = head;
    int count = 0, chaser = 0;

    while(list) {
        count++;
        list = list->next;
    }

    if (count == 1 && n == 1) return NULL;

    count = count - n;
    list = head;
    if (chaser == count) return head = list->next;

    while(chaser != count) {
        chaser++;
        if (chaser == count) list->next = list->next->next;
        list = list->next;
    }
    return head;
}