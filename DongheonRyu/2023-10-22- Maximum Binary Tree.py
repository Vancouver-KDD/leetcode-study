def constructMaximumBinaryTree(nums):
    if not nums:
        return None
    
    # Find the index of the maximum value in the array
    max_val = max(nums)
    max_index = nums.index(max_val)
    
    # Create the root node with the maximum value
    root = TreeNode(max_val)
    
    # Recursively build the left subtree with the subarray to the left of the maximum value
    root.left = constructMaximumBinaryTree(nums[:max_index])
    
    # Recursively build the right subtree with the subarray to the right of the maximum value
    root.right = constructMaximumBinaryTree(nums[max_index + 1:])
    
    return root