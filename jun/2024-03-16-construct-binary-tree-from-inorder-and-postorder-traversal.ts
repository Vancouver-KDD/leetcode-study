function buildTree(inorder: number[], postorder: number[]): TreeNode | null {
    if (postorder.length === 0) return null

    const rootVal = postorder[postorder.length - 1]
    const rootIndex = inorder.indexOf(rootVal)

    const leftInorder = inorder.slice(0, rootIndex)
    const rightInorder = inorder.slice(rootIndex + 1)

    const leftPostorder = postorder.slice(0, rootIndex)
    const rightPostorder = postorder.slice(rootIndex, postorder.length - 1)

    const leftSubtree = buildTree(leftInorder, leftPostorder)
    const rightSubtree = buildTree(rightInorder, rightPostorder)

    return new TreeNode(rootVal, leftSubtree, rightSubtree)
}
