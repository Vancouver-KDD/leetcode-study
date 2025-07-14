function diameterOfBinaryTree(root: TreeNode | null): number {
  let diameter = 0;

  function dfs(node: TreeNode | null): number {
    if (node === null) return 0;

    const leftDepth = dfs(node.left);
    const rightDepth = dfs(node.right);

    diameter = Math.max(diameter, leftDepth + rightDepth);

    return 1 + Math.max(leftDepth, rightDepth);
  }

  dfs(root);
  return diameter;
}
