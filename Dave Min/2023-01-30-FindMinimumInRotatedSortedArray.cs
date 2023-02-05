public class Solution
{
    public int FindMin(int[] nums)
    {
        if (nums.Length == 1) return nums[0];
        if (nums[0] < nums[nums.Length - 1]) return nums[0];

        //Console.WriteLine(string.Concat(nums));
        return BinarySearchMinOfRotatedSortedArray(0, nums.Length - 1, nums);
    }

    public int BinarySearchMinOfRotatedSortedArray(int x, int y, int[] nums)
    {
        if (x > y) return -1;
        int mid = x + (y - x) / 2;

        if (nums[mid] > nums[mid + 1]) return nums[mid + 1];
        if (nums[mid] < nums[mid - 1]) return nums[mid];

        if (nums[0] < nums[mid])
        {
            return BinarySearchMinOfRotatedSortedArray(mid + 1, y, nums);
        }
        else
        {
            return BinarySearchMinOfRotatedSortedArray(x, mid - 1, nums);
        }
    }
}

