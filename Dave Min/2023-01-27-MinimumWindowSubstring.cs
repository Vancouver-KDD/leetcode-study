public class Solution
{
    public string MinWindow(string s, string t)
    {
        if (s.Length < t.Length) return "";
        if (s.Length == 1 && t.Length == 1 && s[0] == t[0]) return t;
        Dictionary<char, int> tMap = new Dictionary<char, int>();
        Dictionary<char, int> sMap = new Dictionary<char, int>();
        string result = null;
        for (int i = 0; i < t.Length; i++)
        {
            if (tMap.ContainsKey(t[i]))
            {
                tMap[t[i]]++;
            }
            else
            {
                tMap.Add(t[i], 1);
            }
        }

        int l = 0, r = 0;
        while (r < s.Length)
        {
            Console.WriteLine();
            Console.WriteLine(s.Substring(l, r - l + 1));
            char c = s[r];
            if (sMap.ContainsKey(c))
            {
                sMap[c]++;
            }
            else
            {
                sMap.Add(c, 1);
            }
            if (r < t.Length)
            {
                r++; continue;
            }
            bool res = CompareToTMap(tMap, sMap);
            while (res && r - t.Length >= l)
            {
                Console.WriteLine(res);
                string str = s.Substring(l, r - l + 1);
                if (result == null)
                    result = str;
                else
                    result = str.Length < result.Length ? str : result;

                sMap[s[l]]--;
                l++;
                res = CompareToTMap(tMap, sMap);
            }
            r++;
        }
        return result;
    }

    public bool CompareToTMap(Dictionary<char, int> tMap, Dictionary<char, int> sMap)
    {
        foreach (var kvp in tMap)
        {
            //Console.WriteLine("CompareToTMap Key: " + kvp.Key + "| Value: " + kvp.Value);
            if (!sMap.ContainsKey(kvp.Key))
            {
                return false;
            }
            else
            {
                if (kvp.Value > sMap[kvp.Key])
                    return false;
            }
        }
        return true;
    }
}