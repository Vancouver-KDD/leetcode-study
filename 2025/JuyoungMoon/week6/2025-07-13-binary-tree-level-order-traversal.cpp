// Author: Juyoung Moon

// KDD LeetCode Study Week 6: Trees (DFS/BFS)
// https://github.com/juyomo/leetcode-study

// LeetCode #102.
// https://leetcode.com/problems/binary-tree-level-order-traversal/

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<pair<TreeNode*, int>> tovisit;
        if (root == nullptr) {
            return {};
        }

        vector<vector<int>> ans;
        tovisit.push(make_pair(root, 0));

        while (!tovisit.empty()) {
            auto curr = tovisit.front();
            int depth = curr.second;
            tovisit.pop();

            if (curr.first != nullptr) {
                if (ans.size() <= depth) {
                    ans.resize(depth + 1);
                }
                ans[depth].push_back(curr.first->val);
                tovisit.push(make_pair(curr.first->left, depth+1));
                tovisit.push(make_pair(curr.first->right, depth+1));
            }
        }
        return ans;
    }
};
