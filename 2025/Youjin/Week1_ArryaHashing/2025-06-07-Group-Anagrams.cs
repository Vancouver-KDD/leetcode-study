/***************************************************************
 * 🔷 LeetCode 49. Group Anagrams
 *
 * 🟠 Difficulty: Medium
 *
 * 📘 Problem:
 *   Given an array of strings `strs`, group the anagrams
 *   together. You can return the answer in any order.
 *
 * ✨ Definition:
 *   An anagram is a word formed by rearranging the letters
 *   of another word.
 *
 * 📥 Example 1:
 *   Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
 *   Output: [["bat"], ["nat","tan"], ["ate","eat","tea"]]
 *
 * 📥 Example 2:
 *   Input:  [""]
 *   Output: [[""]]
 *
 * 📥 Example 3:
 *   Input:  ["a"]
 *   Output: [["a"]]
 ***************************************************************/

using System.Diagnostics;

namespace Week1_ArrayHashing
{
    class GroupAnagrams_49
    {
        static void Main(string[] args)
        {
            var strs1 = new[] { "eat", "tea", "tan", "ate", "nat", "bat" };
            var strs2 = new[] { " " };
            var strs3 = new[] { "a" };

            Console.WriteLine("[GroupAnagrams_49]");
            
            // Answer_1
            Console.WriteLine("Answer 1:");
            MeasureExecutionTime(() =>
            {
                var resultAnswer1 = Answer1_GroupAnagrams(strs1);
                var resultAnswer2 = Answer1_GroupAnagrams(strs2);
                var resultAnswer3 = Answer1_GroupAnagrams(strs3);
                PrintResult(resultAnswer1);
                PrintResult(resultAnswer2);
                PrintResult(resultAnswer3);
            });

            // Answer_2
            Console.WriteLine("Answer 2:");
            MeasureExecutionTime(() =>
            {
                var resultAnswer1 = Answer2_GroupAnagrams(strs1);
                var resultAnswer2 = Answer2_GroupAnagrams(strs2);
                var resultAnswer3 = Answer2_GroupAnagrams(strs3);
                PrintResult(resultAnswer1);
                PrintResult(resultAnswer2);
                PrintResult(resultAnswer3);
            });
        }

        static IList<IList<string>> Answer2_GroupAnagrams(string[] strs)
        {
            var map = new Dictionary<string, List<string>>();

            foreach (var str in strs)
            {
                // Sort the string to use as key
                var chars = str.ToCharArray();
                Array.Sort(chars);
                var key = new string(chars);

                // TryGetValue is slightly faster and cleaner than ContainsKey
                if (map.TryGetValue(key, out var group) == false)
                {
                    group = new List<string>();
                    map[key] = group;
                }

                group.Add(str);
            }

            // Convert Dictionary values to List<IList<string>>
            var result = new List<IList<string>>();
            foreach (var group in map.Values)
            {
                result.Add(group);
            }

            return result;
        }

        static IList<IList<string>> Answer1_GroupAnagrams(string[] strs) 
        {
            var map = new Dictionary<string, List<string>>();

            foreach (var word in strs)
            {
                // Sort the string to use as key
                var charArray  = word.ToCharArray();
                Array.Sort(charArray);
                var sorted = new string(charArray); // e.g., "eat" → "aet"

                // Group words by sorted string
                if (map.ContainsKey(sorted) == false)
                {
                    map[sorted] = new List<string>();
                }

                map[sorted].Add(word);
            }

            // Convert Dictionary values to List<IList<string>>
            var result = new List<IList<string>>();
            foreach (var group in map.Values)
            {
                result.Add(group);
            }

            return result;
        }
        
        private static void PrintResult(IList<IList<string>> groups)
        {
            foreach (var group in groups)
            {
                Console.Write("[");
                Console.Write(string.Join(", ", group));
                Console.WriteLine("]");
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
}