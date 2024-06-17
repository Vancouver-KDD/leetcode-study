function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
    if (preorder.length === 0) return null

    const rootVal = preorder[0]
    const inorderIndex = inorder.indexOf(rootVal)

    const leftInorder = inorder.slice(0, inorderIndex)
    const rightInorder = inorder.slice(inorderIndex + 1)

    const leftPreorder = preorder.slice(1, 1 + leftInorder.length)
    const rightPreorder = preorder.slice(1 + leftInorder.length)

    const left = buildTree(leftPreorder, leftInorder)
    const right = buildTree(rightPreorder, rightInorder)

    return new TreeNode(rootVal, left, right)
}
