/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    IList<string> result = new List<string>();
    public IList<string> BinaryTreePaths(TreeNode root) {
        string curr= "";
        DoTraversal(root, curr);               
        return result;
    }

    public void DoTraversal(TreeNode node, string curr){
        if(node == null) return;
        if(node.left == null && node.right == null) {
            curr +=node.val;
            result.Add(curr.ToString());
            return;
        }else{
            curr += (node.val + "->"); 
            DoTraversal(node.left, curr);  
            DoTraversal(node.right, curr);  
        }
        return;
    }
}
