/***************************************************************
 * 🔷 LeetCode 735. Asteroid Collision
 *
 * 🟡 Difficulty: Medium
 *
 * 📘 Problem:
 *   We are given an array `asteroids` of integers representing 
 *   asteroids in a row. The index represents their position in space.
 *
 *   - The **absolute value** of each asteroid represents its **size**.
 *   - The **sign** represents its **direction**:
 *     - Positive ➡️: moving to the right
 *     - Negative ⬅️: moving to the left
 *
 *   All asteroids move at the same speed.
 *
 *   When two asteroids collide:
 *   - The smaller one explodes.
 *   - If they are the same size, both explode.
 *   - Asteroids moving in the same direction will **never** meet.
 *
 *   Return the state of the asteroids after all collisions.
 *
 * 📥 Example 1:
 *   Input:  asteroids = [5,10,-5]
 *   Output: [5,10]
 *   Explanation: 10 and -5 collide → 10 survives. 5 and 10 never collide.
 *
 * 📥 Example 2:
 *   Input:  asteroids = [8,-8]
 *   Output: []
 *   Explanation: Same size → both explode.
 *
 * 📥 Example 3:
 *   Input:  asteroids = [10,2,-5]
 *   Output: [10]
 *   Explanation:
 *     - 2 and -5 collide → -5 survives
 *     - 10 and -5 collide → 10 survives
 *
 * 🚩 Topic:
 *   Array, Stack, Simulation
 ***************************************************************/

using System.Diagnostics;

namespace Week3_Stack_Assign3;

class AsteroidCollision_735
{
    static void Main(string[] args)
    {
        int[] steroidsCase1 = [5, 10, -5];
        int[] steroidsCase2 = [8, -8];
        int[] steroidsCase3 = [10, 2, -5];
        
        MeasureExecutionTime(() =>
        {
            var result1 = AsteroidCollision(steroidsCase1);
            Console.WriteLine($"Output: [{string.Join(", ", result1)}]");
        });
        
        var result2 = AsteroidCollision(steroidsCase2);
        Console.WriteLine($"Output: [{string.Join(", ", result2)}]");
        
        var result3 = AsteroidCollision(steroidsCase3);
        Console.WriteLine($"Output: [{string.Join(", ", result3)}]");
    }
    
    /// <summary>
    /// Returns the state of the asteroids after all collisions.
    /// </summary>
    /// <param name="asteroids">An array of integers representing asteroids.</param>
    /// <returns>The state of the asteroids after all collisions.</returns>
    private static int[] AsteroidCollision(int[] asteroids)
    {
        var stack = new Stack<int>();

        foreach (var currentAsteroid in asteroids)
        {
            // Flag to track if the current asteroid survives the collisions.
            var survived = true;

            // Collision condition: Stack is not empty, current asteroid is moving left (-), 
            // and the asteroid at the top of the stack is moving right (+).
            while (stack.Count > 0 && currentAsteroid < 0 && stack.Peek() > 0)
            {
                // The asteroid at the top of the stack.
                var lastAsteroid = stack.Peek();

                if (Math.Abs(currentAsteroid) > lastAsteroid)
                {
                    // Current asteroid is bigger, so the one on the stack explodes.
                    stack.Pop();
                    // The current asteroid survives, so it continues to check against the next asteroid on the stack.
                    continue; 
                }
                
                if (Math.Abs(currentAsteroid) == lastAsteroid)
                {
                    // If sizes are equal, both explode.
                    stack.Pop();
                    survived = false; // The current asteroid is also destroyed.
                }
                else // Math.Abs(currentAsteroid) < lastAsteroid
                {
                    // The asteroid on the stack is bigger, so the current asteroid is destroyed.
                    survived = false;
                }
                
                // If the current asteroid was destroyed, no need to check for more collisions.
                break;
            }

            // If the current asteroid survived all collisions, push it onto the stack.
            if (survived)
            {
                stack.Push(currentAsteroid);
            }
        }

        // The stack holds the result in reverse order, so we need to reverse it to get the correct final state.
        // e.g., Stack: [bottom -> 5, 10 -> top] becomes Array [10, 5]. After reversing, it becomes [5, 10].
        return stack.Reverse().ToArray();
    }
    
    private static void MeasureExecutionTime(Action action)
    {
        var stopwatch = Stopwatch.StartNew();
        action();
        stopwatch.Stop();
        Console.WriteLine($"Execution Time: {stopwatch.Elapsed.TotalMilliseconds} ms\n");
    }
}