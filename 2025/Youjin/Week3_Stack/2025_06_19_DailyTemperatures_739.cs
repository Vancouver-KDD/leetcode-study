/***************************************************************
 * 🔷 LeetCode 739. Daily Temperatures
 *
 * 🟡 Difficulty: Medium
 *
 * 📘 Problem:
 *   Given an array of integers `temperatures` representing 
 *   the daily temperatures, return an array `answer` such that 
 *   `answer[i]` is the number of days you have to wait after 
 *   the `i-th` day to get a warmer temperature.
 * 
 *   If there is no future day for which this is possible, 
 *   keep `answer[i] == 0` instead.
 *
 * 📥 Example 1:
 *   Input:  temperatures = [73,74,75,71,69,72,76,73]
 *   Output: [1,1,4,2,1,1,0,0]
 *
 * 📥 Example 2:
 *   Input:  temperatures = [30,40,50,60]
 *   Output: [1,1,1,0]
 *
 * 📥 Example 3:
 *   Input:  temperatures = [30,60,90]
 *   Output: [1,1,0]
 *
 * 🚩 Topic:
 *   Array, Stack, Monotonic Stack
 ***************************************************************/

using System.Diagnostics;
using System.Reflection;

namespace Week3_Stack_Assign2;

class DailyTemperatures_739
{
    static void Main(string[] args)
    {
        int[] temperaturesCase1 = [73, 74, 75, 71, 69, 72, 76, 73];
        int[] temperaturesCase2 = [30, 40, 50, 60];
        int[] temperaturesCase3 = [30, 60, 90];
        
        MeasureExecutionTime(() =>
        {
            var answer1 = DailyTemperatures(temperaturesCase1);
            Console.WriteLine(string.Join(", ", answer1));
        });
        
        var answer2 = DailyTemperatures(temperaturesCase2);
        Console.WriteLine(string.Join(", ", answer2));
        var answer3 = DailyTemperatures(temperaturesCase3);
        Console.WriteLine(string.Join(", ", answer3));
    }
    
    private static int[] DailyTemperatures(int[] temperatures) 
    {
        // Stack to stores indices
        var stack = new Stack<int>(); 
        var answer = new int[temperatures.Length];

        for (var i = 0; i < temperatures.Length; i++) 
        {
            // Check if the current temperature is higher than the one at the top of the stack
            while (stack.Count > 0 && temperatures[i] > temperatures[stack.Peek()]) 
            {
                var prevIndex = stack.Pop();
                answer[prevIndex] = i - prevIndex; // How many days to wait
            }
            
            stack.Push(i); // Push current day's index
        }

        return answer;
    }
    
    private static void MeasureExecutionTime(Action action)
    {
        var stopwatch = Stopwatch.StartNew();
        action();
        stopwatch.Stop();
        Console.WriteLine($"Execution Time: {stopwatch.Elapsed.TotalMilliseconds} ms\n");
    }
}