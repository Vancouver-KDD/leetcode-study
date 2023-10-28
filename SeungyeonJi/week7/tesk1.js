var recursive = function () {
  if (!root) return 0;

  let max = 0;

  function recur(root) {
    if (!root) return 0;

    let left = recur(root.left);
    let right = recur(root.right);

    max = Math.max(left + right, max);

    return Math.max(left, right) + 1;
  }

  recur(root);
  return max;
};
