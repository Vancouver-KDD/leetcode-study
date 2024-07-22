let result;
let target;

var checkPath = function (node, path) {
    if (!node) return;
    path.push(node.val);

    if (!node.left && !node.right) {
        if (path.reduce((acc, cur) => acc + cur, 0) === target)
            result.push(path);
    } else {
        checkPath(node.left, [...path]);
        checkPath(node.right, [...path]);
    }
}

var pathSum = function (root, targetSum) {
    result = [];
    target = targetSum;
    checkPath(root, []);

    return result;
};
