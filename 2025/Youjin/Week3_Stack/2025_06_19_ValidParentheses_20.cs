/***************************************************************
 * 🔷 LeetCode 20. Valid Parentheses
 *
 * 🟢 Difficulty: Easy
 *
 * 📘 Problem:
 *   Given a string `s` containing just the characters 
 *   '(', ')', '{', '}', '[' and ']', determine if the 
 *   input string is valid.
 *
 *   An input string is valid if:
 *   - Open brackets must be closed by the same type of brackets.
 *   - Open brackets must be closed in the correct order.
 *   - Every close bracket has a corresponding open bracket 
 *     of the same type.
 *
 * 📥 Example 1:
 *   Input:  s = "()"
 *   Output: true
 *
 * 📥 Example 2:
 *   Input:  s = "()[]{}"
 *   Output: true
 *
 * 📥 Example 3:
 *   Input:  s = "(]"
 *   Output: false
 *
 * 📥 Example 4:
 *   Input:  s = "([])"
 *   Output: true
 *
 * 🚩 Topic:
 *   String, Stack
 ***************************************************************/

using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace Week3_Stack_Assign1;

public class ValidParentheses_20
{
    public static void Main(string[] args)
    {
        var testCases1 = "()";
        var testCases2 = "()[]{}";
        var testCases3 = "(]";
        var testCases4 = "([])";
            
        MeasureExecutionTime(() =>
        {
            Console.WriteLine($"TestCase1: {IsValid(testCases1)}");
        });
            
        Console.WriteLine($"TestCase2: {IsValid(testCases2)}");
        Console.WriteLine($"TestCase3: {IsValid(testCases3)}");
        Console.WriteLine($"testCase4: {IsValid(testCases4)}");
    }

    private static bool IsValid(string s) 
    {
        // Use a stack to keep track of opening brackets
        var stack = new Stack<char>();     

        // Iterate through each character in the string
        foreach (var c in s)
        {
            // If it's an opening bracket, push it to the stack
            if (c == '(' || c == '{' || c == '[')
            {
                stack.Push(c);
            }
            else
            {
                // If the stack is empty, there's no matching opening bracket
                if (stack.Count == 0)
                {
                    return false;
                }

                // Pop the top element and check if it matches the current closing bracket
                var top = stack.Pop();

                // If the types don't match, the string is invalid
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '['))
                {
                    return false;
                }
            }
        }

        // If the stack is empty, all brackets were matched correctly
        return stack.Count == 0;
    }

    private static void MeasureExecutionTime(Action action)
    {
        var stopwatch = Stopwatch.StartNew();
        action();
        stopwatch.Stop();
        Console.WriteLine($"Execution Time: {stopwatch.Elapsed.TotalMilliseconds} ms\n");
    }
}