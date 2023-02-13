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
class Solution
{
    StringBuilder strP = new StringBuilder();
    StringBuilder strQ = new StringBuilder();
    public boolean isSameTree(TreeNode p, TreeNode q)
    {
        DoIsSameTree(p, strP);
        DoIsSameTree(q, strQ);
        return (strP.toString()).equals(strQ.toString()) ? true : false;
    }

    public void DoIsSameTree(TreeNode node, StringBuilder strb)
    {
        if (node == null)
        {
            strb.append('X');
            return;
        }
        strb.append(Integer.toString(node.val));
        DoIsSameTree(node.left, strb);
        DoIsSameTree(node.right, strb);
        return;
    }
}