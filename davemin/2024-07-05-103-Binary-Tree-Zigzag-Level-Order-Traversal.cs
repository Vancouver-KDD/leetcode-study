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
    IList<IList<int>> result  = new List<IList<int>>();
    public IList<IList<int>> ZigzagLevelOrder(TreeNode root) {        
        DoTraversal(root,0);
        int i=0;
        while(i<result.Count){
            if(i%2 == 1){
                IList<int> tmp = new List<int>(result[i].Reverse());
                result[i]= new List<int>(tmp);
                //Console.WriteLine(String.Concat(tmp));
            }
            i++;
        }
        return result;
    }

    public void DoTraversal(TreeNode node, int lev){
        if(node == null) return;
        if(result.Count < lev+1){
            result.Add(new List<int>());
        }
        //Console.WriteLine(node.val);
        result[lev].Add(node.val);
        lev++;
        DoTraversal(node.left, lev);        
        DoTraversal(node.right,lev);
        
        return;
    }
}
