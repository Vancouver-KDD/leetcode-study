var diameterOfBinaryTree = function(root) {
    let diameter = 0;
    dfs(root);
    return diameter;

    function dfs(node) {
        if (!node) return 0;

        const left = dfs(node.left);
        const right = dfs(node.right);

        // update diameter at every node
        diameter = Math.max(diameter, left + right);

        // update the max path of the current node
        // 1 is the height of the node itself + longest path of children
        return 1 + Math.max(left, right);
    } 
};