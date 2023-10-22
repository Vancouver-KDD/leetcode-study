function inorderTraversal(root) {
  let list = [];

  function inorder(root) {
    if (!root) return;

    if (root.left) {
      inorder(root.left);
    }
    list.push(root.val);
    if (root.right) {
      inorder(root.right);
    }
  }
  inorder(root);
  return list;
}
