// 235. Lowest Common Ancestor of a Binary Search Tree
// Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

// According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



var lowestCommonAncestor = function(root, p, q) {
    // If the value of root node is greater than the value of p node and less than the value of q node...
    if(root.val > p.val && root.val < q.val){
        return root;
    }
    // If the value of p node and the q node is less than the value of root node...
    else if(root.val > p.val && root.val > q.val){
        return lowestCommonAncestor(root.left, p, q);
    }
    // If the value of p node and the q node is greater than the value of root node...
    else if(root.val < p.val && root.val < q.val){
        return lowestCommonAncestor(root.right, p, q);
    }
    return root;
};

//Time Complexity : O(N)
//Space Complexity : O(1)