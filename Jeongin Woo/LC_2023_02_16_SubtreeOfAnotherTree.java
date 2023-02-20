
public class LC_2023_02_16_SubtreeOfAnotherTree {
	 
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
	
	  public boolean isSubtree(TreeNode root, TreeNode subRoot) {
	        if(root == null){
	            return false;
	        }
	        if(subRoot == null){
	            return true;
	        }
	        if(root.val == subRoot.val){
	           if(isSame(root,subRoot))
	           return true;
	        }

	        return isSubtree(root.left,subRoot) || isSubtree(root.right,subRoot);
	    }
	  
	    public boolean isSame(TreeNode a, TreeNode b){
	        if(a ==null && b== null){
	            return true;
	        }
	        if(a ==null || b==null){
	            return false;
	        }
	        if(a.val != b.val){
	            return false;
	        }
	        return isSame(a.left,b.left) && isSame(a.right,b.right);


	    }

	  

}
