// Given the root of a binary tree, invert the tree, and return its root

// binary tree
// 엄격하게 왼쪽과 오른쪽 노드를 참조 하고, 최대 2개의 하위 노드만 포함하는 트리

// input
         4
    2          7
 1     3    6     9  


// output

         4
    7          2
 3     1    9     6  


// Depth-First Search
// what is DFS?
// the algorithm visits the vertices or nodes in a graph or tree 
// by going deeper into the them as much as possible before backtracking

// think how to swap their position

// 1. using depth-first search approach
// calls left and right children of each node recursively
// when the base case is reached, the function returns null => ends the recursion 
// when recursive calls on the left and right children have completed,
// swap them, and returns the root of the inverted tree
// time complexity is O(N) as every nodes in the tree are visited
// space complexity is O(N) as function calls are placed on the stack; the height of tree
class Solution {
    public TreeNode invertTree(TreeNode root) {
        // base case
        if(root == null) return root;
        
        // swap
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        // traverse left til the null is reached
        invertTree(root.left);
        // traverse right
        invertTree(root.right);

        // return node after swapping
        return root;
    }
}


// 2. using Breadth-First Search approach
// what is BFS?
// traverse/search a graph or tree 
// visiting all the nodes at the same level before moving on to the next level
// time complexity is O(N) as every nodes in the tree are visited
// space complexity is O(N) as queue stores all of the nodes at any level in the worst case
class Solution {
    public TreeNode invertTree(TreeNode root) {
        // if the current node is null, return null
        if (root == null) return null;

        Queue<TreeNode> queue = new LinkedList<>();
        // add the root node to the queue
        queue.offer(root);
        
        // traverse nodes until the queue is empty
        while (!queue.isEmpty()) {
          // take the next node from the front of the queue
          TreeNode node = queue.poll();
          
          // swap the left and right children of the current node
          TreeNode temp = node.left;
          node.left = node.right;
          node.right = temp;
          
          // if there is a child node, add it to the queue
          if (node.left != null) queue.offer(node.left);
          if (node.right != null) queue.offer(node.right);
        }

        return root;
  }
}