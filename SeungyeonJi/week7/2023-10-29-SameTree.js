var isSame = function (p, q) {
  //To check if the structure of both tree is the same
  if (!p && !q) return true;
  if (!p || !q || p.val !== q.val) return false;
  return isSame(p.left, q.left) && isSame(p.right, q.right);
};
