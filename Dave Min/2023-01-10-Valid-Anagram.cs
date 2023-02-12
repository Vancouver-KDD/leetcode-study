public class Solution
{
    public bool IsAnagram(string s, string t)
    {
        if (s == null || t == null) return false;

        int Len = s.Length;
        if (Len != t.Length) return false;

        int[] AlphabetArray = new int[26];

        for (int i = 0; i < Len; i++)
        {
            AlphabetArray[(int)s[i] - (int)'a']++;
            AlphabetArray[(int)t[i] - (int)'a']--;
        }

        for (int i = 0; i < 26; i++)
        {
            if (AlphabetArray[i] != 0)
                return false;
        }

        return true;
    }
}