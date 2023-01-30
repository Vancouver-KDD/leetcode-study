public class Solution
{
    public int LongestConsecutive(int[] nums)
    {
        if (nums.Length == 0) return 0;
        PriorityQueue<int, int> priQue = new PriorityQueue<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            priQue.Enqueue(nums[i], nums[i]);
        }

        int max = 0; int pre = -1000000000; int cnt = 0;
        while (priQue.TryDequeue(out int item, out int num))
        {
            if (pre == -1000000000)
            {
                pre = num; continue;
            }

            if (num - pre == 1) cnt++;
            else if (num - pre > 1) cnt = 0;

            max = Math.Max(max, cnt);
            pre = num;
        }
        return max + 1;
    }
}