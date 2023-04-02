

public class LC_2023_02_19_KthSmallestElementInaBST {
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
	
	int count = 0;
	int result = Integer.MIN_VALUE;

	public int kthSmallest(TreeNode root, int k) {
	    traverse(root, k);
	    return result;
	}

	public void traverse(TreeNode root, int k) {
	    if(root == null) return;
	    traverse(root.left, k);
	    count ++;
	    if(count == k) result = root.val;
	    traverse(root.right, k);       
	}

	
}
