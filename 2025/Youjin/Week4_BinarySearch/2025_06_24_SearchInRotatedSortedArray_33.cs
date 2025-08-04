/***************************************************************
 * 🔷 LeetCode 33. Search in Rotated Sorted Array
 *
 * 🟡 Difficulty: Medium
 *
 * 📘 Problem:
 *   There is an integer array nums sorted in ascending order (with distinct values).
 *
 *   Prior to being passed to your function,
 *   nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
 *   such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
 *   For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
 *
 *   You must implement the search with O(log n) time complexity.
 *
 * 📌 Rotation Example:
 *   Original: [0,1,2,4,5,6,7]
 *   Rotated : [4,5,6,7,0,1,2]  ← rotated at index 3
 *
 * 📥 Example 1:
 *   Input:  nums = [4,5,6,7,0,1,2], target = 0
 *   Output: 4
 *
 * 📥 Example 2:
 *   Input:  nums = [4,5,6,7,0,1,2], target = 3
 *   Output: -1
 *
 * 📥 Example 3:
 *   Input:  nums = [1], target = 0
 *   Output: -1
 *
 * ✅ Constraints:
 *   - 1 <= nums.length <= 5000
 *   - -10⁴ <= nums[i], target <= 10⁴
 *   - All elements are unique
 *   - nums is sorted in ascending order and possibly rotated
 *
 * 🚩 Topics:
 *   Array, Binary Search
 ***************************************************************/

using System.Diagnostics;

namespace Week4_BinarySearch_Assign2;

public class SearchInRotatedSortedArray_33
{
    static void Main(string[] args)
    {
        int[] numsCase1 = [4, 5, 6, 7, 0, 1, 2];
        int[] numsCase2 = [1];
        
        Console.WriteLine("[LinearSearch]");
        MeasureExecutionTime(() =>
        {
            var result1 = Search(numsCase1, 0);
            Console.WriteLine(result1);
        });
        
        Console.WriteLine("[BinarySearch]");
        MeasureExecutionTime(() =>
        {
            var result2 = BinarySearch(numsCase1, 0);
            Console.WriteLine(result2);
        });
        
        var result3 = Search(numsCase2, 0);
        Console.WriteLine(result3);
    }
    
    private static int BinarySearch(int[] nums, int target)
    {
        var left = 0;
        var right = nums.Length - 1;

        while (left <= right)
        {
            var mid = left + (right - left) / 2;

            if (nums[mid] == target)
            {
                return mid;
            }

            // Left half is sorted?
            if (nums[left] <= nums[mid])
            {
                if (nums[left] <= target && target < nums[mid])
                {
                    right = mid - 1; // the target is in the left half
                }
                else
                {
                    left = mid + 1; // the target is in the right half
                }
            }
            // Right half is sorted?
            else
            {
                if (nums[mid] < target && target <= nums[right])
                {
                    left = mid + 1; // the target is in the right half
                }
                else
                {
                    right = mid - 1; // the target is in the left half
                }
            }
        }

        return -1; // Not found
    }
    
    private static int Search(int[] nums, int target)
    {
        for (var i = 0; i < nums.Length; i++)
        {
            if (nums[i] == target)
            {
                return i;
            }
        }
        
        return -1;
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
 * 🔎 Interview Questions for LeetCode 33. Search in Rotated Sorted Array
 *
 * 1️⃣ What is the time and space complexity?
 *     🔸 Naive Linear Search:
 *         → Time: O(n) — We may need to check each element one by one.
 *         → Space: O(1) — No extra space required.
 *
 *     🔹 Optimized Binary Search (in rotated array):
 *         → Time: O(log n) — We still eliminate half the search space at each step.
 *         → Space: O(1) — Iterative approach, no extra memory.
 *
 *     ✅ Binary search works efficiently even with rotation if we locate the sorted half.
 *
 * 2️⃣ How does binary search work in a rotated sorted array?
 *     → At each step, at least one half of the array is sorted.
 *       We check which half is sorted and if the target lies within it,
 *       then narrow our search accordingly.
 *
 * 3️⃣ Why can’t we use the standard binary search directly?
 *     → Because the array is not completely sorted.
 *       Due to rotation, the normal binary search assumptions no longer hold.
 *
 * 4️⃣ What edge cases should be considered?
 *     → Target not found, rotation at 0 (i.e., not rotated),
 *       small arrays (length 1 or 2), target at start or end,
 *       fully rotated array (like original order).
 *
 * 5️⃣ Can recursion be used instead of iteration?
 *     → Yes, binary search logic can be implemented recursively,
 *       but iterative version is preferred due to constant space usage.
 *
 * 6️⃣ Can this approach handle duplicates?
 *     → No. With duplicates, we cannot guarantee which half is sorted.
 *       We'd need to modify the algorithm (e.g., skip duplicates at boundaries).
 ***************************************************************/