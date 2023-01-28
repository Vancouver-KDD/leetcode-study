public class Solution
{
    public IList<IList<string>> GroupAnagrams(string[] strs)
    {
        Dictionary<string, IList<string>> dic = new Dictionary<string, IList<string>>();
        int[] alpharbet = new int[26];
        int idx;
        for (int i = 0; i < strs.Length; i++)
        {
            alpharbet = new int[26];
            for (int j = 0; j < strs[i].Length; j++)
            {
                idx = (int)(strs[i][j]) - 'a';
                alpharbet[idx] = alpharbet[idx] + 1;
            }

            if (dic.ContainsKey(string.Concat(alpharbet)))
            {
                dic[string.Concat(alpharbet)].Add(strs[i]);
            }
            else
            {
                IList<string> list = new List<string>();
                list.Add(strs[i]);
                dic.Add(string.Concat(alpharbet), list);
            }
        }

        IList<IList<string>> result = new List<IList<string>>();
        foreach (var d in dic)
        {
            result.Add(d.Value);
        }
        return result;

    }
}