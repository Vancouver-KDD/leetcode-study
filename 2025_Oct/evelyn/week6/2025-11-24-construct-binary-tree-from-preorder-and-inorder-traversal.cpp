/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    unordered_map<int, int> inorderMap;
    int pRootIdx = 0;

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int n = inorder.size();
        for (int i = 0; i < n; i++) inorderMap[inorder[i]] = i;

        return helper(preorder, 0, n - 1);
    }

    TreeNode* helper(vector<int>& preorder, int left, int right) {
        if (left > right) return nullptr;

        int rootVal = preorder[pRootIdx];
        pRootIdx++;

        TreeNode* root = new TreeNode(rootVal);
        int iRootIdx = inorderMap[rootVal];

        root->left = helper(preorder, left, iRootIdx - 1);
        root->right = helper(preorder, iRootIdx + 1, right);

        return root;
    }
};