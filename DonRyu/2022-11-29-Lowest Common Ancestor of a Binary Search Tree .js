/* Start at root and check if p and q are less, then go left, otherwise go right. */
var lowestCommonAncestor = function(root, p, q) {
    if (root.val > p.val && root.val > q.val) {
        return lowestCommonAncestor(root.left, p, q);
    }
    else if (root.val < p.val && root.val < q.val) {
        return lowestCommonAncestor(root.right, p, q);
    }
    else {
        return root;
    }
}
