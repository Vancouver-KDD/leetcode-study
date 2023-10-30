class Solution {
    int result=0;
    public void sum(TreeNode root, int num) {
        if(root == null) return;
        num = root.val + ( 10 * num);

        if(root.left == null && root.right == null){
            result += num;
        }
        sum(root.left, num);
        sum(root.right, num);
    }
    public int sumNumbers(TreeNode root) {
        sum(root, 0);
        return result;
    }
}