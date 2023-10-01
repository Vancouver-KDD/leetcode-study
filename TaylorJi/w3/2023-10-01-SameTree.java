class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
      if (p == null && q == null) return true;
      if (p == null || q == null) return false;
      Stack<TreeNode> pStack = new Stack <TreeNode>();
      Stack<TreeNode> qStack = new Stack <TreeNode>();
      // push all the treenodes into stack by push p, q
      // benefit of using stack
      // I do not have to consider left and right node 
      // push the head node

      pStack.push(p);
      qStack.push(q);

      //iterate the stack until it is empty 
      // what are cases? 
      // the nodes are different -> false
      // the nodes are equal -> continue, if both are null then continue;



      /**
      inside this loop, all the node will be added into the stack 
      all the node will be validated here 
       */

      while (!pStack.isEmpty() || !qStack.isEmpty()) {
          TreeNode pNode = pStack.pop();
          TreeNode qNode = qStack.pop();
          if (pNode == null && qNode == null) continue;
          if (pNode == null || qNode == null) return false;
          if (pNode.val != qNode.val) return false;
          pStack.push(pNode.left);
          pStack.push(pNode.right);
            qStack.push(qNode.left);
          qStack.push(qNode.right);  
      }



      if (pStack.isEmpty() && qStack.isEmpty()) {
          return true;
      } else {
          return false;
      }
    }
}