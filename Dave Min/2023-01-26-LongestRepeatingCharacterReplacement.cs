public class Solution
{
    public int CharacterReplacement(string s, int k)
    {
        int[] frequencyMap = new int[26];
        int l = 0; int r = 0; //left: l,  right: r.
        int maxFrequency = 0;
        int longestSubstringLen = 0;

        while (r < s.Length)
        {
            int idx = (int)s[r] - 'A';
            int window = r - l + 1;
            frequencyMap[idx]++;
            maxFrequency = Math.Max(maxFrequency, frequencyMap[idx]);
            //if window - max > k, then l should be moved one to the right
            if (window - maxFrequency > k)
            {
                frequencyMap[(int)s[l] - 'A']--;

                l++;
            }
            longestSubstringLen = r + 1 - l;
            r++;
        }
        return longestSubstringLen;
    }
}