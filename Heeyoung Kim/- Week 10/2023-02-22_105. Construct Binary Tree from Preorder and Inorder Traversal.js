var buildTree = function(preorder, inorder) {
    let p =0, i=0;
    let build = (stop) => {
        if(inorder[i] != stop) {
            var root = new TreeNode(preorder[p++]);
            root.left = build(root.val);
            i++;
            root.right = build(stop);
            return root;
        }

        return null;
    }

    return build();
}