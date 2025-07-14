/***************************************************************
 * 🔷 LeetCode 104. Maximum Depth of Binary Tree
 *
 * 🟢 Difficulty: Easy
 *
 * 📘 Problem:
 *   Given the root of a binary tree, return its maximum depth.
 *
 *   A binary tree's maximum depth is the number of nodes along
 *   the longest path from the root node down to the farthest leaf node.
 *
 * 📥 Example 1:
 *   Input:  root = [3,9,20,null,null,15,7]
 *   Output: 3
 *
 * 📥 Example 2:
 *   Input:  root = [1,null,2]
 *   Output: 2
 *
 * ✅ Constraints:
 *   - The number of nodes in the tree is in the range [0, 10⁴].
 *   - -100 <= Node.val <= 100
 *
 * 🚩 Topics:
 *   Tree, Depth-First Search, Breadth-First Search, Binary Tree
 ***************************************************************/

using System.Diagnostics;

namespace Week6_Trees_Assign1;

public class MaximumDepthOfBinaryTree_104
{
    private static void Main()
    {
        var solution = new MaximumDepthOfBinaryTree_104();

        //      3
        //     / \
        //    9  20
        //       / \
        //      15  7
        var root = new TreeNode(3)
        {
            left = new TreeNode(9),
            right = new TreeNode(20, new TreeNode(15), new TreeNode(7))
        };

        Console.WriteLine("Binary Tree Maximum Depth Calculation\n");

        // 1. DFS - Recursive
        Console.WriteLine("--- Recursive DFS Version ---");
        var recursiveDepth = 0;
        MeasureExecutionTime(() => { recursiveDepth = solution.MaxDepth_RecursiveVersion(root); });
        Console.WriteLine($"Maximum Depth: {recursiveDepth}");

        // 2. BFS - Queue
        Console.WriteLine("\n--- Iterative BFS (Queue) Version ---");
        var queueDepth = 0;
        MeasureExecutionTime(() => { queueDepth = solution.MaxDepth_QueueVersion(root); });
        Console.WriteLine($"Maximum Depth: {queueDepth}");
    }

    private int MaxDepth_RecursiveVersion(TreeNode root)
    {
        // Base case: if the node is null, the depth is 0
        if (root == null)
        {
            return 0;
        }

        // Recursively calculate the depth of left and right subtrees
        var leftDepth = MaxDepth_RecursiveVersion(root.left);
        var rightDepth = MaxDepth_RecursiveVersion(root.right);

        // The depth of the current node is 1 (itself) + the max of its subtrees
        return 1 + Math.Max(leftDepth, rightDepth);
    }

    private int MaxDepth_QueueVersion(TreeNode root)
    {
        // If the tree is empty, its depth is 0
        if (root == null)
        {
            return 0;
        }

        // Initialize a queue for level-order traversal
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        var depth = 0;

        // Traverse the tree level by level
        while (queue.Count > 0)
        {
            var levelSize = queue.Count; // Number of nodes at current level

            // Process all nodes at the current level
            for (var i = 0; i < levelSize; i++)
            {
                var current = queue.Dequeue();

                // Add child nodes to the queue for the next level
                if (current.left != null)
                {
                    queue.Enqueue(current.left);
                }

                if (current.right != null)
                {
                    queue.Enqueue(current.right);
                }
            }

            // After processing one level, increase depth by 1
            depth++;
        }

        return depth;
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
 * 🔷 Interview Questions for LeetCode 104. Maximum Depth of Binary Tree
 *
 * 1️⃣ What is the time and space complexity of your solution?
 *     🔸 Recursive DFS:
 *         → Time: O(n) — Every node is visited once.
 *         → Space: O(h) — h is the height of the tree (due to recursion stack).
 *
 *     🔹 Iterative BFS:
 *         → Time: O(n) — Every node is added to and removed from the queue once.
 *         → Space: O(w) — w is the maximum width of the tree (nodes at the widest level).
 *
 * 2️⃣ Why does DFS work well for this problem?
 *     → DFS allows us to go as deep as possible into each branch,
 *       which directly matches the goal of finding the maximum depth.
 *       We compare the depths from the left and right subtrees recursively.
 *
 * 3️⃣ How does the base case in recursion work?
 *     → If the node is null, it means we've gone beyond a leaf,
 *       so we return a depth of 0. This terminates the recursion.
 *
 * 4️⃣ When would BFS be preferred over DFS?
 *     → BFS might be preferred when we want to process nodes level-by-level,
 *       or if we want to avoid recursion due to potential stack overflow in deep trees.
 *
 * 5️⃣ Can you explain the BFS approach?
 *     → We use a queue to perform level-order traversal.
 *       For each level, we count the number of nodes and process them,
 *       incrementing the depth after each level is completed.
 *
 * 6️⃣ What are some edge cases to consider?
 *     → Empty tree (root is null): return 0
 *       Tree with one node: return 1
 *       Left- or right-skewed trees (linked list-shaped)
 *
 *
 * 7️⃣ What is the difference between depth and height of a tree?
 *     → They are often used interchangeably.
 *       In this problem, “maximum depth” refers to the longest path from the root down to any leaf.
 ***************************************************************/
 
/***************************************************************
 * 🔍 1. DFS (Depth-First Search)
 * 
 * 📌 Definition:
 *   - Starts from the root and explores as deep as possible along each branch.
 *   - Backtracks when no further nodes are found in the current path.
 * 
 * 📌 Characteristics:
 *   - Typically implemented using recursion or an explicit stack.
 *   - Traverses left subtree first, then right subtree.
 *   - Suitable for problems like computing max depth, checking paths, etc.
 * 
 * 🧠 Example:
 * int MaxDepth(TreeNode root)
 * {
 *     if (root == null)
 *     {
 *          return 0;
 *     }
 *     int left = MaxDepth(root.left);
 *     int right = MaxDepth(root.right);
 * 
 *     return Math.Max(left, right) + 1;
 * }
 *
 *
 * 🔍 2. BFS (Breadth-First Search)
 * 
 * 📌 Definition:
 *   - Explores all nodes at the current level before moving to the next.
 *   - Traverses the tree level by level from top to bottom.
 * 
 * 📌 Characteristics:
 *   - Implemented using a queue (FIFO).
 *   - Ideal for level-order traversal and shortest path problems.
 * 
 * 🧠 Example:
 * int MaxDepth(TreeNode root)
 * {
 *     if (root == null)
 *     {
 *          return 0;
 *     }
 *     Queue<TreeNode> queue = new Queue<TreeNode>();
 *     queue.Enqueue(root);
 *     int depth = 0;
 * 
 *     while (queue.Count > 0)
 *     {
 *         int size = queue.Count;
 *         for (int i = 0; i < size; i++)
 *         {
 *             TreeNode node = queue.Dequeue();
 *             if (node.left != null)
 *             {
 *                  queue.Enqueue(node.left);
 *             }
 *             if (node.right != null)
 *             {
 *                  queue.Enqueue(node.right);
 *             }
 *         }
 *         depth++;
 *     }
 * 
 *     return depth;
 * }
 *
 *
 * 🎯 Summary:
 * DFS:
 *   → Uses recursion or stack.
 *   → Goes deep first, then backtracks.
 *   → Space Complexity: O(h)
 *   → Time Complexity: O(n)
 * 
 * BFS:
 *   → Uses a queue.
 *   → Processes nodes level by level.
 *   → Space Complexity: O(w)
 *   → Time Complexity: O(n)
 *   (h = height of tree, w = maximum width, n = total nodes)
 ***************************************************************/