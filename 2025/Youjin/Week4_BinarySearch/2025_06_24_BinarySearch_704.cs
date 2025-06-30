/***************************************************************
 * 🔷 LeetCode 704. Binary Search
 *
 * 🟢 Difficulty: Easy
 *
 * 📘 Problem:
 *   Given an array of integers nums which is sorted in ascending order, and an integer target, 
 * 	 write a function to search target in nums. 
 *	 If target exists, then return its index. Otherwise, return -1.
 *
 *   You must write an algorithm with O(log n) runtime complexity.
 *
 * 📥 Example 1:
 *   Input:  nums = [-1,0,3,5,9,12], target = 9
 *   Output: 4
 *   Explanation: 9 exists in nums and its index is 4
 *
 * 📥 Example 2:
 *   Input:  nums = [-1,0,3,5,9,12], target = 2
 *   Output: -1
 *   Explanation: 2 does not exist in nums so return -1
 *
 * ✅ Constraints:
 *   - 1 <= nums.length <= 10⁴
 *   - -10⁴ < nums[i], target < 10⁴
 *   - All the integers in nums are unique.
 *   - nums is sorted in ascending order.
 *
 * 🚩 Topics:
 *   Array, Binary Search
 ***************************************************************/

using System.Diagnostics;

namespace Week4_BinarySearch_Assign1;

public class BinarySearch_704
{
    static void Main(string[] args)
    {
        int[] nums = [-1, 0, 3, 5, 9, 12];
        
        Console.WriteLine("[LinearSearch]");
        MeasureExecutionTime(() =>
        {
            var result1 = LinearSearch(nums, 9);
            Console.WriteLine(string.Join(", ", result1));
        });

        MeasureExecutionTime(() =>
        {
            var result2 = LinearSearch(nums, 2);
            Console.WriteLine(string.Join(", ", result2));
        });
        
        Console.WriteLine("[BinarySearch]");
        MeasureExecutionTime(() =>
        {
            var result3 = BinarySearch(nums, 9);
            Console.WriteLine(string.Join(", ", result3));
        });

        MeasureExecutionTime(() =>
        {
            var result4 = BinarySearch(nums, 2);
            Console.WriteLine(string.Join(", ", result4));
        });
    }

    private static int BinarySearch(int[] nums, int target)
    {
        var left = 0; // Set the initial left boundary of the search range
        var right = nums.Length - 1; // Set the initial right boundary

        while (left <= right) // Continue searching while the range is valid
        {
            // Calculate the middle index to avoid potential overflow
            var mid = left + (right - left) / 2;
            
            if (nums[mid] == target)
            {
                return mid; // Target found at the mid index
            }

            if (nums[mid] < target)
            {
                left = mid + 1; // Target is in the right half, move left pointer
            }
            else
            {
                right = mid - 1; // Target is in the left half, move right pointer
            }
        }

        return -1; // Target not found in the array
    }

    private static int LinearSearch(int[] nums, int target) 
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
 * 🔎 Interview Questions for LeetCode 704. Binary Search
 *
 * 1️⃣ What is the time and space complexity for linear vs. binary search?
 *     🔸 Linear Search:
 *         → Time: O(n) — We may need to scan the entire array.
 *         → Space: O(1) — No extra space is used.
 *
 *     🔹 Binary Search (used in optimal solution):
 *         → Time: O(log n) — We cut the search space in half each time.
 *         → Space: O(1) — Iterative version uses constant space.
 *
 *     ✅ Binary search is much faster on sorted arrays, especially large ones.
 *
 * 2️⃣ Why use binary search?
 *     → Because the input array is sorted, we can eliminate half the search space
 *       at each step, which greatly reduces time complexity.
 *
 * 3️⃣ What if the array is not sorted?
 *     → Binary search won’t work reliably. You would need to use linear search
 *       or sort the array first (which costs O(n log n)).
 *
 * 4️⃣ What edge cases should be considered?
 *     → Empty array, single-element array, target not present,
 *       target at the first or last position.
 *
 * 5️⃣ Can recursion be used instead of iteration?
 *     → Yes, but recursion adds extra space due to the call stack (O(log n)).
 *       Iterative binary search is preferred for space efficiency.
 ***************************************************************/