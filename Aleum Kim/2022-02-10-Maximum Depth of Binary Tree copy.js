/**
 * https://leetcode.com/problems/maximum-depth-of-binary-tree/
 * TIme O(N) | Space O(N)
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    // 1 + Math(1,2) =
    if(root === null)
       return 0;
       return Math.max(maxDepth(root.left)+1, maxDepth(root.right)+1)
};

const maxDepth = (root) => {
    let maxDepth = 0;
    
    let BFS = (node, level) => {
        if(node===null) return

        if(level > maxDepth) maxDepth = level;
        BFS(node.left, level+1)
        BFS(node.right, level+1)
    }
    BFS(root, 1)
    return maxDepth
}

/**
 * https://leetcode.com/problems/maximum-depth-of-binary-tree/
 * TIme O(N) | Space O(N)
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    const isBaseCase = root === null;
    if (isBaseCase) return 0;

    return bfs([[ root, 0 ]]);
}

const bfs = (queue, height = 0) => {
    while (queue.length) {
        for (let i = (queue.length - 1); 0 <= i; i--) {
            const [ root, depth ] = queue.shift();

            height = Math.max(height, (depth + 1));

            if (root.left) queue.push([ root.left, (depth + 1) ]);
            if (root.right) queue.push([  root.right, (depth + 1) ]);
        }
    }

    return height;
}
