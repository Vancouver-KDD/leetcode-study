#include "common.h"


struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};



int maxDepth(struct TreeNode* root){
    if (!root) return 0;
    int left_depth = maxDepth(root->left);
    int right_depth = maxDepth(root->right);
    if(left_depth > right_depth) return left_depth + 1;
    else return right_depth + 1;
}