/***************************************************************
 * 🔷 LeetCode 3. Longest Substring Without Repeating Characters
 *                                                              
 * 🟠 Difficulty: Medium                                        
 *                                                              
 * 📘 Problem:                                                  
 *   Given a string `s`, find the length of the longest         
 *   substring without repeating characters.                    
 *                                                              
 *   A substring is a contiguous sequence of characters,        
 *   unlike a subsequence.                                      
 *                                                              
 * 📥 Example 1:                                                 
 *   Input:  s = "abcabcbb"                                     
 *   Output: 3                                                  
 *   Explanation: The answer is "abc", with length 3.           
 *                                                              
 * 📥 Example 2:                                                 
 *   Input:  s = "bbbbb"                                        
 *   Output: 1                                                  
 *   Explanation: The answer is "b".                            
 *                                                              
 * 📥 Example 3:                                                 
 *   Input:  s = "pwwkew"                                       
 *   Output: 3                                                  
 *   Explanation: The answer is "wke", with length 3.           
 *                "pwke" is not valid because it's not a       
 *                contiguous substring.                         
 * 
 * 🚩 Topic:
 *	 Hash Table, String, Sliding Window
 ***************************************************************/

using System.Diagnostics;

namespace Week2_TwoPtrSlideWin;

public class LongestSubstringWithoutRepeatingCharacters_3
{
    static void Main(string[] args)
    {
        const string testCase1 = "abcabcbb";
        const string testCase2 = "bbbbb";
        const string testCase3 = "pwwkew";

        MeasureExecutionTime(() =>
        {
            var resultTestCase1 = LengthOfLongestSubstring(testCase1);
            Console.WriteLine($"TestCase1 {testCase1} Output: {resultTestCase1}");
        });
        
        var resultTestCase2 = LengthOfLongestSubstring(testCase2);
        Console.WriteLine($"TestCase1 {testCase2} Output: {resultTestCase2}");
        
        var resultTestCase3 = LengthOfLongestSubstring(testCase3);
        Console.WriteLine($"TestCase1 {testCase3} Output: {resultTestCase3}");
    }
    
    private static int LengthOfLongestSubstring(string s)
    {
        // Dictionary to track the last occurrence index of each character
        var lastSeenIndex = new Dictionary<char, int>();

        var maxLength = 0;          // The length of the longest substring found
        var windowStart = 0;        // Start index of the current sliding window

        for (var i = 0; i < s.Length; i++)
        {
            var currentChar = s[i];

            // If the character has been seen and is within the current window,
            // move the window start to one position after its last seen index.
            if (lastSeenIndex.ContainsKey(currentChar) && lastSeenIndex[currentChar] >= windowStart)
            {
                windowStart = lastSeenIndex[currentChar] + 1;
            }

            // Update the last seen index of the current character
            lastSeenIndex[currentChar] = i;

            // Update the maximum length of substring found so far
            var windowLength = i - windowStart + 1;
            maxLength = Math.Max(maxLength, windowLength);
        }

        return maxLength;
    }
    
    private static void MeasureExecutionTime(Action action)
    {
        var stopwatch = Stopwatch.StartNew();
        action();
        stopwatch.Stop();
        Console.WriteLine($"Execution Time: {stopwatch.Elapsed.TotalMilliseconds} ms\n");
    }
}