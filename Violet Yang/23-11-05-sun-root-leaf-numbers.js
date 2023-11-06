var sumNumbers = function(root) {
    const paths = []
    traversePaths(root, [], paths)
    return paths.reduce((ret, path) => {
        const num = path.reduce((sum, node) => {
            sum = sum * 10 + node.val
            return sum
        }, 0)
        return ret + num
    }, 0)
};

function traversePaths(root, path, paths) {
    if (!root) {
        return
    }
    if (!root.left && !root.right) {
        paths.push([...path, root])
    }
    if (root.left) {
        traversePaths(root.left, [...path, root], paths)
    }
    if (root.right) {
        traversePaths(root.right, [...path, root], paths)
    }
}