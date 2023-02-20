

public class LC_2023_02_17_LowestCommonAncesterOfaBST {
	public class TreeNode {
	      int val;
	      TreeNode left;
	      TreeNode right;
	      TreeNode() {}
	      TreeNode(int val) { this.val = val; }
	      TreeNode(int val, TreeNode left, TreeNode right) {
	          this.val = val;
	          this.left = left;
	          this.right = right;
	      }
	  }
	
	public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode current = root;
        while(current != null){
            if(p.val > current.val && q.val > current.val)
            current = current.right;
            else if(p.val < current.val && q.val < current.val)
            current = current.left;
            else
            return current;

        }
        return current;
        
    }

}
