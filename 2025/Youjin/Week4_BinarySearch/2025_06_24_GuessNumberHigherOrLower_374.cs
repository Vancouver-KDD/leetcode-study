/***************************************************************
 * 🔷 LeetCode 374. Guess Number Higher or Lower
 *
 * 🟢 Difficulty: Easy
 *
 * 📘 Problem:
 *   We are playing the Guess Game. I pick a number from 1 to `n`.
 *   You have to guess which number I picked.
 *
 *   Every time you guess wrong, I will tell you whether the number 
 *   I picked is higher or lower than your guess.
 *
 *   You call a pre-defined API `int guess(int num)`, which returns:
 *     - -1: Your guess is higher than the number I picked.
 *     -  1: Your guess is lower than the number I picked.
 *     -  0: Your guess is equal to the number I picked.
 *
 *   Return the number that I picked.
 *
 * 📥 Example 1:
 *   Input:  n = 10, pick = 6
 *   Output: 6
 *
 * 📥 Example 2:
 *   Input:  n = 1, pick = 1
 *   Output: 1
 *
 * 📥 Example 3:
 *   Input:  n = 2, pick = 1
 *   Output: 1
 *
 * ✅ Constraints:
 *   - 1 <= n <= 2³¹ - 1
 *   - 1 <= pick <= n
 *
 * 🚩 Topics:
 *   Binary Search, Interactive
 ***************************************************************/

using System.Diagnostics;

namespace Week4_BinarySearch_Assign3
{
    public class GuessNumberHigherOrLower_374 : GuessGame
    {
        static void Main(string[] args)
        {
            // Simulate: Let's say the picked number is 6
            Pick = 6;

            MeasureExecutionTime(() =>
            {
                var solver = new GuessNumberHigherOrLower_374();
                var result = solver.GuessNumber(10);
                Console.WriteLine($"Guessed Number: {result}");
            });
        }

        /// <summary>
        /// Finds the number using binary search by querying guess(int num).
        /// </summary>
        private int GuessNumber(int n)
        {
            var left = 1;
            var right = n;

            while (left <= right)
            {
                // Avoid overflow by using this formula instead of (left + right) / 2
                var mid = left + (right - left) / 2;

                var result = Guess(mid); // Simulated API call

                if (result == 0)
                {
                    return mid; // Correct guess
                }

                if (result < 0)
                {
                    right = mid - 1; // Guessed number is too high
                }
                else
                {
                    left = mid + 1; // Guessed number is too low
                }
            }

            return -1; // Should not reach here
        }

        /// <summary>
        /// Measures and prints the execution time of an action.
        /// </summary>
        private static void MeasureExecutionTime(Action action)
        {
            var stopwatch = Stopwatch.StartNew();
            action();
            stopwatch.Stop();
            Console.WriteLine($"Execution Time: {stopwatch.Elapsed.TotalMilliseconds} ms\n");
        }
    }

    /// <summary>
    /// Simulated GuessGame base class with a static pick number and guess() API.
    /// </summary>
    public class GuessGame
    {
        // Static number picked for guessing (in LeetCode, this is hidden)
        protected static int Pick;

        /// <summary>
        /// Simulates the LeetCode API which tells whether the guess is too high, low, or correct.
        /// </summary>
        protected int Guess(int num)
        {
            if (num > Pick)
            {
                return -1;
            }

            if (num < Pick)
            {
                return 1;
            }
            
            return 0;
        }
    }
}