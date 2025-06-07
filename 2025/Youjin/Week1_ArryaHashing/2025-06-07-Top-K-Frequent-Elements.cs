/***************************************************************
 * 🔷 LeetCode 347. Top K Frequent Elements                     
 *                                                              
 * 🟠 Difficulty: Medium                                        
 *                                                              
 * 📘 Problem:                                                  
 *   Given an integer array `nums` and an integer `k`,          
 *   return the `k` most frequent elements. You may return      
 *   the answer in any order.                                   
 *                                                              
 * 📥 Example 1:                                                
 *   Input:  nums = [1,1,1,2,2,3], k = 2                         
 *   Output: [1,2]                                               
 *                                                              
 * 📥 Example 2:                                                
 *   Input:  nums = [1], k = 1                                   
 *   Output: [1]                                                
 ***************************************************************/

using System.Diagnostics;

namespace Week1_ArrayHashing
{
    class TopKFrequentElements_347
    {
        static void Main(string[] args)
        {
            // Example test cases
            var num1 = new[] { 1, 1, 1, 2, 2, 3 };
            int[] num2 = [1];
            
            Console.WriteLine("[TopKFrequentElements_347]");

            // Answer_1
            MeasureExecutionTime(() => {
                Console.WriteLine("Answer 1:");
                var resultNum1 = Answer1_TopKFrequent(num1, 2); // Expected output: [1, 2]
                var resultNum2 = Answer1_TopKFrequent(num2, 1); // Expected output: [1]
                Console.WriteLine(string.Join(", ", resultNum1));
                Console.WriteLine(string.Join(", ", resultNum2));
            });

            // Answer_2
            MeasureExecutionTime(() =>
            {
                Console.WriteLine("Answer 2:");
                var resultNum3 = Answer2_TopKFrequent(num1, 2);
                var resultNum4 = Answer2_TopKFrequent(num2, 1);
                Console.WriteLine(string.Join(", ", resultNum3));
                Console.WriteLine(string.Join(", ", resultNum4));
            });
        }
        
        /********** Method to find the k most frequent elements in the array **********/
        static int[] Answer2_TopKFrequent(int[] nums, int k)
        {
            // Count frequencies
            var countMap = new Dictionary<int, int>();
            foreach (var num in nums)
                countMap[num] = countMap.GetValueOrDefault(num, 0) + 1;

            // Min-Heap to keep top k elements
            var minHeap = new PriorityQueue<int, int>(); // element = num, priority = frequency

            foreach (var entry in countMap)
            {
                minHeap.Enqueue(entry.Key, entry.Value); // frequency as priority
                if (minHeap.Count > k)
                    minHeap.Dequeue(); // remove smallest frequency
            }

            // Extract result
            var result = new int[k];
            for (var i = k - 1; i >= 0; i--)
                result[i] = minHeap.Dequeue();

            return result;
        }
        
        static int[] Answer1_TopKFrequent(int[] nums, int k)
        {
            // Dictionary to count the frequency of each element
            var frequentCountList = new Dictionary<int, int>();

            foreach (var item in nums)
            {
                // Increment count if exists, otherwise initialize to 1
                if (frequentCountList.ContainsKey(item))
                {
                    frequentCountList[item]++;
                }
                else
                {
                    frequentCountList[item] = 1;
                }
            }

            // Result array to store top k frequent elements
            var frequentElementList = new int[k];

            for (var i = 0; i < k; i++)
            {
                int maxKey = default;
                var maxCount = -1;

                // Find the element with the highest frequency
                foreach (var pair in frequentCountList)
                {
                    if (pair.Value > maxCount)
                    {
                        maxCount = pair.Value;
                        maxKey = pair.Key;
                    }
                }

                // Store the element and remove it from the dictionary to avoid reuse
                frequentElementList[i] = maxKey;
                frequentCountList.Remove(maxKey);
            }

            return frequentElementList;
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