
/**
 * https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
 * Time O(N) | Space O(H)
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    if(p.val <root.val && q.val < root.val)
    return lowestCommonAncestor(root.left,p,q)
    else if(p.val > root.val && q.val > root.val){
        return lowestCommonAncestor(root.right,p,q)
    } else {
        return root
    }
};
/**
 * https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
 * Time O(N) | Space O(1)
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
 var lowestCommonAncestor = function(root, p, q) {
    while (root !== null) {
        const isGreater = (root.val < p.val) && (root.val < q.val)
        if (isGreater) {
            root = root.right;
            continue;
        }

        const isLess = (p.val < root.val) && (q.val < root.val);;
        if (isLess) {
            root = root.left;
            continue;
        }

        break;
    }

    return root;
};
  