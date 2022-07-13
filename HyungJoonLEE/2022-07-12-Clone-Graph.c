#include "common.h"



struct Node{
    int val;
    int numNeighbors;
    struct Node** neighbors;
};


void dfs(struct Node* head, struct Node *s, struct Node** visit) {
    head->val = s->val;
    head->numNeighbors = s->numNeighbors;
    visit[s->val] = head;

    if (s->numNeighbors == 0) return;
    head->neighbors = (struct Node**) malloc(sizeof(struct Node*) * (s->numNeighbors));
    for (int i = 0; i < (s->numNeighbors); i++)
        if (visit[s->neighbors[i]->val] == NULL){
            head->neighbors[i] = (struct Node*) malloc(sizeof(struct Node));
            dfs(head->neighbors[i], s->neighbors[i], visit);
        }
        else head->neighbors[i] = visit[s->neighbors[i]->val];
    return;
}


struct Node *cloneGraph(struct Node *s) {

    if (!s) return NULL;

    struct Node* visit[101] = {NULL};
    struct Node* head = (struct Node*)malloc(sizeof(struct Node));

    if (!head) printf("cloneGraph memory allocation error\n");
    else dfs(head, s, visit);

    return head;
}