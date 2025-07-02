/***************************************************************
 * 🔷 LeetCode 21. Merge Two Sorted Lists
 *
 * 🟢 Difficulty: Easy
 *
 * 📘 Problem:
 *   You are given the heads of two sorted linked lists list1 and list2.
 *   Merge the two lists into one sorted list. The list should be made by
 *   splicing together the nodes of the first two lists.
 *
 *   Return the head of the merged linked list.
 *
 * 📥 Example 1:
 *   Input:  list1 = [1,2,4], list2 = [1,3,4]
 *   Output: [1,1,2,3,4,4]
 *
 * 📥 Example 2:
 *   Input:  list1 = [], list2 = []
 *   Output: []
 *
 * 📥 Example 3:
 *   Input:  list1 = [], list2 = [0]
 *   Output: [0]
 *
 * ✅ Constraints:
 *   - The number of nodes in both lists is in the range [0, 50].
 *   - -100 <= Node.val <= 100
 *   - Both list1 and list2 are sorted in non-decreasing order.
 *
 * 🚩 Topics:
 *   Linked List, Recursion
 ***************************************************************/

using System.Diagnostics;
using System.Text;

namespace Week5_LinkedList_Assign1;

public class MergeTwoSortedLists_21
{
    private static void Main(string[] args)
    {
        var solution = new MergeTwoSortedLists_21();

        // Test Case 1
        var list1 = CreateLinkedList([1, 2, 4]);
        var list2 = CreateLinkedList([1, 3, 4]);

        Console.WriteLine("[Iterative Version]");
        MeasureExecutionTime(() =>
        {
            var mergedList = solution.MergeTwoLists_IterativeVersion(list1, list2);
            Console.WriteLine($"Merged: {PrintLinkedList(mergedList)}"); // Expected: [1, 1, 2, 3, 4, 4]
        });

        // Re-create lists as they were modified by the iterative merge
        list1 = CreateLinkedList([1, 2, 4]);
        list2 = CreateLinkedList([1, 3, 4]);

        Console.WriteLine("[Recursive Version]");
        MeasureExecutionTime(() =>
        {
            var mergedList = solution.MergeTwoLists_RecursiveVersion(list1, list2);
            Console.WriteLine($"Merged: {PrintLinkedList(mergedList)}"); // Expected: [1, 1, 2, 3, 4, 4]
        });

        // Test Case 2: Empty lists
        var list3 = CreateLinkedList([]);
        var list4 = CreateLinkedList([]);
        var merged2 = solution.MergeTwoLists_IterativeVersion(list3, list4);
        Console.WriteLine($"Empty lists merged: {PrintLinkedList(merged2)}"); // Expected: []

        // Test Case 3: One empty list
        var list5 = CreateLinkedList([]);
        var list6 = CreateLinkedList([0]);
        var merged3 = solution.MergeTwoLists_IterativeVersion(list5, list6);
        Console.WriteLine($"One empty list merged: {PrintLinkedList(merged3)}"); // Expected: [0]
    }
    
    private ListNode? MergeTwoLists_RecursiveVersion (ListNode? list1, ListNode? list2) 
    {
        // If one of the lists is null, return the other list
        if (list1 == null)
        {
            return list2;
        }

        if (list2 == null)
        {
            return list1;
        }

        // Compare current nodes and recursively merge the rest
        if (list1.val < list2.val)
        {
            // list1's value is smaller, keep it and merge the rest with list1.next
            list1.next = MergeTwoLists_RecursiveVersion(list1.next, list2);
            return list1;
        }
        else
        {
            // list2's value is smaller or equal, keep it and merge the rest with list2.next
            list2.next = MergeTwoLists_RecursiveVersion(list1, list2.next);
            return list2;
        }
    }
    
    private ListNode? MergeTwoLists_IterativeVersion (ListNode? list1, ListNode? list2)
    {
        // Create a dummy node to simplify list building
        var dummy = new ListNode(-1);
        var current = dummy;

        // Traverse both lists until one becomes null
        while (list1 != null && list2 != null)
        {
            if (list1.val < list2.val)
            {
                // Attach list1 node and move list1 forward
                current.next = list1;
                list1 = list1.next;
            }
            else
            {
                // Attach list2 node and move list2 forward
                current.next = list2;
                list2 = list2.next;
            }
            // Move the current pointer forward
            current = current.next;
        }

        // Attach any remaining nodes (only one list will be non-null)
        current.next = list1 ?? list2;

        // Return the merged list starting from the next node after dummy
        return dummy.next;
    }

    public class ListNode
    {
        public int val;
        public ListNode? next;

        public ListNode(int val = 0, ListNode? next = null)
        {
            this.val = val;
            this.next = next;
        }
    }
    
    // Helper to create a list from an array for testing
    private static ListNode? CreateLinkedList(int[]? values)
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
    
    // Helper to print a list for verification
    private static string PrintLinkedList(ListNode? head)
    {
        if (head == null)
        {
            return "[]";
        }

        var sb = new StringBuilder("[");
        var current = head;
        while (current != null)
        {
            sb.Append(current.val);
            if (current.next != null)
            {
                sb.Append(", ");
            }
            current = current.next;
        }
        sb.Append("]");
        
        return sb.ToString();
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
 * 🔎 Interview Questions for LeetCode 21. Merge Two Sorted Lists
 *
 * 1️⃣ What is the time and space complexity for both solutions?
 * 🔸 Iterative Solution:
 * → Time: O(n + m) — We must visit every node in both lists exactly once, where n and m are the lengths of the lists.
 * → Space: O(1) — We only use a few extra pointers (dummy, current), regardless of the list size.
 *
 * 🔹 Recursive Solution:
 * → Time: O(n + m) — Each recursive call processes one node, resulting in n + m total calls.
 * → Space: O(n + m) — The space is consumed by the recursion stack. The worst-case depth is the sum of the lengths of both lists.
 *
 * 2️⃣ Why is a dummy node useful in the iterative solution?
 * → The dummy node acts as a placeholder for the head of the new list.
 * This greatly simplifies the code by eliminating the need for a special conditional check to handle the creation of the very first node
 * in the merged list.
 * We can simply start appending nodes and return `dummy.next` at the end.
 *
 * 3️⃣ Which approach is generally preferred in an interview: iterative or recursive?
 * → The **iterative** approach is often preferred. Its O(1) space complexity is superior to the recursive solution's O(n + m) space complexity.
 * This makes it more memory-efficient and safer, as it avoids the risk of a stack overflow error that could occur with very long lists.
 *
 * 4️⃣ What are the key edge cases to consider?
 * → One or both input lists are empty (null).
 * → Lists with only one node.
 * → Lists where all elements of one list are smaller than all elements of the other.
 * → Lists containing duplicate numbers across one or both lists.
 *
 * 5️⃣ Can this logic be extended to merge 'k' sorted lists?
 * → Yes. A common follow-up question.
 * While you could merge lists one by one, it's inefficient.
 * A much better approach is to use a Min-Heap (Priority Queue) to keep track of the smallest element among all k lists,
 * leading to a time complexity of O(N log k), where N is the total number of nodes.
 *
 * 6️⃣ Why does the recursive solution work?
 * → It uses a "divide and conquer" strategy.
 * The problem of merging `list1` and `list2` is reduced to picking the smaller of the two head nodes and then
 * recursively calling the function to merge the rest of the lists.
 * The base cases (when one list is null) stop the recursion, and the call stack unwinds to link the nodes together in sorted order.
 ***************************************************************/