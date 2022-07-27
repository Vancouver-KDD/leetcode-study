#include "common.h"


struct ListNode {
    int val;
    struct ListNode *next;
};


void reorderList(struct ListNode* head){
    int count = 0;
    struct ListNode* list = head;
    struct ListNode* dummy = malloc(sizeof(struct ListNode));

    while (list) {
        count++;
        list = list->next;
    }

    struct ListNode* arr[count];

    list = head;
    for (int i = 0; i < count; i++) {
        arr[i] = list;
        list = list->next;
    }
    if (count <= 2) return head;


    for (int i = 0; i < count / 2; i++) {
        dummy->next = arr[i];
        dummy->next->next = arr[count - i - 1];
        if (i != count / 2 - 1) dummy = dummy->next->next;
        else {
            if (count % 2 != 0) {
                dummy->next->next->next = arr[i + 1];
                dummy->next->next->next->next = NULL;
            } else {
                dummy->next->next->next = NULL;
            }
        }
    }

    return head;
}

