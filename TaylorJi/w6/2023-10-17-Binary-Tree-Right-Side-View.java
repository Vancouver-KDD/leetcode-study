class Solution {
    List<Integer> result = new ArrayList<Integer>();
    public List<Integer> rightSideView(TreeNode root) {
        recursionHelper(root, 0);
        return result;

    }
    void recursionHelper (TreeNode node, int level) {
        if (node == null) return;

        // if the root has both right and left, this condition will only add the right node to the result
        if (result.size() == level) {
                result.add(node.val);
        }

        recursionHelper(node.right, level + 1);
        recursionHelper(node.left, level + 1);
    }
    
}