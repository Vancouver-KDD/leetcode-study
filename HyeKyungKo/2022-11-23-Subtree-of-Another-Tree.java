/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
 //2022-11-23 - iteration
 //Time Complexity: O(NxN) <-- N 은 root tree 의 노드수, M 은 subRoot tree 의 노드수 
 //Space Complexity: O(N+M) 이라고 하네 
 /*
 There will be at most NNN recursive call to dfs ( or isSubtree). Now, each of these calls will have MMM recursive calls to isIdentical. Before calling isIdentical, our call stack has at most O(N) elements and might increase to O(N+M) during the call. After calling isIdentical, it will be back to at most O(N)since all elements made by isIdentical are popped out. Hence, the maximum number of elements in the call stack will be M+N
 */

class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if(subRoot == null){
            return true;
        }else if(root == null ){
            return false;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while(!queue.isEmpty()){
            TreeNode node = queue.remove();
            if(node.val == subRoot.val){
                if(isSametree(node, subRoot)){// the subRoot tree is included.
                    return true;
                }
            }
            if(node.left != null){
                queue.add(node.left);
            }
            if(node.right != null){
                queue.add(node.right);
            }
        }

        return false; 
    }

    private boolean isSametree(TreeNode root, TreeNode subRoot){
        if(root == null && subRoot == null){
            return true;
        }else if( root == null || subRoot == null){
            return false;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);//add orginal node
        queue.add(subRoot);//add compared node

        while(!queue.isEmpty()){
            TreeNode orgNode = queue.remove();
            TreeNode comparedNode = queue.remove();

            if(orgNode == null && comparedNode == null){
                continue; //same
            }else if(orgNode == null || comparedNode == null){
                return false; // not same
            }

            if(orgNode.val != comparedNode.val){
                return false; //not same
            }

            queue.add(orgNode.left);
            queue.add(comparedNode.left);
            queue.add(orgNode.right);
            queue.add(comparedNode.right);
        }

        return true; //same
    }
}