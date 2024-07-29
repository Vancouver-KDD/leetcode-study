public class Solution {
    IList<IList<int>> res = new List<IList<int>>();
    public IList<IList<int>> Permute(int[] nums) {
        DoPermute(nums, 0, nums.Length -1);
        return res;
    }
    public void DoPermute(int[] nums, int l , int r) {
        if(l==r) {
            Console.WriteLine(String.Concat(nums));
            res.Add(nums.ToList());
        }
        else{
            for(int i=l;i<=r;i++){
                var arr = swap(nums, l ,i);           
                DoPermute(arr, l+1, r);   
            }
        }
    }
    public int[] swap(int[] nums, int x, int y){
        List<int> arr = new List<int>(nums.ToList());
        int tmp = 0;
        tmp = arr[x];
        arr[x] = arr[y];
        arr[y] = tmp;
        return arr.ToArray();
    }
}
