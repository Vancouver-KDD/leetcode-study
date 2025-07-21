/***************************************************************
 * 🔷 LeetCode 78. Subsets
 *
 * 🟡 Difficulty: Medium
 *
 * 📘 Problem:
 *   Given an integer array `nums` of unique elements, return all possible
 *   subsets (the power set).
 *
 *   The solution set must not contain duplicate subsets.
 *   Return the solution in any order.
 *
 * 📥 Example 1:
 *   Input:  nums = [1,2,3]
 *   Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
 *
 * 📥 Example 2:
 *   Input:  nums = [0]
 *   Output: [[], [0]]
 *
 * ✅ Constraints:
 *   - 1 <= nums.length <= 10
 *   - -10 <= nums[i] <= 10
 *   - All the numbers of `nums` are unique.
 *
 * 🚩 Topics:
 *   Array, Backtracking, Bit Manipulation
 ***************************************************************/

using System.Diagnostics;

namespace Week7_Backtracking_Assign1;

public class Subsets_78
{
    private static void Main()
    {
        var instance = new Subsets_78();

        int[] nums = [1, 2, 3];  // Example input

        Console.WriteLine("🔁 Generating Subsets using Backtracking:");
        MeasureExecutionTime(() =>
        {
            var subsets1 = instance.Subsets_Backtracking(nums);
            PrintSubsets(subsets1);
        });

        Console.WriteLine("🔁 Generating Subsets using Bit Manipulation:");
        MeasureExecutionTime(() =>
        {
            var subsets2 = instance.Subsets_BitManipulation(nums);
            PrintSubsets(subsets2);
        });
    }
    
    /// <summary>
    /// Utility method to print list of subsets
    /// </summary>
    private static void PrintSubsets(IList<IList<int>> subsets)
    {
        foreach (var subset in subsets)
        {
            Console.Write("[");
            Console.Write(string.Join(",", subset));
            Console.WriteLine("]");
        }

        Console.WriteLine($"\nTotal subsets: {subsets.Count}\n");
    }

    private IList<IList<int>> Subsets_Backtracking(int[] nums)
    {
        var result = new List<IList<int>>();
        Backtrack(0, new List<int>());
        return result;
        
        // Helper Method
        void Backtrack(int start, List<int> current)
        {
            // Add a copy of current subset
            result.Add(new List<int>(current)); 

            // Explore further subsets
            for (var i = start; i < nums.Length; i++)
            {
                current.Add(nums[i]);                        // Include nums[i]
                Backtrack(i + 1, current);              // Recurse with next index
                current.RemoveAt(current.Count - 1);    // Backtrack
            }
        }
    }

    private List<IList<int>> Subsets_BitManipulation(int[] nums)
    {
        var result = new List<IList<int>>();
        var n = nums.Length;
        var total = 1 << n;     // 2^n

        for (var i = 0; i < total; i++)
        {
            var subset = new List<int>();
            for (var j = 0; j < n; j++)
            {
                if ((i & (1 << j)) != 0)
                {
                    subset.Add(nums[j]);
                }
            }
            result.Add(subset);
        }

        return result;
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
 * 🔍 Interview Questions for LeetCode 78 – Subsets
 *
 * 1️⃣ What is the goal of this problem?
 *     - Answer: To generate all possible subsets (also known as the power set) of a given array of unique integers.
 *
 * 2️⃣ What algorithm(s) can be used to solve this?
 *     - Answer: Backtracking (DFS-style recursion) and Bit Manipulation.
 *
 * 3️⃣ What is the time and space complexity of your solution?
 *     - Time Complexity: O(2^n * n), where n is the length of the input array.
 *     - Space Complexity: O(2^n * n), to store all subsets in memory.
 *
 * 4️⃣ Why is backtracking a good choice for this problem?
 *     - Answer: It allows us to build subsets incrementally and explore all inclusion/exclusion combinations in a natural, recursive way.
 *
 * 5️⃣ How does bit manipulation work in this context?
 *     - Answer: Each subset can be represented by a binary number of n bits, where each bit indicates whether the corresponding element is included.
 *
 * 6️⃣ Which method is easier to implement and understand in an interview?
 *     - Answer: Backtracking is typically easier to understand and explain. It's also more intuitive for recursive problem solvers.
 *
 * 7️⃣ Can this problem be solved iteratively?
 *     - Answer: Yes, you can build subsets iteratively by starting with the empty subset and adding each number to existing subsets.
 *
 * 8️⃣ What constraints make this problem manageable?
 *     - Answer: The input array has at most 10 elements, so the total number of subsets (2^10 = 1024) is small enough to generate all.
 ***************************************************************/