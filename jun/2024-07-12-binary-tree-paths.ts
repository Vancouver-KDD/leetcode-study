function binaryTreePaths(root: TreeNode | null): string[] {
    const result: string[] = [];
    function dfs(_root: TreeNode | null, path: string) {
        if(!_root) return;
        path += _root.val;
        if(!_root.left && !_root.right) {
            result.push(path);
            return;
        }
        dfs(_root.left, path + '->' );
        dfs(_root.right, path + '->' );
    }
    dfs(root, '');
    return result;
};