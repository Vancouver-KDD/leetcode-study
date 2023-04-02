// 230. Kth Smallest Element in a BST

// Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



var kthSmallest = function(root, k) {
    let tree=root, count=1, val;

    let inOrder = (tree) => {
        if(!tree) return;
        inOrder(tree.left);
        if(count === k){
            val = tree.val;
        }
        count++;
        inOrder(tree.right);
    }

    inOrder(tree);

    return val;
};


//Time Complexity : O(N)
//Space Complexity : O(1)