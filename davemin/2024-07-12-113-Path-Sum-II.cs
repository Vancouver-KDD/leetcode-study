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

    IList<IList<int>> result = new List<IList<int>>();
    public IList<IList<int>> PathSum(TreeNode root, int targetSum) {
        DoPreOrderTraversal(root,0,new List<int>(), targetSum);
        return result;
    }

    public void DoPreOrderTraversal(TreeNode node, int sum, List<int> visitedNode, int targetSum){
            if(node ==null) return;

            sum+=node.val;
            visitedNode.Add(node.val);
            if(node.left==null && node.right==null && sum==targetSum){
                    result.Add(new List<int>(visitedNode));
            }
            DoPreOrderTraversal(node.left,sum,visitedNode,targetSum);
            DoPreOrderTraversal(node.right,sum,visitedNode,targetSum);
            visitedNode.RemoveAt(visitedNode.Count-1);
            return ;
    }
}
