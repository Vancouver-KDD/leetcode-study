/***************************************************************
 * 🔷 LeetCode 102. Binary Tree Level Order Traversal
 *
 * 🟡 Difficulty: Medium
 *
 * 📘 Problem:
 *   Given the root of a binary tree, return the level order traversal
 *   of its nodes' values. (i.e., from left to right, level by level).
 *
 * 📥 Example 1:
 *   Input:  root = [3,9,20,null,null,15,7]
 *   Output: [[3],[9,20],[15,7]]
 *
 * 📥 Example 2:
 *   Input:  root = [1]
 *   Output: [[1]]
 *
 * 📥 Example 3:
 *   Input:  root = []
 *   Output: []
 *
 * ✅ Constraints:
 *   - The number of nodes in the tree is in the range [0, 2000].
 *   - -1000 <= Node.val <= 1000
 *
 * 🚩 Topics:
 *   Tree, Breadth-First Search, Binary Tree
 ***************************************************************/

using System.Diagnostics;

namespace Week6_Trees_Assign2;

public class BinaryTreeLevelOrderTraversal_102
{
    private static void Main()
    {
        // Build sample tree: [3,9,20,null,null,15,7]
        var root = new TreeNode(3,
            new TreeNode(9),
            new TreeNode(20, new TreeNode(15), new TreeNode(7)));

        MeasureExecutionTime(() =>
        {
            var traversal = new BinaryTreeLevelOrderTraversal_102().LevelOrder(root);
            foreach (var level in traversal)
            {
                Console.WriteLine($"[{string.Join(",", level)}]");
            }
        });
    }
    
    private IList<IList<int>> LevelOrder(TreeNode root)
    {
        // Initialize the result list to store level-wise node values
        var result = new List<IList<int>>();

        // If the tree is empty, return an empty list
        if (root == null)
        {
            return result;
        }

        // Initialize a queue for BFS traversal
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root); // Start with the root node

        // Traverse the tree level by level
        while (queue.Count > 0)
        {
            var levelSize = queue.Count; // Number of nodes at the current level
            var level = new List<int>(); // List to store the current level's values

            // Process all nodes in the current level
            for (var i = 0; i < levelSize; i++)
            {
                var node = queue.Dequeue(); // Get the next node in the queue
                level.Add(node.val); // Add its value to the current level list

                // Enqueue the left child if it exists
                if (node.left != null)
                {
                    queue.Enqueue(node.left);
                }

                // Enqueue the right child if it exists
                if (node.right != null)
                {
                    queue.Enqueue(node.right);
                }
            }

            // Add the current level's values to the final result
            result.Add(level);
        }

        // Return the list of level order values
        return result;
    }

    /// <summary>
    /// Definition for a binary tree node
    /// </summary>
    public class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;

        public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
        {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    
    private static void MeasureExecutionTime(Action action)
    {
        var stopwatch = Stopwatch.StartNew();
        action();
        stopwatch.Stop();
        Console.WriteLine($"Execution Time: {stopwatch.Elapsed.TotalMilliseconds} ms\n");
    }
}

/***************************************************************
 * 🔷 Interview Questions for LeetCode 102 - Binary Tree Level Order Traversal
 *
 * 1. What traversal technique is used in this problem, and why is it appropriate?
 *    → This problem uses Breadth-First Search (BFS) because it naturally visits nodes level by level,
 * which is exactly what the question asks.
 *
 * 2. How would you implement this traversal without using a queue?
 *    → You could use Depth-First Search (DFS) and pass in the level as a parameter,
 * then manually group values into a list based on the level.
 *
 * 3. What is the time and space complexity of your solution?
 *    → Time Complexity: O(n), because each node is visited once.
 *      Space Complexity: O(n), due to the queue used for traversal and the result list.
 *
 * 4. How would your solution behave if the tree is very deep (e.g., skewed)?
 *    → In the BFS version, queue size may grow linearly with the depth in the worst case (e.g., skewed tree),
 * but it is manageable for level order traversal.
 *
 * 5. Could this problem be solved using a recursive approach?
 *    → Yes, using DFS with level tracking. However, BFS is simpler and more intuitive for level order traversal.
 *
 * 6. Can you explain what happens at each iteration of the while-loop in your BFS approach?
 *    → At each iteration, we process all nodes at the current level (queue size at that moment) and
 * add their values to a level list, then enqueue their children.
 *
 * 7. What would happen if the input tree is null?
 *    → The algorithm should return an empty list immediately.
 *
 * 8. How would you modify your solution to return the values in reverse level order?
 *    → Use a stack to reverse the level order or insert each level at the beginning of the result list.
 *
 ***************************************************************/