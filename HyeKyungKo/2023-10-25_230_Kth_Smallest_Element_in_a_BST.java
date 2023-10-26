We can use inorder traversal(left->root->right). Since the input tree is a BST, left child's value is smaller than the root value, and the right child's value is bigger than root's value. 

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

[idea 1: iterative inorder traversal - Stack]

//Time Complexity: O(H + K),  This complexity is defined by the stack, which contains at least H+k elements, since before starting to pop out one has to go down to a leaf. This results in O(logN+k) for the balanced tree and O(N+k) for completely unbalanced tree with all the nodes in the left subtree.
//Space Complexity: O(H)
 
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        if( root == null || k <= 0){
            return -1;
        }
        
        Stack<TreeNode> stack = new Stack<>();
        int count  = 0;
        stack.push(root);
        
        while(!stack.isEmpty()){
            
            while(root != null){
                if(root.left != null){
                    stack.push(root.left);
                }
                root = root.left;
            }
            
            TreeNode node = stack.pop();
            count++;
            if(count == k){
                return node.val;
            }
            root = node.right;
        }
        
        return -1;
    }
}


//idea 2: recursive call inorder traversal ( left < root < right  )
//Time Complexity: O(H + K)
//Space Complexity: O(H) 
class Solution {
    
    int count = 0;
    public int kthSmallest(TreeNode root, int k) {
        if(root == null || k <= 0){
            return -1;
        }
        
       return dfs(root, k);
    }
    
    int dfs(TreeNode root, int k){
        if(root == null){
            return -1;
        }
        
        int result = dfs(root.left, k);
        if(result < 0){
            count++;
            if(count == k){
               return root.val;
            }
            result = dfs(root.right, k);
        }

        return result;
    }
}

