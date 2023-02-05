public class Solution
{
    public int[] TopKFrequent(int[] nums, int k)
    {

        Dictionary<int, int> dic = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            if (dic.ContainsKey(nums[i]))
            {
                dic[nums[i]]++;
            }
            else
            {
                dic.Add(nums[i], 1);
            }
        }

        PriorityQueue<int, int> priQueue = new PriorityQueue<int, int>();
        foreach (var v in dic)
        {
            priQueue.Enqueue(v.Key, v.Value);
        }
        int len = priQueue.Count;
        int[] result = new int[k];
        int j = 0; int idx = 0;

        while (priQueue.TryDequeue(out int kkey, out int vvalu))
        {
            if (j >= len - k)
                result[idx++] = kkey;
            j++;
        }
        return result;
    }
}