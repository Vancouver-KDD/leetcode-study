// Use DFS to add values to an array
// Return the kth index of that array
var kthSmallest = function(root, k) {
    const values = []

    // DFS function
    function dfs(root, values) {
        if(root.left) dfs(root.left, values)
        values.push(root.val)
        if(root.right) dfs(root.right, values)
    }

    // Run dfs and populate array of values
    dfs(root, values)

    return values[k-1]
};
