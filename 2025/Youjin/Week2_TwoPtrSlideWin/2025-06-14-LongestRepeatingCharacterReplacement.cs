/***************************************************************
 * 🔷 LeetCode 424. Longest Repeating Character Replacement     
 *                                                              
 * 🟠 Difficulty: Medium                                        
 *                                                              
 * 📘 Problem:                                                  
 *   You are given a string `s` and an integer `k`.             
 *   You can change any character in the string to any other    
 *   uppercase English letter, at most `k` times.               
 *                                                              
 *   Return the length of the longest substring containing      
 *   the same letter after performing up to `k` replacements.   
 *                                                              
 * 📥 Example 1:                                                 
 *   Input:  s = "ABAB", k = 2                                  
 *   Output: 4                                                  
 *   Explanation: Replace two 'A's with 'B's (or vice versa),   
 *                result: "BBBB" or "AAAA".                     
 *                                                              
 * 📥 Example 2:                                                 
 *   Input:  s = "AABABBA", k = 1                                
 *   Output: 4                                                  
 *   Explanation: Replace the middle 'A' with 'B',              
 *                result: "AABBBBA" → "BBBB" has length 4.      
 *                Other valid transformations may exist.        
 * 
 * 🚩 Topic:
 *	 Hash Table, String, Sliding Window
 ***************************************************************/

using System.Diagnostics;

namespace Week2_TwoPtrSlideWin;

public class LongestRepeatingCharacterReplacement_424
{
    static void Main(string[] args)
    {
        const string testCase1 = "ABAB";
        const string testCase2 = "AABABBA";
        
        MeasureExecutionTime(() =>
        {
            var resultTestCase1 = CharacterReplacement(testCase1, 2);
            Console.WriteLine($"TestCase1 {testCase1} Output: {resultTestCase1}");
        });
        
        var resultTestCase2 = CharacterReplacement(testCase2, 1);
        Console.WriteLine($"TestCase1 {testCase2} Output: {resultTestCase2}");
    }

    private static int CharacterReplacement(string s, int k)
    {
        // Dictionary to track the frequency of each character in the current sliding window
        var charCounts = new Dictionary<char, int>();

        var windowStart = 0;           // Left boundary of the sliding window
        var maxLength = 0;      // Length of the longest valid substring found
        var maxCount = 0;       // Highest frequency of any single character in the window

        // Expand the sliding window by moving the right boundary
        for (var i = 0; i < s.Length; i++)
        {
            var currentChar = s[i];

            // Increment the frequency count for the current character
            if (charCounts.ContainsKey(currentChar) == false)
            {
                charCounts[currentChar] = 0;    // Initialize if not present
            }
            charCounts[currentChar]++;

            // Update the count of the most frequent character in the current window
            maxCount = Math.Max(maxCount, charCounts[currentChar]);

            // If the remaining characters (that are not the most frequent one) exceed k,
            // shrink the window from the left
            while (i - windowStart + 1 - maxCount > k)
            {
                var leftChar = s[windowStart];
                charCounts[leftChar]--;
                windowStart++;
            }

            // Update the maximum length of a valid window found so far
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