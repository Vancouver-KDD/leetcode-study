/***************************************************************
 * 🔷 LeetCode 23. Merge k Sorted Lists
 *
 * 🔴 Difficulty: Hard
 *
 * 📘 Problem:
 *   You are given an array of `k` linked lists. Each linked list is sorted in ascending order.
 *   Merge all `k` linked lists into one sorted linked list and return it.
 *
 * 📥 Example 1:
 *   Input:  lists = [[1,4,5],[1,3,4],[2,6]]
 *   Output: [1,1,2,3,4,4,5,6]
 *   Explanation:
 *     Input lists:
 *     [
 *       1→4→5,
 *       1→3→4,
 *       2→6
 *     ]
 *     Merged result:
 *     1→1→2→3→4→4→5→6
 *
 * 📥 Example 2:
 *   Input:  lists = []
 *   Output: []
 *
 * 📥 Example 3:
 *   Input:  lists = [[]]
 *   Output: []
 *
 * ✅ Constraints:
 *   - k == lists.length
 *   - 0 <= k <= 10⁴
 *   - 0 <= lists[i].length <= 500
 *   - -10⁴ <= lists[i][j] <= 10⁴
 *   - All lists[i] are sorted in ascending order
 *   - The total number of nodes across all lists ≤ 10⁴
 *
 * 🚩 Topics:
 *   Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
 ***************************************************************/

using System.Diagnostics;
using System.Text;

namespace Week8_HeapPriorityQueue_Assign3;

public class MergekSortedLists_23
{
    public class ListNode
    {
        public int val;
        public ListNode next;

        public ListNode(int val = 0, ListNode next = null)
        {
            this.val = val;
            this.next = next;
        }
    }
    
    private static void Main()
    {
        var solution = new MergekSortedLists_23();

        // --- Helper functions for testing ---
        ListNode CreateList(int[] values)
        {
            if (values == null || values.Length == 0)
            {
                return null;
            }
            var dummy = new ListNode();
            var current = dummy;
            foreach (var val in values)
            {
                current.next = new ListNode(val);
                current = current.next;
            }
            return dummy.next;
        }

        void PrintList(ListNode head)
        {
            if (head == null)
            {
                Console.WriteLine("[]");
                return;
            }
            var sb = new StringBuilder("[");
            var current = head;
            while (current != null)
            {
                sb.Append(current.val);
                if (current.next != null) sb.Append(", ");
                current = current.next;
            }
            sb.Append("]");
            Console.WriteLine(sb.ToString());
        }

        // --- Example 1 ---
        Console.WriteLine("--- Example 1 ---");
        var lists1 = new[]
        {
            CreateList([1, 4, 5]),
            CreateList([1, 3, 4]),
            CreateList([2, 6])
        };
        Console.WriteLine("Input lists:");
        Array.ForEach(lists1, PrintList);
        MeasureExecutionTime(() =>
        {
            var result = solution.MergeKLists(lists1);
            Console.Write("Merged Result: ");
            PrintList(result); // Expected: [1, 1, 2, 3, 4, 4, 5, 6]
        });

        // --- Example 2 ---
        Console.WriteLine("\n--- Example 2 ---");
        var lists2 = Array.Empty<ListNode>();
        Console.WriteLine("Input lists: []");
        MeasureExecutionTime(() =>
        {
            var result = solution.MergeKLists(lists2);
            Console.Write("Merged Result: ");
            PrintList(result); // Expected: []
        });

        // --- Example 3 ---
        Console.WriteLine("\n--- Example 3 ---");
        var lists3 = new[] { CreateList([]) };
        Console.WriteLine("Input lists: [[]]");
        MeasureExecutionTime(() =>
        {
            var result = solution.MergeKLists(lists3);
            Console.Write("Merged Result: ");
            PrintList(result); // Expected: []
        });
    }

