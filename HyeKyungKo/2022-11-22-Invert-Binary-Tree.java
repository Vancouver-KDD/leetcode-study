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
 2022-11-22
 //Recursive 
 //Time Complexity: O(N)
 //Space Complexity: O(N)
 class Solution{
     public TreeNode invertTree(TreeNode root){

         recursiveInvert(root);

         return root;
     }

     public void recursiveInvert(TreeNode root){
         if(root == null){
             return;
         }

         TreeNode temp = root.left;
         root.left = root.right;
         root.right = temp;
        recursiveInvert(root.left);
        recursiveInvert(root.right);
     } 
 }
 //Iteration case 
 //Time Complexity: O(N)
 //Space Complexity: O(N) <-- Queue 에 들어갈수 있는 max 값이 tree node 수 
 /*
class Solution{
    public TreeNode invertTree(TreeNode root){
        if(root == null){
            return root;
        }

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        while(!queue.isEmpty()){
            TreeNode node = queue.remove();
            TreeNode temp = node.left;
            node.left = node.right;
            node.right = temp;
            if(node.left != null){
                queue.add(node.left);
            }
            if(node.right != null){
                queue.add(node.right);
            }
        }

        return root;
    }
}
*/