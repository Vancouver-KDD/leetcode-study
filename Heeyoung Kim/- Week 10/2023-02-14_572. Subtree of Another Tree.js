// 572. Subtree of Another Tree
// Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

// A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
 const isSubtree = (root, subRoot) => {
    const areEqual = (node1, node2) => {
      if (!node1 || !node2) return !node1 && !node2;
      if (node1.val !== node2.val) return false;
      return areEqual(node1.left, node2.left) && areEqual(node1.right, node2.right);
    }
    const dfs = (node) => {
      if (!node) return false;
      if (areEqual(node, subRoot)) return true;
      return dfs(node.left) || dfs(node.right);
    }
    return dfs(root);
  };

  //Time Complexity : O(N)
  //Space Complexity : O(1)