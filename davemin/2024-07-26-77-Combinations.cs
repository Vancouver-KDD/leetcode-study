public class Solution {
    public IList<IList<int>> Combine(int n, int k) {
        IList<IList<int>> result = new List<IList<int>>();
        BackTrack(result, new List<int>(), n, k, 1);
        return result;
    }
    void BackTrack(IList<IList<int>> result, IList<int> tempList, int n, int k, int start)
    {
        if(tempList.Count == k)
        {            
            int[] array = new int[k];
            tempList.CopyTo(array, 0);
            Console.WriteLine(String.Concat(array));
            result.Add(array.ToList());
            return;
        }
        for(int i= start; i<=n; i++)
        {
            tempList.Add(i);
            BackTrack(result, tempList, n, k, i+1);
            tempList.RemoveAt(tempList.Count - 1);
        }
    }
}
