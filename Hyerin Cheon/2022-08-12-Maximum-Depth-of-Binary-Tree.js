function maxDepth(root){
  if(!root) return 0;

  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
  // 1 for top(root) value
}