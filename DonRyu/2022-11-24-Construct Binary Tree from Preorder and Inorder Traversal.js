var buildTree = function(preorder, inorder) {
  return helper(preorder, inorder, 0, 0, inorder.length - 1);
};

var helper = function (preorder, inorder, preIndex, inStart, inEnd) {
  if (preIndex >= preorder.length || inStart > inEnd) return null;

  var index = 0;
  var root = new TreeNode(preorder[preIndex]);

  for (var i = inStart; i <= inEnd; i++) {
    if (inorder[i] === root.val) {
      index = i;
      break;
    }
  }

  if (index > inStart) root.left = helper(preorder, inorder, preIndex + 1, inStart, index - 1);
  if (index < inEnd) root.right = helper(preorder, inorder, preIndex + index - inStart + 1, index + 1, inEnd);

  return root;
};
