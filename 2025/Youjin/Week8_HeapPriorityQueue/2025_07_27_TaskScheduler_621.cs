/***************************************************************
 * 🔷 LeetCode 621. Task Scheduler
 *
 * 🟡 Difficulty: Medium
 *
 * 📘 Problem:
 *   You are given an array of CPU tasks, each represented by a capital letter A to Z.
 *   Each task takes one interval to complete, but the same task type must be separated
 *   by at least `n` intervals (cooling period).
 *
 *   Each interval can execute a task or be idle.
 *   Return the **minimum number of intervals** the CPU will take to finish all tasks.
 *
 * 📥 Example 1:
 *   Input:  tasks = ["A","A","A","B","B","B"], n = 2
 *   Output: 8
 *   Explanation: A → B → idle → A → B → idle → A → B
 *
 * 📥 Example 2:
 *   Input:  tasks = ["A","C","A","B","D","B"], n = 1
 *   Output: 6
 *   Explanation: A → B → C → D → A → B
 *
 * 📥 Example 3:
 *   Input:  tasks = ["A","A","A","B","B","B"], n = 3
 *   Output: 10
 *   Explanation: A → B → idle → idle → A → B → idle → idle → A → B
 *
 * ✅ Constraints:
 *   - 1 <= tasks.length <= 10⁴
 *   - tasks[i] is an uppercase English letter (A–Z)
 *   - 0 <= n <= 100
 *
 * 🚩 Topics:
 *   Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting
 ***************************************************************/

using System.Diagnostics;

namespace Week8_HeapPriorityQueue_Assign2;

public class TaskScheduler_621
{
    private static void Main()
    {
        var solution = new TaskScheduler_621();

        // --- Example 1 ---
        char[] tasks1 = { 'A', 'A', 'A', 'B', 'B', 'B' };
        const int n1 = 2;
        Console.WriteLine($"Example 1: tasks = [{string.Join(",", tasks1)}], n = {n1}");
        Console.WriteLine(new string('-', 50));

        Console.WriteLine("🔸 Using Max Heap (Simulation):");
        MeasureExecutionTime(() =>
        {
            var result = solution.LeastInterval_HeapQueue(tasks1, n1);
            Console.WriteLine($"Result: {result}"); // Expected: 8
        });

        Console.WriteLine("🔸 Using Counting & Greedy Formula:");
        MeasureExecutionTime(() =>
        {
            var result = solution.LeastInterval_CountingGreedy(tasks1, n1);
            Console.WriteLine($"Result: {result}"); // Expected: 8
        });

        Console.WriteLine("\n" + new string('=', 60) + "\n");

        // --- Example 2 ---
        char[] tasks2 = { 'A', 'C', 'A', 'B', 'D', 'B' };
        const int n2 = 1;
        Console.WriteLine($"Example 2: tasks = [{string.Join(",", tasks2)}], n = {n2}");
        Console.WriteLine(new string('-', 50));

        Console.WriteLine("🔸 Using Max Heap (Simulation):");
        MeasureExecutionTime(() =>
        {
            var result = solution.LeastInterval_HeapQueue(tasks2, n2);
            Console.WriteLine($"Result: {result}"); // Expected: 6
        });

        Console.WriteLine("🔸 Using Counting & Greedy Formula:");
        MeasureExecutionTime(() =>
        {
            var result = solution.LeastInterval_CountingGreedy(tasks2, n2);
            Console.WriteLine($"Result: {result}"); // Expected: 6
        });

        Console.WriteLine("\n" + new string('=', 60) + "\n");

        // --- Example 3 ---
        char[] tasks3 = { 'A', 'A', 'A', 'B', 'B', 'B' };
        var n3 = 3;
        Console.WriteLine($"Example 3: tasks = [{string.Join(",", tasks3)}], n = {n3}");
        Console.WriteLine(new string('-', 50));

        Console.WriteLine("🔸 Using Max Heap (Simulation):");
        MeasureExecutionTime(() =>
        {
            var result = solution.LeastInterval_HeapQueue(tasks3, n3);
            Console.WriteLine($"Result: {result}"); // Expected: 10
        });

        Console.WriteLine("🔸 Using Counting & Greedy Formula:");
        MeasureExecutionTime(() =>
        {
            var result = solution.LeastInterval_CountingGreedy(tasks3, n3);
            Console.WriteLine($"Result: {result}"); // Expected: 10
        });
    }

