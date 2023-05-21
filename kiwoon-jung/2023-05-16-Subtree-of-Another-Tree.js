var isSubtree = function (root, subRoot) {
  if (subRoot && !root) return false;

  if (isMatch(root, subRoot)) return true;

  return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};

function isMatch(r, s) {
  if (r && s) {
    return (
      r.val === s.val && isMatch(r.left, s.left) && isMatch(r.right, s.right)
    );
  }

  if (!r && s) return false;
  if (r && !s) return false;
  if (!r && !s) return true;
}
