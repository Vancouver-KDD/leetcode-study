/***************************************************************
 * 🔷 LeetCode 39. Combination Sum
 *
 * 🟡 Difficulty: Medium
 *
 * 📘 Problem:
 *   Given an array of distinct integers candidates and a target integer target,
 *   return a list of all unique combinations of candidates where the chosen numbers
 *   sum to target. You may return the combinations in any order.
 *
 *   The same number may be chosen from candidates an unlimited number of times.
 *   Two combinations are unique if the frequency of at least one of the chosen
 *   numbers is different.
 *
 *   The test cases are generated such that the number of unique combinations that
 *   sum up to target is less than 150 combinations for the given input.
 *
 * 📥 Example 1:
 *   Input:  candidates = [2,3,6,7], target = 7
 *   Output: [[2,2,3], [7]]
 *
 * 📥 Example 2:
 *   Input:  candidates = [2,3,5], target = 8
 *   Output: [[2,2,2,2], [2,3,3], [3,5]]
 *
 * 📥 Example 3:
 *   Input:  candidates = [2], target = 1
 *   Output: []
 *
 * ✅ Constraints:
 *   - 1 <= candidates.length <= 30
 *   - 2 <= candidates[i] <= 40
 *   - All elements of candidates are distinct
 *   - 1 <= target <= 40
 *
 * 🚩 Topics:
 *   Array, Backtracking
 ***************************************************************/

using System.Diagnostics;

namespace Week7_Backtracking_Assign3;

public class CombinationSum_39
{
    private static void Main()
    {
        var instance = new CombinationSum_39();
        int[] candidates = { 2, 3, 6, 7 };
        var target = 7;

        Console.WriteLine("🔹 Combination Sum (Backtracking):");
        MeasureExecutionTime(() =>
        {
            var result = instance.CombinationSum(candidates, target);
            PrintResult(result);
        });
    }

    /// <summary>
    /// Standard backtracking solution to generate all unique combinations.
    /// </summary>
    private IList<IList<int>> CombinationSum(int[] candidates, int target)
    {
        var result = new List<IList<int>>();
        Array.Sort(candidates);

        void Backtrack(int start, int remaining, List<int> current)
        {
            // Base case: found a valid combination
            if (remaining == 0)
            {
                result.Add(new List<int>(current));
                return;
            }

            for (var i = start; i < candidates.Length; i++)
            {
                if (candidates[i] > remaining)
                {
                    break;
                }

                current.Add(candidates[i]); // Choose
                Backtrack(i, remaining - candidates[i], current); // Not i + 1 because we can reuse same element
                current.RemoveAt(current.Count - 1); // Un-choose (backtrack)
            }
        }

        Backtrack(0, target, new List<int>());
        return result;
    }

    /// <summary>
    /// Helper to print 2D list result
    /// </summary>
    private static void PrintResult(IList<IList<int>> result)
    {
        foreach (var combination in result)
        {
            Console.WriteLine($"[{string.Join(", ", combination)}]");
        }

        Console.WriteLine($"\nTotal combinations: {result.Count}\n");
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
 * 🔍 Interview Questions for LeetCode 39 – Combination Sum
 *
 * 1️⃣ What algorithm(s) can be used to solve this?
 *     - Answer: Backtracking (DFS). Dynamic Programming (less common) can also be used in variants.
 *
 * 2️⃣ What is the time and space complexity of your solution?
 *     - Time Complexity: O(2^t), where t is the target value.
 *       - Each number can be picked multiple times, so the decision tree can grow exponentially.
 *     - Space Complexity: O(t) for the recursion stack and O(k) per combination stored in the result.
 *
 * 3️⃣ Why is backtracking a good choice for this problem?
 *     - Answer: It allows exploring all combinations while pruning invalid paths early when the sum exceeds the target.
 *
 * 4️⃣ How do you allow the same number to be reused multiple times?
 *     - Answer: By **not incrementing** the index after choosing a number. This allows the same number to be picked again.
 *
 * 5️⃣ How do you avoid duplicate combinations?
 *     - Answer: By ensuring the recursive function only considers candidates at or after the current index.
 *       - This avoids using the same set in different orders (e.g., [2,2,3] vs [3,2,2]).
 *
 * 6️⃣ Can this problem be solved iteratively?
 *     - Answer: Not easily. Iterative solutions are uncommon due to complexity in tracking path state and pruning.
 *
 * 7️⃣ What constraints make this problem feasible?
 *     - Answer: The number of candidates is at most 30 and the target is ≤ 40, so the number of valid combinations
 *       is small (guaranteed < 150), making recursive backtracking practical.
 ***************************************************************/