/***************************************************************
 * 🔷 LeetCode 215. Kth Largest Element in an Array
 *
 * 🟡 Difficulty: Medium
 *
 * 📘 Problem:
 *   Given an integer array `nums` and an integer `k`, return the kᵗʰ largest
 *   element in the array.
 *
 *   Note: It's the kᵗʰ **largest** element in **sorted order**, not the kᵗʰ distinct element.
 *
 *   Your solution should aim for better performance than fully sorting the array.
 *
 * 📥 Example 1:
 *   Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
 *   Output: 5
 *
 * 📥 Example 2:
 *   Input:  nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
 *   Output: 4
 *
 * ✅ Constraints:
 *   - 1 <= k <= nums.length <= 10⁵
 *   - -10⁴ <= nums[i] <= 10⁴
 *
 * 🚩 Topics:
 *   Array, Heap (Priority Queue), Divide and Conquer, Quickselect
 ***************************************************************/

using System.Diagnostics;

namespace Week8_HeapPriorityQueue_Assign1;

public class KthLargestElementinanArray_215
{
    private static void Main()
    {
        var solution = new KthLargestElementinanArray_215();

        // --- Example 1 ---
        int[] nums1 = { 3, 2, 1, 5, 6, 4 };
        const int k1 = 2;
        Console.WriteLine($"Example 1: Find the {k1}nd largest element in [{string.Join(", ", nums1)}]");
        Console.WriteLine(new string('-', 50));

        Console.WriteLine("🔸 Using Min Heap (Priority Queue):");
        MeasureExecutionTime(() =>
        {
            var result = solution.FindKthLargest_MinHeap(nums1, k1);
            Console.WriteLine($"Result: {result}");
        });

        Console.WriteLine("🔸 Using Quick Select:");
        MeasureExecutionTime(() =>
        {
            // QuickSelect modifies the array, so we pass a clone for a fair comparison.
            var result = solution.FindKthLargest_QuickSelect((int[])nums1.Clone(), k1);
            Console.WriteLine($"Result: {result}");
        });

        Console.WriteLine("\n" + new string('=', 60) + "\n");

        // --- Example 2 ---
        int[] nums2 = { 3, 2, 3, 1, 2, 4, 5, 5, 6 };
        const int k2 = 4;
        Console.WriteLine($"Example 2: Find the {k2}th largest element in [{string.Join(", ", nums2)}]");
        Console.WriteLine(new string('-', 50));

        Console.WriteLine("🔸 Using Min Heap (Priority Queue):");
        MeasureExecutionTime(() =>
        {
            var result = solution.FindKthLargest_MinHeap(nums2, k2);
            Console.WriteLine($"Result: {result}");
        });

        Console.WriteLine("🔸 Using Quick Select:");
        MeasureExecutionTime(() =>
        {
            var result = solution.FindKthLargest_QuickSelect((int[])nums2.Clone(), k2);
            Console.WriteLine($"Result: {result}");
        });
    }

    /// <summary>
    /// Finds the kth largest element using a Min-Heap (Priority Queue).
    /// This approach maintains a heap of size 'k' to keep track of the 'k' largest elements seen so far.
    /// Time Complexity: O(N log k), where N is the number of elements in nums.
    /// Space Complexity: O(k) to store the elements in the heap.
    /// </summary>
    /// <param name="nums">The input array of numbers.</param>
    /// <param name="k">The 'k' value.</param>
    /// <returns>The kth largest element.</returns>
    private int FindKthLargest_MinHeap(int[] nums, int k)
    {
        // A Min-Heap will always have the smallest of its elements at the top.
        var minHeap = new PriorityQueue<int, int>();

        foreach (var num in nums)
        {
            // Add the current number to the heap.
            minHeap.Enqueue(num, num);

            // If the heap size exceeds k, it means we have more than k "largest" elements.
            // We remove the smallest element from the heap (the root of the min-heap)
            // to maintain exactly k elements.
            if (minHeap.Count > k)
            {
                minHeap.Dequeue();
            }
        }

        // After iterating through all numbers, the heap contains the k largest elements of the array.
        // The root of the min-heap is the smallest among these k elements, which is the kth largest element overall.
        return minHeap.Peek();
    }

    /// <summary>
    /// Finds the kth largest element using the Quickselect algorithm.
    /// This is the entry point that converts the problem of finding the "kth largest"
    /// to finding the "(N-k)th smallest" element, which is what Quickselect typically finds.
    /// Time Complexity: Average O(N), Worst Case O(N^2).
    /// Space Complexity: O(log N) for the recursion stack.
    /// </summary>
    /// <param name="nums">The input array of numbers (will be modified in-place).</param>
    /// <param name="k">The 'k' value.</param>
    /// <returns>The kth largest element.</returns>
    private int FindKthLargest_QuickSelect(int[] nums, int k)
    {
        // The kth largest element is at index (nums.Length - k) in a sorted array.
        // For example, in [1,2,3,4,5,6], the 2nd largest (5) is at index 6 - 2 = 4.
        var targetIndex = nums.Length - k;
        return QuickSelect(nums, 0, nums.Length - 1, targetIndex);
    }

