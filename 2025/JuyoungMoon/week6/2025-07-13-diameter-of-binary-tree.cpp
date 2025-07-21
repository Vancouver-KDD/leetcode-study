// Author: Juyoung Moon

// KDD LeetCode Study Week 6: Trees (DFS/BFS)
// https://github.com/juyomo/leetcode-study

// LeetCode #543.
// https://leetcode.com/problems/diameter-of-binary-tree/

class Solution {
public:
    // diameter
    // - passes through root: leftDepth + rightDepth
    // - doesn't pass through root: max(leftMaxDia, rightMaxDia)
    // need to pass up depth and maxDia
    // - depth = max(leftDepth, rightDepth) + 1;
    // - maxDia = max(leftDepth + rightDepth, max(leftMaxDia, rightMaxDia))
    int diaRecur(TreeNode* root, int& depth) {
        if (root == nullptr) {
            depth = 0;
            return 0;
        }

        int leftDepth;
        int rightDepth;
    
        int leftMaxDia = diaRecur(root->left, leftDepth);
        int rightMaxDia = diaRecur(root->right, rightDepth);
        depth = max(leftDepth, rightDepth) + 1;

        return max(leftDepth + rightDepth, max(leftMaxDia, rightMaxDia));
    }

    int diameterOfBinaryTree(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        int depth;
        return diaRecur(root, depth);
    }
};
