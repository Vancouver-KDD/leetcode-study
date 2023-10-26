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

//2023-10-23
//Idea:  preorder traversal by recursive call
//Time Complexity: O(N) 
//Space Complexity: O(N) - recursive call stack size - its worst case is O(N), general case is O(logN)
class Solution {
    
    int totalSum = 0;
    public int sumNumbers(TreeNode root) {
        
        visitTree(root, 0);
        return totalSum;
    }
    
    //intput: [4,9,0,5,1]
    // 4 (9 (5 -49, 1-49)-4, 0 -4)-0
    //number:0, 4, 49, 495, 491, 4
    //newNumber: 4, 49, 495, 491, 40
    //totalSum: 495 + 491 + 40
    void visitTree(TreeNode root, int number){
        if(root == null){
            return;
        }
        
        int newNumber = number * 10 + root.val;
        if(root.left == null && root.right == null){            
            totalSum += newNumber;
            return;
        }
        
        visitTree(root.left, newNumber);
        visitTree(root.right, newNumber);
        
    }
}