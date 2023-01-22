
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
        queue<TreeNode*> q;         // queue
        vector<vector<int>> res;    // result
        vector<int> temp;           // temp vector for storing level-wise nodes
        
        // base condition
        if(!root) return res;

        // push root and null for distinguishing levels (acts as marker)
        q.push(root);
        q.push(nullptr);
        
        while(!q.empty()){  // while queue is not empty..
            TreeNode *top = q.front();
            q.pop();
            
            // check if queue front node is null
            // if not null, push node into temp => push temp in res and clear temp for next level
            if(!top){
                res.push_back(temp);
                temp.clear();
                
                // push null to mark end of next level
                // (child nodes already in queue)
                if(!q.empty()){
                    q.push(nullptr);
                    continue;
                }
                // return res if queue is empty
                // (no further nodes to traverse)
                return res;
            }
            else temp.push_back(top->val);
            
            if(top->left) q.push(top->left);
            if(top->right) q.push(top->right);
        }
        return res;
    }
};


// TC: O(N)
// SC: O(W); W = width of tree
// keep count of each level; visit every node L->R order
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
        
        vector<vector<int>> res;
        vector<int> temp;
        queue<TreeNode*> q;
        
        q.push(root);
        q.push(nullptr);
        
        while(q.size()){
            root = q.front();
            q.pop();
            
            if(!root){
                if(temp.size()) res.push_back(temp);
                temp.clear();
                
                q.push(nullptr);
                if(!q.front()) break;
                
                continue;
            }
            temp.push_back(root->val);
            if(root->left) q.push(root->left);
            if(root->right) q.push(root->right);
        }
        return res;
    }
};
