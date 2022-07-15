#include "common.h"


struct Node
{
    int data;
    struct Node* link;
};


struct stack {
    struct Node *top;
    int size;
};


// Utility function to add an element
// data in the stack insert at the beginning
void push(struct stack *st, int data)
{

    // Create new node temp and allocate memory
    struct Node* temp;
    temp = (struct Node *)malloc(sizeof(struct Node));

    // Check if stack (heap) is full.
    // Then inserting an element would
    // lead to stack overflow
    if (!temp)
    {
        printf("Heap Overflow \n");
        exit(1);
    }

    // Initialize data into temp data field
    temp->data = data;

    // Put top pointer reference into temp link
    temp->link = st->top;

    // Make temp as top of Stack
    st->top = temp;
    st->size++;
}

// Utility function to check if
// the stack is empty or not
int isEmpty(struct stack *st)
{
    return st->top == NULL;
}

// Utility function to return top element in a stack
int peek(struct stack *st)
{

    // Check for empty stack
    if (!isEmpty(st))
        return st->top->data;
    else
        exit(1);
}

// Utility function to pop top
// element from the stack
int pop(struct stack *st)
{
    struct Node* temp;
    int val = -1;

    // Check for stack underflow
    if (st->top == NULL)
    {
        printf("Stack Underflow \n");
        exit(1);
    }
    else
    {

        // Top assign into temp
        temp = st->top;

        val = temp->data;
        // Assign second node to top
        st->top = st->top->link;

        // Destroy connection between
        // first and second
        temp->link = NULL;

        // Release memory of top node
        free(temp);
    }
    return val;
}

bool canFinish(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize) {

    int **adjlist = (int **) malloc(numCourses * sizeof(int *));
    int i = 0, j = 0;

    int v = 0;

    int curcourseid;
    int ccount = 0;
    int indegree[numCourses];
    struct stack st;


    for (i = 0; i < numCourses; i++) {
        adjlist[i] = NULL;
        indegree[i] = 0;
    }


    for (curcourseid = 0; curcourseid < prerequisitesSize; curcourseid++) {
        int *coursepair = prerequisites[curcourseid];


        if (!adjlist[coursepair[1]]) {
            adjlist[coursepair[1]] = (int *) malloc(30 * sizeof(int));
            for (i = 0; i < 30; i++)
                adjlist[coursepair[1]][i] = -1;
        }
        i = 0;
        while (adjlist[coursepair[1]][i] != -1)
            i++;
        adjlist[coursepair[1]][i] = coursepair[0];
        indegree[coursepair[0]]++;
    }

    st.size = 0;
    st.top = NULL;
    for (v = 0; v < numCourses; v++) {
        if (indegree[v] == 0)
            push(&st, v);
    }

    while (!isEmpty(&st)) {
        curcourseid = pop(&st);
        ccount++;

        if (curcourseid != -1) {
            int *course_arr = adjlist[curcourseid];
            if (course_arr) {
                for (j = 0; j < 30; j++) {
                    if (course_arr[j] != -1) {
                        indegree[course_arr[j]]--;

                        if (indegree[course_arr[j]] == 0)
                            push(&st, course_arr[j]);
                    }

                }
            }
        }
    }
    return (ccount == numCourses);
}