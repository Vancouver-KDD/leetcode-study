public class Solution
{
    public IList<IList<int>> ThreeSum(int[] nums)
    {
        Array.Sort(nums);
        HashSet<int> hset = new HashSet<int>();
        for (int i = 0; i < nums.Length; i++)
        {
            if (!hset.Contains(nums[i])) hset.Add(nums[i]);
        }

        HashSet<string> duplChecker = new HashSet<string>();
        IList<IList<int>> resultList = new List<IList<int>>();
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] > 0) break;

            for (int j = i + 1; j < nums.Length; j++)
            {
                if (0 - (nums[j] + nums[i]) < nums[j]) continue;
                if (hset.Contains(0 - (nums[j] + nums[i])))
                {
                    var result = new List<int>() { nums[i], nums[j], 0 - (nums[j] + nums[i]) };
                    if (!duplChecker.Contains(string.Concat(result)))
                    {
                        duplChecker.Add(string.Concat(result));
                        resultList.Add(result);
                    }
                }
            }
        }
        return resultList;
    }
}