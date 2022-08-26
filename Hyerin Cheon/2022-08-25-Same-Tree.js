function isSameTree(p, q){
  // empty tree -> if both nodes are null 
  if(!p && !q) return true;

  // not same if either of the nodes is null or values are different
  if(!p || !q || p.val !== q.val) return false;

  // recursive step
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}