/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */


//  104. Maximum Depth of Binary Tree
//  Given the root of a binary tree, return its maximum depth.

//  A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


 var maxDepth = function(root) {
    let answer = 0;
   if (root == null) return answer;
 
  let depth = 1;
  
  const helper = (root, depth) => {
      if(root === null) return;
          
      if (root.left == null && root.right == null) {
          answer = Math.max(answer, depth);
          return;
      }
      
      helper(root.left, depth + 1);
      helper(root.right, depth + 1);
  }
  
  helper(root, depth);
  
  return answer;
};