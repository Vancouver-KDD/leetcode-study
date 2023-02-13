import java.util.*;

public class MaximumDepthOfBinaryTree {
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
	//recursion
    public int maxDepth1(TreeNode root) {
        if(root == null)
        return 0;
        int left = maxDepth1(root.left);
        int right = maxDepth1(root.right);
        return Math.max(left,right)+1;
    }
	//iterative
	public int maxDepth(TreeNode root) {
	        Stack<TreeNode> stack = new Stack<>();
	        Stack<Integer> intStack = new Stack<>();
	        stack.push(root);
	        intStack.push(1);
	        int max = 0;
	        while(!stack.isEmpty()){
	           TreeNode temp =stack.pop();
	           int value = intStack.pop();
	           if(temp.left == null && temp.right == null){
	              return  Math.max(max,value);
	           }
	           else{
	               if(temp.left != null){
	                   stack.push(temp.left);
	                   intStack.push(value+1);
	               }
	               if(temp.right != null){
	                   stack.push(temp.right);
	                   intStack.push(value+1);
	               }
	           }
	        }return max;
	
	    }

}
