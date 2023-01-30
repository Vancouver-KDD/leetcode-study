public class Solution
{
    //shorter runtime because of the constant factor compared to using HashSet/HashMap.
    public int LengthOfLongestSubstring(string s)
    {
        int[] table = new int[128];
        //moving window; l -> left pointer /  r -> right pointer
        int max = 0, idx = 0, l = 0, r = 0;
        for (int k = 0; k < 128; k++) table[k] = -1;

        while (r < s.Length)
        {
            int numChar = (int)s[r];
            idx = table[numChar];

            if (idx != -1 && idx >= l && idx < r)
                l = idx + 1;

            table[numChar] = r;
            max = Math.Max(max, r - l + 1);
            r++;
        }
        return max;
    }
}

//If we know that the charset is rather small, 
//we can mimic what a HashSet/HashMap does with a boolean/integer array as direct access table.
//Though the time complexity of query or insertion is still O(1)O(1)O(1),
//the constant factor is smaller in an array than in a HashMap/HashSet.
//Thus, we can achieve a shorter runtime by the replacement here.

public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        if (s.Length == 1) return 1;

        //moving window; 
        //l -> left pointer /  r -> right pointer
        int l = 0; int r = 0;
        Dictionary<char, int> dic = new Dictionary<char, int>();
        int max = 0;

        while (r < s.Length)
        {
            if (dic.ContainsKey(s[r]))
            {
                if (dic[s[r]] >= l)
                    l = ++dic[s[r]];
                dic[s[r]] = r;
            }
            else
            {
                dic.Add(s[r], r);
            }
            max = Math.Max(max, r - l + 1);
            //Console.WriteLine($"s[r]:{s[r]} r:{r} l:{l}  max:{max}");
            r++;
        }
        return max;
    }
}

