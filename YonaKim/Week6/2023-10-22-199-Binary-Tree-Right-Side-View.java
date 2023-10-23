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

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
 
/**
queue.remove()
queue.peek()
queue.add()
queue.size()

Time Complexity: O(N), visiting each node.
Space Complexity: O(D) for queues, D is the tree diameter. 
 */
 class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();

        if(root == null) {
            return result;
        }

        Queue<TreeNode> curr = new LinkedList<TreeNode>();
        Queue<TreeNode> next = new LinkedList<TreeNode>();

        curr.add(root);
        
        while(!curr.isEmpty()) {
            next = new LinkedList<TreeNode>();
            //fill in next by removing one element each from queue
            //if queue size is one, add to result
            while(curr.size() > 0) {
                TreeNode node = curr.remove();
                if(node != null) {
                    if(node.left != null) next.add(node.left);
                    if(node.right != null) next.add(node.right);
                }
                if(curr.size() == 0 && node != null) {
                    result.add(node.val);
                } 
            }
            curr = next;
        }

        return result;
    }
}