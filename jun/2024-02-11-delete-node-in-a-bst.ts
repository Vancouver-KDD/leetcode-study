function findSmallist(root: TreeNode): TreeNode {
  if (root.left) {
    return findSmallist(root.left)
  }
  return root
}

function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
  if (root === null) {
    return root
  }
  if (root.val < key && root.right) {
    root.right = deleteNode(root.right, key)
  } else if (root.val > key && root.left) {
    root.left = deleteNode(root.left, key)
  } else if (key === root.val) {
    if (!root.right) {
      root = root.left
    } else {
      if (root.left) {
        findSmallist(root.right).left = root.left
      }
      root = root.right
    }
  }
  return root
}
