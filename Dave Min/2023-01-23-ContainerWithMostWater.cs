public class Solution
{
    public int MaxArea(int[] height)
    {
        int l = 0;
        int r = height.Length - 1;

        int max = 0;
        while (l < r)
        {
            int h = Math.Min(height[l], height[r]);
            max = Math.Max(max, (r - l) * h);

            // to hold the taller 
            if (height[l] <= height[r])
            {
                l++;
            }
            else
            {
                r--;
            }
        }
        return max;
    }
}