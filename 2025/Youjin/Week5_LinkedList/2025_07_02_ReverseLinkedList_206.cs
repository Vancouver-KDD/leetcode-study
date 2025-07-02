/***************************************************************
 * 🔷 LeetCode 206. Reverse Linked List
 *
 * 🟢 Difficulty: Easy
 *
 * 📘 Problem:
 *   Given the head of a singly linked list, reverse the list,
 *   and return the reversed list.
 *
 * 📥 Example 1:
 *   Input:  head = [1,2,3,4,5]
 *   Output: [5,4,3,2,1]
 *
 * 📥 Example 2:
 *   Input:  head = [1,2]
 *   Output: [2,1]
 *
 * 📥 Example 3:
 *   Input:  head = []
 *   Output: []
 *
 * ✅ Constraints:
 *   - The number of nodes in the list is in the range [0, 5000].
 *   - -5000 <= Node.val <= 5000
 *
 * 💡 Follow up:
 *   - A linked list can be reversed either iteratively or recursively.
 *     Could you implement both?
 *
 * 🚩 Topics:
 *   Linked List, Recursion
 ***************************************************************/

using System.Diagnostics;
using System.Text;

namespace Week5_LinkedList_Assign2;

public class ReverseLinkedList_206
{
    private static void Main(string[] args)
    {
        var solution = new ReverseLinkedList_206();

        // Create two identical lists for testing both versions
        var listForIterative = CreateLinkedList([1, 2, 3, 4, 5]);
        var listForRecursive = CreateLinkedList([1, 2, 3, 4, 5]);

        Console.WriteLine($"Original List: {PrintLinkedList(listForIterative)}\n");

        // --- Test Iterative Version ---
        Console.WriteLine("--- Iterative Solution ---");
        MeasureExecutionTime(() =>
        {
            var reversedList = solution.ReverseList_Iterative(listForIterative);
            Console.WriteLine($"Reversed List: {PrintLinkedList(reversedList)}");
        });

        // --- Test Recursive Version ---
        Console.WriteLine("--- Recursive Solution ---");
        MeasureExecutionTime(() =>
        {
            var reversedList = solution.ReverseList_Recursive(listForRecursive);
            Console.WriteLine($"Reversed List: {PrintLinkedList(reversedList)}");
        });
    }
    
    /// <summary>
    /// Reverses a linked list using a recursive approach.
    /// This method uses O(n) space for the recursion call stack.
    /// </summary>
    private ListNode? ReverseList_Recursive(ListNode? head)
    {
        // Base case: if the list is empty or has only one node, it's already reversed
        if (head?.next == null)
        {
            return head;
        }

        // Recursively reverse the rest of the list
        var newHead = ReverseList_Recursive(head.next);

        // After the above call, head.Next is the last node of the original list.
        // We want this node to point back to the current 'head'.
        head.next.next = head;

        // Break the original forward link to prevent a cycle
        head.next = null;

        // 'newHead' is the head of the fully reversed list
        return newHead;
    }

    /// <summary>
    /// Reverses a linked list using an iterative approach.
    /// This method uses constant extra space O(1).
    /// </summary>
    private ListNode? ReverseList_Iterative(ListNode? head)
    {
        ListNode? prev = null;
        var current = head;

        while (current != null)
        {
            // 1. Store the next node before we change the link
            var nextTemp = current.next;

            // 2. Reverse the link of the current node
            current.next = prev;

            // 3. Move pointers one step forward
            prev = current;
            current = nextTemp;
        }
        // At the end, 'prev' will be the new head of the reversed list
        return prev;
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
    
    #region Helper Methods for Testing

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
    
    #endregion Helper Methods for Testing
}

/***************************************************************
 * 🔎 Interview Questions for LeetCode 206. Reverse Linked List
 *
 * 1️⃣ What is the time and space complexity for both solutions?
 * 🔸 Iterative Solution:
 * → Time: O(n) — We must traverse the entire list once.
 * → Space: O(1) — We only use a few pointers (prev, current, nextTemp), requiring constant extra space.
 *
 * 🔹 Recursive Solution:
 * → Time: O(n) — Each node is visited once during the recursion.
 * → Space: O(n) — The space is used by the recursion call stack. In the worst case, the stack's depth is equal to the number of nodes in the list.
 *
 * 2️⃣ How does the iterative approach work?
 * → It uses three pointers: `prev`, `current`, and `nextTemp`.
 * The `current` pointer iterates through the list. In each step, we first store the `next` node so we don't lose the rest of the list.
 * Then, we reverse the `current` node's pointer to point to `prev`. Finally, we move `prev` and `current` one step forward for the next iteration.
 *
 * 3️⃣ How does the recursive approach work?
 * → It uses a "divide and conquer" strategy.
 * 1. Base Case: If the list is empty or has only one node, it's already reversed, so we return it.
 * 2. Recursive Step: The function calls itself on the rest of the list (`head.next`). This call reverses the entire sublist and returns its new head.
 * 3. Link Reversal: After the sub-problem is solved, the original `head` is attached to the end of the reversed sublist by making its original successor point back to it (`head.next.next = head`).
 *
 * 4️⃣ Which approach is generally preferred and why?
 * → In a production environment, the **iterative** approach is generally preferred.
 * ✅ Its O(1) space complexity is more efficient and avoids the risk of a "stack overflow" error,
 * which can occur with the recursive solution if the linked list is very long.
 *
 * 5️⃣ What are the key edge cases to consider?
 * → An empty list (`head == null`).
 * → A list with only one node (`head.next == null`).
 * ✅ Both provided solutions handle these cases correctly. The iterative loop won't execute, and the recursive function will hit its base case immediately, returning the correct result.
 *
 * 6️⃣ What is a common follow-up to this problem?
 * → A very common follow-up is "Reverse Linked List II" (LeetCode 92),
 * where you are asked to reverse only a portion of the list, from position `m` to `n`. This tests a deeper understanding of pointer manipulation.
 ***************************************************************/