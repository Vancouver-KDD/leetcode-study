
// preorder : root->left->right
// inorder : left->root->right

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
private:
    int cur;    
    
public:
    TreeNode* makeTree(vector<int> &pre, vector<int> &in, int l, int r){
        
        if(l>r) return nullptr;
        
        int i = find(in.begin(), in.end(), pre[cur]) - in.begin();
        TreeNode *root = new TreeNode(in[i]);
        
        cur++;
        root->left = makeTree(pre,in,l,i-1);
        root->right = makeTree(pre,in,i+1,r);
        
        return root;
    }
    
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int n = inorder.size();
        cur = 0;
        
        return makeTree(preorder,inorder,0,n-1);
    }
};