/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
		int temp = root->val;   // Present root node value
        
        // If both p and q are less than the root value Then go for the left subtree of the root
        if(p->val < temp && q->val < temp){
			 return lowestCommonAncestor(root->left, p, q);
        }
        // If both p and q are greater than the root value Then go for the right subtree of the root
        else if(p->val > temp && q->val > temp){
			return lowestCommonAncestor(root->right, p, q);
        }else{
            return root;
			 // the present root is the solution;
        }
    }
};