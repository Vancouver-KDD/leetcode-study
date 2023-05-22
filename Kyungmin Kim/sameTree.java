class Solution{
    public boolean isSameTree(TreeNode p, TreeNode q){
        return dfs(p,q);
    }
    private boolean dfs(TreeNode p, TreeNode q){
        if(p == null && q == null){
            return true;
        }
        if(p == null || q == null){
            return false;
        }
        if(p.val != q.val){
            return false;
        }
        boolean left = dfs(p.left, q.left);
        boolean right = dfs(p.right, q.right);

        return left && right;
    }
}