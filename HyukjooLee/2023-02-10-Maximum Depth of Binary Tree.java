// Given the root of a binary tree, return its maximum depth.
// A binary tree's maximum depth is the number of nodes
// along the longest path from the root node down to the farthest leaf node.

// find the maximum depth of a binary tree

// 1. using recursion +  DFS 
// check to see if the root node is null => if it is, return 0
// maxDepth method will return the depth of left & right subtrees 
// maximum depth of a node = the maximum depth of its subtrees + 1

// time complexity is O(N) = the number of nodes
// space complexity is O(N) if the tree is completely unbalanced
// could be O(logN) if tree is completely balanced because of the height of the tree = O(logN)
class Solution {
    public int maxDepth(TreeNode root) {
        return (root == null ) ? 0 : 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}

// 2. using iterative + BFS
// using queue to keep track of the nodes
// processes the nodes in the queue level by level (starting from root node)
// adding the children of each node to the queue
// count the number of levels processed => return
// time complexity is O(N) = the number of nodes in tree
// space complexity is O(n) = max size of the queue = the number of nodes in tree
class Solution {
    public int maxDepth(TreeNode root) {
      if(root == null) return 0;
      Queue<TreeNode> que = new LinkedList<>();
      que.offer(root);
      int depth = 0;
      while(!que.isEmpty()) {
        for(int i = 0; i < que.size(); i++) {
          TreeNode node = que.poll();
          if(node.left != null) que.offer(node.left);
          if(nod.right != null) que.offer(node.right);
        }
        depth++;
      }
      return depth;
    }
}
