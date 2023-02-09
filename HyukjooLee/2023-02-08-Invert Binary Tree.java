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

// Review

// 트리를 invert 하는 문제, 한 parent 노드가 갖는 자식들의 (오른쪽 왼쪽) 위치를 swap 해서 리턴하는 문제
// DFS approach 
// DFS 란 그래프나 트리 안에 노드의 정점을 방문하면서
// backtracking 이 가능할 때까지, downward 로 방문하면서 서치하는 알고리즘 = 수직으로 

// 방문될 root 노드가 null 이 될때 까지 (base case)
// 왼쪽, 오른쪽 노드의 위치를 바꿔주고
// 재귀적으로 노드의 children (left and right node) 를 호출해준다
// invert 된 루트를 리턴함  
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

// Review
// BFS 란 그래프나 트리 안에 같은 레벨에 있는 모든 노드를 방문하면서 
// 모든 노드가 방문 될 때까지 서치하는 알고리즘 = 너비 우선 탐색
// nodes are waiting to be processed
// queue is used to store all neighbor nodes
// the use of a queue in BFS provides a way to ensure that the search is done in a breadth-first manner
// i.e., all the nodes at a given level are processed before moving on to the next level

// swap left and right child of all nodes in the tree
// using queue to store nodes whose left and right child not swapped yet
// remove the next node from the queue until queue is not empty
// and swap child nodes
// add child nodes to the queue
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