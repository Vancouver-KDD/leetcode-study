var isBalanced = function (root) {
  let flag = true;

  const getHeights = (node, height) => {
    if (!node) {
      return 0;
    }

    const leftHeight = getHeights(node.left, height + 1);
    const rightHeight = getHeights(node.right, height + 1);

    if (Math.abs(rightHeight - leftHeight) > 1) {
      flag = false;
    }

    return Math.max(leftHeight, rightHeight) + 1;
  };

  getHeights(root, 0);

  return flag;
};
