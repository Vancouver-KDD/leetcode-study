
import java.util.*;

public class SameTree {
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
	
	public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null)
            return true;
        if(p == null || q == null)
            return false;
        if(p.val != q.val)
            return false;
        Stack<TreeNode> stackP = new Stack<TreeNode>();
        Stack<TreeNode> stackQ = new Stack<TreeNode>();    
        stackP.push(p);
        stackQ.push(q);
        while(!stackP.isEmpty() && !stackQ.isEmpty()){
            TreeNode tempP = stackP.pop();
            TreeNode tempQ = stackQ.pop();
            if(tempP.val != tempQ.val){
                return false;
            }
            if(tempP.left != null && tempQ.left ==null)
                return false;
            else if(tempP.left == null && tempQ.left !=null)
                return false;
            else if(tempP.right != null && tempQ.right ==null)
                return false;   
            else if(tempP.right == null && tempQ.right !=null)
                return false;
            if(tempP.left != null && tempQ.left != null){
                stackP.push(tempP.left);
                stackQ.push(tempQ.left);
            }
            if(tempP.right != null && tempQ.right !=null){
                 stackP.push(tempP.right);
                 stackQ.push(tempQ.right);
            }
        }  
            return true;
    } 



}
