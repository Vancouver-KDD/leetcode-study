// 98. Validate Binary Search Tree
// Given the root of a binary tree, determine if it is a valid binary search tree (BST).

// A valid BST is defined as follows:

// The left 
// subtree
//  of a node contains only nodes with keys less than the node's key.
// The right subtree of a node contains only nodes with keys greater than the node's key.
// Both the left and right subtrees must also be binary search trees.

var isValidBST = function(root) {
    return validate(root, -Infinity, Infinity);
};

var validate = function(node,lower,upper){
    if (node == null){return true;}
    if((lower < node.val) && ( node.val < upper )){
        return validate(node.left,lower,node.val) && validate(node.right, node.val, upper);
    }else{ return false;}   
}

//Time Complexity : O(N)
//Space Complexity : O(1)