    /// <summary>
    /// Solves the problem by simulating the process using a Max Heap and a Queue.
    /// The heap always provides the most frequent task to execute next (greedy choice).
    /// The queue manages tasks that are in their cooling-down period.
    /// </summary>
    /// <param name="tasks">Array of tasks to execute.</param>
    /// <param name="n">The cooling period.</param>
    /// <returns>The minimum time intervals required.</returns>
    private int LeastInterval_HeapQueue(char[] tasks, int n)
    {
        // Step 1: Count the frequency of each task.
        var freq = new int[26];
        foreach (var task in tasks)
        {
            freq[task - 'A']++;
        }

        // Step 2: Create a Max Heap to store frequencies in descending order.
        // This allows us to always pick the most frequent task.
        var maxHeap = new PriorityQueue<int, int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));
        foreach (var f in freq)
        {
            if (f > 0)
            {
                maxHeap.Enqueue(f, f);
            }
        }

        var time = 0;
        // This queue will store tasks that are in their cooldown period.
        // Format: (remaining_count, available_at_time)
        var cooldown = new Queue<(int remaining, int availableAt)>();

        // Loop until both the heap (tasks ready to run) and the cooldown queue are empty.
        while (maxHeap.Count > 0 || cooldown.Count > 0)
        {
            time++; // Advance one time interval.

            // First, check if any task is ready to come out of cooldown.
            // A task is ready if its `availableAt` time matches the current `time`.
            // This check must happen before scheduling a new task.
            if (cooldown.Count > 0 && cooldown.Peek().availableAt == time)
            {
                var task = cooldown.Dequeue();
                maxHeap.Enqueue(task.remaining, task.remaining);
            }

            // If the heap is not empty, we can schedule a task.
            if (maxHeap.Count > 0)
            {
                var count = maxHeap.Dequeue();
                // If the task still needs to be run again, add it to the cooldown queue.
                // It will be available again after `n` intervals from now.
                if (count - 1 > 0)
                {
                    cooldown.Enqueue((count - 1, time + n));
                }
            }
            // If the heap is empty but cooldown is not, the CPU must be idle for this time interval.
            // The loop continues, incrementing `time` until a task is ready from the cooldown queue.
        }

        return time;
    }

    /// <summary>
    /// Solves the problem using a mathematical greedy formula based on the most frequent task.
    /// This is more efficient than simulation as it calculates the result directly.
    /// </summary>
    /// <param name="tasks">Array of tasks to execute.</param>
    /// <param name="n">The cooling period.</param>
    /// <returns>The minimum time intervals required.</returns>
    private int LeastInterval_CountingGreedy(char[] tasks, int n)
    {
        // Step 1: Count frequencies of each task.
        var freq = new int[26];
        foreach (var task in tasks)
        {
            freq[task - 'A']++;
        }

        // Step 2: Sort frequencies to easily find the max frequency.
        Array.Sort(freq);
        var maxFreq = freq[25]; // The most frequent task's count.

        // Step 3: Calculate the number of idle slots created by the most frequent task.
        // The most frequent task creates (maxFreq - 1) blocks of time before its last execution.
        // Each block has a size of `n` (the cooldown period).
        // Example: A, _, _, A, _, _, A. Here maxFreq=3, so there are 2 blocks of size n=2.
        var idleSlots = (maxFreq - 1) * n;

        // Step 4: Fill the idle slots with other tasks.
        // Iterate backwards from the second most frequent task.
        for (var i = 24; i >= 0 && freq[i] > 0; i--)
        {
            // A less frequent task can fill up the idle slots.
            // If a task has frequency equal to maxFreq, it takes up a full "column"
            // in the schedule, so it reduces the idle slots by (maxFreq - 1).
            // If a task is less frequent, it only fills freq[i] slots.
            idleSlots -= Math.Min(maxFreq - 1, freq[i]);
        }

        // If idleSlots is negative, it means we have more tasks than slots,
        // so no idling is needed. We cap it at 0.
        idleSlots = Math.Max(0, idleSlots);

        // The total time is the time to execute all tasks plus any necessary idle time.
        return tasks.Length + idleSlots;
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
 * 🔍 Interview Questions for LeetCode 621 – Task Scheduler
 *
 * 1️⃣ What is the goal of this problem?
 *     - To determine the minimum number of CPU intervals required to finish all given tasks
 *       with the constraint that the same task must have at least `n` intervals between executions.
 *
 * 2️⃣ What are the two main strategies to solve this?
 *     - 1. Simulation using Max Heap (Priority Queue) + Cooldown Queue.
 *     - 2. Counting frequencies + Greedy mathematical formula.
 *
 * 3️⃣ What is the time and space complexity of each approach?
 *     - Heap + Queue:
 *         - Time: O(N log K), where N = total tasks, K = number of unique tasks (≤ 26).
 *         - Space: O(K) for heap + cooldown queue.
 *     - Counting + Greedy:
 *         - Time: O(N + K log K) ≈ O(N), since K is at most 26.
 *         - Space: O(1) (constant space for 26 letters).
 *
 * 4️⃣ How does the Heap + Queue simulation work?
 *     - Always pick the task with the highest frequency (max heap).
 *     - After execution, put it in a cooldown queue for `n` intervals.
 *     - Each time unit, check if any task can return from cooldown to heap.
 *     - Continue until both heap and cooldown are empty.
 *
 * 5️⃣ How does the Counting + Greedy formula work?
 *     - Focus on the most frequent task and build a schedule based on its block pattern:
 *       (maxFreq - 1) * (n + 1) + tasks with max frequency.
 *     - Calculate idle slots and subtract the frequencies of other tasks to fill them.
 *     - Total time = total tasks + max(0, remaining idle slots).
 *
 * 6️⃣ When should you prefer one over the other?
 *     - Heap + Queue: Good for interview explanation, clear simulation logic.
 *     - Counting + Greedy: Optimal in real-world for performance and simplicity.
 *
 * 7️⃣ What edge cases should be considered?
 *     - n = 0: No cooldown, just return task.Length.
 *     - All tasks the same: Full idle intervals are required.
 *     - All tasks unique: No idle time.
 *
 * 8️⃣ What does the greedy method assume?
 *     - That idle time is only created by the most frequent task(s), and all other tasks are used to reduce that idle time.
 *
 * 9️⃣ Can the result be smaller than any formula estimate?
 *     - No. The result is always ≥ tasks.Length. The greedy estimate ensures the **minimum** required.
 *
 ***************************************************************/