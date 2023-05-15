var diameterOfBinaryTree = function (root) {
  if (!root) return 0;

  let max = 0;

  const dfs = (node) => {
    if (!node) return 0;

    let left = dfs(node.left);
    let right = dfs(node.right);

    max = Math.max(left + right, max);

    return Math.max(left, right) + 1;
  };

  dfs(root);
  return max;
};
