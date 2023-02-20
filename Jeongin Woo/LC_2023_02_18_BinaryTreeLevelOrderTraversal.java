import java.util.*;

public class LC_2023_02_18_BinaryTreeLevelOrderTraversal {
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
	public List<List<Integer>> levelOrder(TreeNode root) {
        // show the total result ex) [[1,2],[3],[4,5]]
        List<List<Integer>> result = new ArrayList<>(); 
        if(root == null) return result;      
        //store integer value
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while(!queue.isEmpty()){
            List<Integer> indi = new ArrayList<>();
            int count = queue.size();
            for(int i = 0 ; i < count ; i++){
                TreeNode node = queue.poll();
                indi.add(node.val);
                if(node.left!=null){ queue.add(node.left);}
                if(node.right!=null){ queue.add(node.right);}
            }   
             result.add(indi);
        } 
       return result;
    } 

}