    /// <summary>
    /// Merges an array of k sorted linked lists into one single sorted linked list.
    /// This solution uses a Min-Heap (PriorityQueue) to efficiently find the
    /// node with the minimum value across all lists at each step.
    ///
    /// Time Complexity: O(N log k), where N is the total number of nodes in all lists,
    /// and k is the number of lists. The log k factor comes from the heap operations (Enqueue/Dequeue).
    ///
    /// Space Complexity: O(k) for storing at most k nodes in the priority queue.
    /// </summary>
    /// <param name="lists">An array of ListNode, where each is the head of a sorted list.</param>
    /// <returns>The head of the new single sorted linked list.</returns>
    private ListNode MergeKLists(ListNode[] lists)
    {
        // Create a Min-Heap (PriorityQueue) to store list nodes.
        // The priority is based on the node's value, so the node with the smallest
        // value will always be at the top.
        var pq = new PriorityQueue<ListNode, int>();

        // Add the head of each non-empty list to the priority queue to start.
        foreach (var node in lists)
        {
            pq.Enqueue(node, node.val);
        }

        // Create a dummy head node. This is a common technique to simplify
        // the logic of building a new list, as it avoids edge cases for the first node.
        var dummy = new ListNode();
        // 'current' will be our pointer to build the new list.
        var current = dummy;

        // Continue the process as long as there are nodes in the priority queue.
        while (pq.Count > 0)
        {
            // Dequeue the node with the smallest value from the heap.
            // This is the next node in our sorted merged list.
            var minNode = pq.Dequeue();

            // Append this smallest node to our result list.
            current.next = minNode;

            // Advance the 'current' pointer.
            current = current.next;

            // If the node we just added has a 'next' node in its original list,
            // add that next node to the priority queue to be considered for the next step.
            pq.Enqueue(minNode.next, minNode.next.val);
        }

        // The merged list starts right after our dummy node.
        return dummy.next;
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
 * 🔍 Interview Questions for LeetCode 23 – Merge k Sorted Lists
 *
 * 1️⃣ What is the goal of this problem?
 *     - To merge k sorted linked lists into a single sorted linked list.
 *       Each input list is already sorted in ascending order.
 *
 * 2️⃣ What are the two main approaches to solve this?
 *     - Min-Heap (PriorityQueue) based approach.
 *     - Divide and Conquer (Merge Sort style) approach.
 *
 * 3️⃣ What is the time and space complexity of the Min-Heap approach?
 *     - Time: O(N log k), where N is total number of nodes, and k is number of lists.
 *     - Space: O(k) for the heap (stores at most one node per list at any time).
 *
 * 4️⃣ How does the Min-Heap approach work?
 *     - Add the head of each non-empty list to the heap (min-heap by node value).
 *     - Repeatedly extract the smallest node and append it to the result list.
 *     - If the extracted node has a `next`, enqueue that next node into the heap.
 *     - Repeat until the heap is empty.
 *
 * 5️⃣ Why is PriorityQueue appropriate here?
 *     - It allows us to efficiently find and extract the smallest node across k lists in O(log k) time.
 *     - It avoids scanning all k heads every time.
 *
 * 6️⃣ How does the Divide and Conquer approach work?
 *     - Repeatedly merge two lists at a time in a bottom-up fashion.
 *     - This mimics the behavior of merge sort, halving the problem each time.
 *     - Time Complexity: O(N log k), same as the heap approach.
 *
 * 7️⃣ Which approach is better in practice?
 *     - Heap is better when k is large and lists are long.
 *     - Divide-and-conquer may use slightly less space and is easier to implement recursively.
 *
 * 8️⃣ What edge cases should be handled?
 *     - `lists` is empty: return null.
 *     - `lists` contains empty lists: skip them.
 *     - All values are the same: result should still be sorted.
 *
 * 9️⃣ What’s the difference between this and merging two sorted lists?
 *     - Merging two sorted lists is simpler (O(N) time).
 *     - Here, we generalize it to k lists, requiring a more scalable solution (heap or merge sort).
 *
 * 🔟 Is the input modified?
 *     - No. A new merged list is constructed. The original input lists are not altered.
 *
 ***************************************************************/