
public class LC_2023_02_18_ValidBST {
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
	
	public boolean isValidBST(TreeNode root) {
        return valid(root,null,null);
    }

    public boolean valid(TreeNode root,Integer max, Integer min){
    	//루트가 없다는건 바이너리 공식에 맞음
        if(root == null)
        return true;
        //왼쪽트리는 크더라도 루트보단 작아야하고,  얼마나 적을지는 상관 없음
        // 오른쪽트리는 작더라도 루트보단 커야하고 얼마나 클지는 상관없음
        // 즉 루트가 왼쪽트리보다 작거나 같은경우 || 루트가 오른쪽트리보다 크거나 같은경우 > 거짓
        else if(max !=null && max <= root.val || min!=null && root.val <= min)
        return false;
        else{
            return valid(root.left,root.val,min) && valid(root.right,max,root.val);
        }
    }


}
