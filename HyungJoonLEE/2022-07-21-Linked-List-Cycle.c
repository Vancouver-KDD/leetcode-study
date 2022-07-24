#include "common.h"

struct ListNode {
    int val;
    struct ListNode *next;
};

bool hasCycle(struct ListNode *head) {
    struct ListNode *chaser = head, *pioneer = NULL;

    if(!head || !(head->next)) return false;

    pioneer = head->next;

    while(chaser != pioneer) {
        if (pioneer == NULL) return false;

        chaser = chaser->next;
        if(pioneer->next && pioneer->next->next)
            pioneer = pioneer->next->next;
        else
            pioneer = pioneer->next;
    }
    return true;
}
