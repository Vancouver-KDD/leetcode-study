// Given the roots of two binary trees p and q,
// write a function to check if they are the same or not.

// Two binary trees are considered the same 
// if they are structurally identical, and the nodes have the same value.


// 1. comparing the nodes of the trees, level by level (BFS)
// using queue to store the nodes of the trees
// two nodes at the front of the queue are removed and compared
class Solution {
  public boolean isSameTree(TreeNode p, TreeNode q) {
    // uses a queue to store the nodes of the tree
    Queue<TreeNode> que = new LinkedList<TreeNode>();
    que.add(p);
    que.add(q);

    while(!que.isEmpty()) {
        // two nodes at the front of the queue are removed and compared
        p = que.poll();
        q = que.poll();
        // if both nodes are null,
        // the code continues to the next iteration of the loop
        if (p == null && q == null) continue;
        // if one of the nodes is null and the other is not null,
        // return false, means that the trees is not same
        if (p == null || q == null) return false;
        //if their values are not equal,
        // return false as well
        if (p.val != q.val) return false;
        // left and right children of the nodes; for the next iteration
        que.add(p.left);
        que.add(q.left);
        que.add(p.right);
        que.add(q.right);
    }
    return true;
  }
}