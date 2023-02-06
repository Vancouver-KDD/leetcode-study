public class Solution
{
    public int Search(int[] nums, int target)
    {
        if (nums.Length == 1)
            return nums[0] == target ? 0 : -1;
        int l = 0, r = nums.Length - 1;
        int startingPoint = 0;

        if (nums[0] < nums[nums.Length - 1])
        {
            var idx = nums.ToList().BinarySearch(target);
            return idx < 0 ? -1 : idx;
        }
        while (l <= r)
        {
            int mid = l + (r - l) / 2;
            if (nums[mid - 1] > nums[mid])
            {
                startingPoint = mid; break;
            }
            if (nums[mid] > nums[mid + 1])
            {
                startingPoint = mid + 1; break;
            }

            if (nums[0] < nums[mid])
            {
                l = mid + 1;
            }
            else
            {
                r = mid - 1;
            }
        }

        Console.WriteLine(startingPoint);
        if (nums[startingPoint] == target)
            return startingPoint;
        else if (nums[startingPoint] < target)
        {
            var list = nums.ToList().GetRange(startingPoint, nums.Length - startingPoint);
            var idx = list.BinarySearch(target);
            return idx < 0 ? -1 : startingPoint + idx;
        }
        else
        {
            var list = nums.ToList().GetRange(0, startingPoint);
            var idx = list.BinarySearch(target);
            return idx < 0 ? -1 : startingPoint + idx;
        }
    }
}