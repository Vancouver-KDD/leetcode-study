function invertTree(root){
  if(!root) return root;

  //save node temporary
  const temp = root.left;
  
  // invert nodes
  root.left = invertTree(root.right);
  root.right = invertTree(temp)

  return root;
}