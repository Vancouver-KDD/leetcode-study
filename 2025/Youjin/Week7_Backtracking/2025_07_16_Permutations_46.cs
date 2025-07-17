/***************************************************************
 * 🔷 LeetCode 46. Permutations
 *
 * 🟡 Difficulty: Medium
 *
 * 📘 Problem:
 *   Given an array `nums` of distinct integers, return all possible
 *   permutations. You can return the answer in any order.
 *
 * 📥 Example 1:
 *   Input:  nums = [1,2,3]
 *   Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 *
 * 📥 Example 2:
 *   Input:  nums = [0,1]
 *   Output: [[0,1],[1,0]]
 *
 * 📥 Example 3:
 *   Input:  nums = [1]
 *   Output: [[1]]
 *
 * ✅ Constraints:
 *   - 1 <= nums.length <= 6
 *   - -10 <= nums[i] <= 10
 *   - All the integers of `nums` are unique.
 *
 * 🚩 Topics:
 *   Array, Backtracking
 ***************************************************************/

using System.Diagnostics;

namespace Week7_Backtracking_Assign2;

public class Subsets_78
{
    private static void Main()
    {
        var instance = new Subsets_78();

        int[] nums = { 1, 2, 3 };

        Console.WriteLine("🔹 Permutations using Backtracking + visited[]:\n");
        MeasureExecutionTime(() =>
        {
            var result = instance.Permute_Backtracking(nums);
            PrintResult(result);
        });

        Console.WriteLine("🔹 Permutations using In-place Swapping:\n");
        MeasureExecutionTime(() =>
        {
            var result = instance.Permute_Swapping(nums);
            PrintResult(result);
        });
    }

    /// <summary>
    /// Utility method to print list of subsets
    /// </summary>
    private static void PrintResult(IList<IList<int>> result)
    {
        foreach (var permutation in result)
        {
            Console.WriteLine($"[{string.Join(", ", permutation)}]");
        }
        Console.WriteLine($"\nTotal permutations: {result.Count}\n");
    }
    
    private IList<IList<int>> Permute_Backtracking(int[] nums)
    {
        var result = new List<IList<int>>();
        var used = new bool[nums.Length]; // Tracks which elements are used in the current path

        void Backtrack(List<int> current)
        {
            // If current permutation is complete, add a copy to result
            if (current.Count == nums.Length)
            {
                result.Add(new List<int>(current));
                return;
            }

            // Explore unused elements
            for (var i = 0; i < nums.Length; i++)
            {
                if (used[i]) continue; // Skip if already used

                // Choose
                used[i] = true;
                current.Add(nums[i]);

                // Explore
                Backtrack(current);

                // Un-choose (backtrack)
                current.RemoveAt(current.Count - 1);
                used[i] = false;
            }
        }

        Backtrack(new List<int>());
        return result;
    }

    private IList<IList<int>> Permute_Swapping(int[] nums)
    {
        var result = new List<IList<int>>();

        void Backtrack(int start)
        {
            // Base case: all elements fixed, add a copy of current permutation
            if (start == nums.Length)
            {
                result.Add(new List<int>(nums));
                return;
            }

            // Iterate through possible swaps
            for (var i = start; i < nums.Length; i++)
            {
                // Swap current index with i
                (nums[start], nums[i]) = (nums[i], nums[start]);

                // Recurse for the next index
                Backtrack(start + 1);

                // Backtrack: swap back
                (nums[start], nums[i]) = (nums[i], nums[start]);
            }
        }

        Backtrack(0);
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
 * 🔍 Interview Questions for LeetCode 46 – Permutations
 *
 * 1️⃣ What algorithm(s) can be used to solve this?
 *     - Answer: Backtracking (with used[] array) and Swap-based in-place backtracking.
 *
 * 2️⃣ What is the time and space complexity of your solution?
 *     - Time Complexity: O(n × n!), where n is the length of the input array.
 *     - Space Complexity: O(n) for recursion stack, plus O(n!) for storing results.
 *
 * 3️⃣ Why is backtracking a good choice for this problem?
 *     - Answer: It allows building up permutations step-by-step and efficiently pruning paths with already used elements.
 *
 * 4️⃣ How does the swap-based approach work?
 *     - Answer: It recursively fixes one element at a time by swapping it with all possible candidates ahead,
 *       and backtracks by swapping back to preserve the original array.
 *
 * 5️⃣ Which is more efficient: backtracking with used[] or swapping?
 *     - Answer:
 *         • Swap-based is more memory efficient (in-place).
 *         • used[] version is more intuitive and avoids modifying the input.
 *         ✅ Use whichever fits the interview style or project requirement best.
 *
 * 6️⃣ Can this problem be solved iteratively?
 *     - Answer: It’s complex to implement iteratively and not commonly done. Recursive backtracking is the standard approach.
 *
 * 7️⃣ What constraints make this problem feasible?
 *     - Answer: The input length is small (n ≤ 6), so generating all n! permutations (max 720) is computationally reasonable.
 ***************************************************************/