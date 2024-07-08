var zigzagLevelOrder = function (root) {
    if (root === null) return [];
    let result = [];
    let q = [[root, true, 0]]

    while (q.length) {
        const [node, flip, level] = q.shift();
        if (!node) continue;
        if (!result[level]) result[level] = [];
        if (!flip) result[level].push(node.val);
        else result[level].unshift(node.val)
        q.push([node.right, !flip, level + 1]);
        q.push([node.left, !flip, level + 1]);
    }

    return result;
};
