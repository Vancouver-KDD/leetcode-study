var invertTree = function(root) {

    const reverseNodes = (node) => {
        if(node == null) {
            return;
        }
        reverseNodes(node.left);
        reverseNodes(node.right);
        
        let hold = node.left;
        node.left = node.right;
        node.right = hold
    }
    reverseNodes(root)
       return root;
}
// TIme O(N) | Space O(n)

/**
 * https://leetcode.com/problems/invert-binary-tree/
 * TIme O(N) | Space O(W)
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = (root,) => {
    const isBaseCase = root === null;
    if (isBaseCase) return root;

    bfs([ root ]);

    return root;
}

const bfs = (queue) => {
    while (queue.length) {
        for (let i = (queue.length - 1); 0 <= i; i--) {
            const node = queue.shift();
            const left = node.right;
            const right = node.left;

            node.left = left;
            node.right = right;

            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
    }
}
