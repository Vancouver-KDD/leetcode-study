/***************************************************************
 * 🔷 LeetCode 125. Valid Palindrome
 *
 * 🟢 Difficulty: Easy
 *
 * 📘 Problem:
 *   A phrase is a palindrome if, after converting all uppercase
 *   letters into lowercase and removing all non-alphanumeric
 *   characters, it reads the same forward and backward.
 *
 *   Alphanumeric characters include letters and numbers.
 *
 *   Given a string `s`, return true if it is a palindrome, or
 *   false otherwise.
 *
 * 📥 Example 1:
 *   Input:  s = "A man, a plan, a canal: Panama"
 *   Output: true
 *   Explanation: "amanaplanacanalpanama" is a palindrome.
 *
 * 📥 Example 2:
 *   Input:  s = "race a car"
 *   Output: false
 *   Explanation: "raceacar" is not a palindrome.
 *
 * 📥 Example 3:
 *   Input:  s = " "
 *   Output: true
 *   Explanation: An empty string is considered a palindrome.
 * 
 * 🚩 Topic:
 *	 Two Pointers, String
 ***************************************************************/

using System.Diagnostics;

namespace Week2_TwoPtrSlideWin;

public class ValidPalindrome_125
{
    static void Main(string[] args)
    {
        Console.WriteLine("[ValidPalindrome_125]");

        string[] testCases = {
            "A man, a plan, a canal: Panama",  // true
            "race a car",                      // false
            " ",                               // true
            "No 'x' in Nixon",                 // true
            "Was it a car or a cat I saw?"     // true
        };

        MeasureExecutionTime(() =>
        {
            for (var i = 0; i < testCases.Length; i++)
            {
                var input = testCases[i];
                var result = IsPalindrome(input);
                Console.WriteLine($"Test Case {i + 1}: \"{input}\" → {result}");
            }
        });
    }
    
    /// <summary>
    /// This solution uses the Two Pointers technique to check whether a string is a valid palindrome.
    /// We initialize two pointers at the beginning and end of the string, and move them inward.
    /// While moving, we skip non-alphanumeric characters and compare the lowercase values of each character.
    /// If all valid characters match symmetrically, the string is a palindrome.
    /// This approach runs in O(n) time and uses O(1) additional space.
    /// </summary>
    /// <param name="s"></param>
    /// <returns></returns>
    private static bool IsPalindrome(string s)
    {
        var left = 0;
        var right = s.Length - 1;

        while (left < right)
        {
            // Skip non-alphanumeric characters on the left
            while (left < right && char.IsLetterOrDigit(s[left]) == false)
            {
                left++;
            }

            // Skip non-alphanumeric characters on the right
            while (left < right && char.IsLetterOrDigit(s[right]) == false)
            {
                right--;
            }

            // Compare characters after converting to lowercase
            if (char.ToLower(s[left]) != char.ToLower(s[right]))
            {
                return false;
            }

            left++;
            right--;
        }

        return true;
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
 * 🔎 Interview Questions for LeetCode 125. Valid Palindrome
 *
 * 1️⃣ What is a palindrome?
 *     → A string that reads the same forward and backward.
 *
 * 2️⃣ Why did you use the two pointers technique?
 *     → It allows efficient comparison from both ends with O(n) time
 *        and avoids creating a new string, saving space.
 *
 * 3️⃣ How do you handle case sensitivity and non-alphanumeric characters?
 *     → Convert characters to lowercase using `char.ToLower`,
 *        and skip non-alphanumeric using `char.IsLetterOrDigit`.
 *
 * 4️⃣ What happens if the string only contains spaces or symbols?
 *     → All such characters are skipped; the string becomes empty,
 *        which is considered a valid palindrome.
 *
 * 5️⃣ What is the time and space complexity?
 *     → Time: O(n), Space: O(1) if using two pointers directly.
 *
 * 6️⃣ Could you solve this in another way?
 *     → Yes, by filtering the string using regex or a `StringBuilder`,
 *        then comparing it to its reverse — but this uses O(n) space.
 ***************************************************************/