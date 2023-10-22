/*
 * https://leetcode.com/problems/binary-tree-right-side-view/
 * 
 * ## Description
 * Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
 * 
 * ## Example
 * Input: root = [1,2,3,null,5,null,4] Output: [1,3,4] 
 */

class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        //Initialize the result array
        List<Integer> result = new ArrayList<>();

        //queue will store the nodes in a row 
        Queue<TreeNode> queue = new LinkedList<>();
        
        //Set early exit condition
        if (root == null) return result; 

        //store the root in queue to start traversing 
        queue.offer(root);

        //traverse all the nodes in the binary tree
        while(!queue.isEmpty()){   
            //will iterate x time where x is the number of nodes in a row that we are traversing
            int size = queue.size();
            for(int i = 0; i < size; i++) {
                //poll the queue and store it in current pointer. 
                TreeNode curr = queue.poll(); 
                // since we are storing the right value first in queue, in first iteration for the row(i=0), the curr pointer will point the right most value!! 
                if(i == 0) result.add(curr.val); 
                //store right child first for next row iteration if there is. 
                if(curr.right != null) queue.offer(curr.right);
                //store left child for next row iteration if there is
                //because there is a chance that there isn't any right value, then the left child could be the right most value. 
                if(curr.left != null) queue.offer(curr.left);
            }
        }

        return result;
    }
}