    /// <summary>
    /// A recursive helper method that implements the Quickselect algorithm.
    /// It partitions the array and recursively searches in the half that contains the target index.
    /// </summary>
    /// <param name="nums">The array to search within.</param>
    /// <param name="left">The starting index of the subarray.</param>
    /// <param name="right">The ending index of the subarray.</param>
    /// <param name="kSmallest">The target index (of the kth smallest element) we are looking for.</param>
    /// <returns>The element at the kSmallest index.</returns>
    private int QuickSelect(int[] nums, int left, int right, int kSmallest)
    {
        // Base case: if the subarray has only one element, it must be the one we're looking for.
        if (left == right)
        {
            return nums[left];
        }

        // Partition the array and get the final index of the pivot element.
        var pivotIndex = Partition(nums, left, right);

        // If the pivot is at our target index, we've found the element.
        if (pivotIndex == kSmallest)
        {
            return nums[pivotIndex];
        }

        // If the pivot index is smaller than our target, the element must be in the right partition.
        if (pivotIndex < kSmallest)
        {
            return QuickSelect(nums, pivotIndex + 1, right, kSmallest);
        }

        // Otherwise, the element must be in the left partition.
        return QuickSelect(nums, left, pivotIndex - 1, kSmallest);
    }

    /// <summary>
    /// Partitions a subarray using the last element as the pivot (Lomuto partition scheme).
    /// It rearranges the array such that all elements smaller than or equal to the pivot
    /// are on its left, and all elements greater are on its right.
    /// </summary>
    /// <param name="nums">The array to partition.</param>
    /// <param name="left">The starting index of the subarray.</param>
    /// <param name="right">The ending index of the subarray (and the pivot's initial index).</param>
    /// <returns>The final index of the pivot element after partitioning.</returns>
    private int Partition(int[] nums, int left, int right)
    {
        // Choose the rightmost element as the pivot.
        var pivot = nums[right];
        // 'i' is the pointer for the end of the "smaller than pivot" section.
        var i = left;

        // Iterate through the array from left to right-1.
        for (var j = left; j < right; j++)
        {
            // If the current element is less than or equal to the pivot...
            if (nums[j] <= pivot)
            {
                // ...swap it with the element at pointer 'i' and advance 'i'.
                (nums[i], nums[j]) = (nums[j], nums[i]);
                i++;
            }
        }

        // Finally, swap the pivot (originally at nums[right]) with the element at 'i'.
        // This places the pivot in its correct sorted position.
        (nums[i], nums[right]) = (nums[right], nums[i]);
        return i; // Return the pivot's final index.
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
 * 🔍 Interview Questions for LeetCode 215 – Kth Largest Element in an Array
 *
 * 1️⃣ What is the goal of this problem?
 *     - Answer: To find the kᵗʰ largest element in an unsorted array efficiently.
 *
 * 2️⃣ What algorithms can be used to solve this problem?
 *     - Answer: Min Heap (Priority Queue) and Quickselect (a variant of Quicksort).
 *
 * 3️⃣ What is the time and space complexity of each approach?
 *     - Min Heap:
 *         - Time Complexity: O(N log k)
 *         - Space Complexity: O(k)
 *     - Quickselect:
 *         - Time Complexity: O(N) average, O(N²) worst case
 *         - Space Complexity: O(1) extra space (in-place), O(log N) for recursion
 *
 * 4️⃣ Why is a Min Heap a good solution?
 *     - Answer: It maintains the k largest elements seen so far in a heap of size k.
 *       This guarantees that the smallest of those (the root) is the kᵗʰ largest element.
 *
 * 5️⃣ Why is Quickselect efficient for this problem?
 *     - Answer: It avoids full sorting and instead uses partitioning to focus on the kᵗʰ element directly,
 *       achieving linear average time.
 *
 * 6️⃣ When should you use Quickselect over a Heap?
 *     - Answer: Use Quickselect for best average-case time when input size is large and you don't need to maintain a stream.
 *       Use a heap if you want good worst-case behavior or if the input comes as a stream.
 *
 * 7️⃣ What data structures are used in each method?
 *     - Min Heap: PriorityQueue in C#
 *     - Quickselect: Array and in-place swaps using partitioning
 *
 * 8️⃣ How do you convert kth largest into a kth smallest problem?
 *     - Answer: The kth largest element in an array of length N is at index (N - k) when sorted in ascending order.
 *
 * 9️⃣ What are the edge cases to consider?
 *     - Answer: Arrays with duplicate values, arrays where k = 1 or k = nums.Length,
 *       and arrays with negative numbers.
 *
 ***************************************************************/