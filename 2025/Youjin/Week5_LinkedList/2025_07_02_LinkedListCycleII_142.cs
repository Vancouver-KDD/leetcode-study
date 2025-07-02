/***************************************************************
 * 🔷 LeetCode 142. Linked List Cycle II
 *
 * 🟡 Difficulty: Medium
 *
 * 📘 Problem:
 *   Given the head of a linked list, return the node where the cycle begins.
 *   If there is no cycle, return null.
 *
 *   There is a cycle in a linked list if there is some node in the list that
 *   can be reached again by continuously following the next pointer.
 *
 *   Internally, pos is used to denote the index of the node that tail's next
 *   pointer is connected to (0-indexed). It is -1 if there is no cycle.
 *   Note: `pos` is not passed as a parameter.
 *
 *   Do not modify the linked list.
 *
 * 📥 Example 1:
 *   Input:  head = [3,2,0,-4], pos = 1
 *   Output: tail connects to node index 1
 *   Explanation: There is a cycle in the linked list, where tail connects to the second node.
 *
 * 📥 Example 2:
 *   Input:  head = [1,2], pos = 0
 *   Output: tail connects to node index 0
 *   Explanation: There is a cycle in the linked list, where tail connects to the first node.
 *
 * 📥 Example 3:
 *   Input:  head = [1], pos = -1
 *   Output: no cycle
 *   Explanation: There is no cycle in the linked list.
 *
 * ✅ Constraints:
 *   - The number of the nodes in the list is in the range [0, 10⁴].
 *   - -10⁵ <= Node.val <= 10⁵
 *   - `pos` is -1 or a valid index in the linked-list.
 *
 * 💡 Follow up:
 *   Can you solve it using O(1) (i.e., constant) memory?
 *
 * 🚩 Topics:
 *   Hash Table, Linked List, Two Pointers
 ***************************************************************/

using System.Diagnostics;

namespace Week5_LinkedList_Assign3;

public class LinkedListCycleII_142
{
    private static void Main(string[] args)
    {
        var solution = new LinkedListCycleII_142();

        // --- Test Case 1: head = [3,2,0,-4], pos = 1 ---
        var node1 = new ListNode(3);
        var node2 = new ListNode(2);
        var node3 = new ListNode(0);
        var node4 = new ListNode(-4);
        node1.next = node2;
        node2.next = node3;
        node3.next = node4;
        node4.next = node2; // Cycle starts at node with value 2

        Console.WriteLine("--- Test Case 1 ---");
        MeasureExecutionTime(() => {
            var result = solution.DetectCycle(node1);
            Console.WriteLine(result != null ? $"Cycle begins at node with value: {result.val}" : "No cycle");
        });

        // --- Test Case 2: head = [1,2], pos = 0 ---
        var nodeA = new ListNode(1);
        var nodeB = new ListNode(2);
        nodeA.next = nodeB;
        nodeB.next = nodeA; // Cycle starts at node with value 1

        Console.WriteLine("--- Test Case 2 ---");
        MeasureExecutionTime(() => {
            var result = solution.DetectCycle(nodeA);
            Console.WriteLine(result != null ? $"Cycle begins at node with value: {result.val}" : "No cycle");
        });

        // --- Test Case 3: head = [1], pos = -1 ---
        var nodeC = new ListNode(1);

        Console.WriteLine("--- Test Case 3 ---");
        MeasureExecutionTime(() => {
            var result = solution.DetectCycle(nodeC);
            Console.WriteLine(result != null ? $"Cycle begins at node with value: {result.val}" : "No cycle");
        });
    }
    
    /// <summary>
    /// Detects the starting node of a cycle in a linked list using Floyd's algorithm.
    /// </summary>
    /// <param name="head">The head of the linked list.</param>
    /// <returns>The node where the cycle begins, or null if there is no cycle.</returns>
    private ListNode? DetectCycle(ListNode? head)
    {
        if (head?.next == null)
        {
            return null;
        }

        var slow = head;
        var fast = head;

        // Phase 1: Find the meeting point inside the cycle.
        while (fast != null && fast.next != null)
        {
            slow = slow?.next;
            fast = fast.next.next;

            if (slow != fast)
            {
                continue;
            }
            
            // Cycle detected. Now find the start of the cycle.
            // Phase 2: Move one pointer from the head and another from the meeting point.
            var finder = head;
            while (finder != slow)
            {
                finder = finder?.next;
                slow = slow?.next;
            }
            // The point where they meet is the start of the cycle.
            return finder;
        }

        // If the loop finishes, fast reached the end, so there is no cycle.
        return null;
    }

    public class ListNode
    {
        public int val;
        public ListNode? next;

        public ListNode(int x)
        {
            val = x;
            next = null;
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
 * 🔎 Interview Questions for LeetCode 142. Linked List Cycle II
 *
 * 1️⃣ What is the time and space complexity of the common solutions?
 * 🔸 Hash Table Solution:
 * → Time: O(n) — We must iterate through the list once, performing a constant-time hash table insertion and lookup at each step.
 * → Space: O(n) — In the worst case, we might need to store all nodes in the hash set before finding the cycle.
 *
 * 🔹 Two Pointers (Floyd's Algorithm):
 * → Time: O(n) — Although the fast pointer moves more steps, the total time is proportional to the number of nodes in the list.
 * → Space: O(1) — This is the optimal solution, as it only requires a few pointers, regardless of the list's size.
 *
 * 2️⃣ Can you explain how Floyd's Two-Pointer algorithm works in two phases?
 * → **Phase 1: Detect the Cycle.** A `slow` pointer moves one step at a time, and a `fast` pointer moves two steps. If there's a cycle, they are guaranteed to meet at some node inside the cycle. If the `fast` pointer reaches `null`, there is no cycle.
 *
 * → **Phase 2: Find the Cycle's Start.** After the pointers meet, reset one pointer to the `head` of the list. Then, move both this pointer and the other pointer (which is still at the meeting point) one step at a time. The node where they meet again is the beginning of the cycle.
 *
 * 3️⃣ Why does the second phase of Floyd's algorithm work?
 * → The key insight is based on the distances traveled. Let `L` be the distance from the head to the cycle start, and `k` be the distance from the cycle start to the meeting point. It can be proven mathematically that `L` is equal to the distance from the meeting point back to the cycle start, moving in the direction of the cycle. Therefore, starting one pointer at the head and another at the meeting point and moving them at the same speed will cause them to collide at the cycle's entrance.
 *
 * 4️⃣ Why is the Two-Pointer method preferred over the Hash Table method?
 * → The primary reason is the **O(1) space complexity**. The problem's follow-up explicitly asks for a constant memory solution, making the Two-Pointer algorithm the intended and optimal approach. The Hash Table method, while conceptually simpler, fails this constraint.
 *
 * 5️⃣ What's the main difference between this problem (Cycle II) and Linked List Cycle I?
 * → **Linked List Cycle I** (LeetCode 141) is a simpler decision problem. It only asks *if* a cycle exists (return `true` or `false`). This only requires completing Phase 1 of Floyd's algorithm.
 * → **Linked List Cycle II** (this problem) asks for the *specific node* where the cycle begins, which requires implementing both Phase 1 and the more complex Phase 2.
 *
 * 6️⃣ What are some important edge cases to consider?
 * → An empty list (`head == null`).
 * → A list with only one or two nodes and no cycle.
 * → A list where the entire list is a cycle (the head is the start of the cycle, `pos = 0`).
 * → A very long list, which could cause a stack overflow if a recursive solution were attempted (which is not natural for this problem).
 ***************************************************************/