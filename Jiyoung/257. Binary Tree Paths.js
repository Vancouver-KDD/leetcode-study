let result = [];

var checkPath = function (node, path) {
    if (!node) return;
    path.push(node.val);

    if (!node.left && !node.right) {
        result.push(path.join("->"));
    } else {
        checkPath(node.left, [...path]);
        checkPath(node.right, [...path]);
    }
}

var binaryTreePaths = function (root) {
    result = [];
    checkPath(root, []);
    return result;
};
