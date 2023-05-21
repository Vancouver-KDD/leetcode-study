
public class KthLargest {
    private PriorityQueue<int,int> prq;
    private int kth;
    public KthLargest(int k, int[] nums) {
        prq = new PriorityQueue<int,int>();
        kth=k;
        
        for(int i=0; i<nums.Length;i++){
            prq.Enqueue(nums[i],nums[i]);
        }
        while(prq !=null && prq.Count>kth){
            prq.Dequeue();
        }
    }
    
    public int Add(int val) {
        prq.Enqueue(val,val);
        if(prq.Count>kth)
        prq.Dequeue();
        return prq.Peek();
    }
}
 TC : Heapify O(N) + Removing N time O(N * log N) + Adding O(log N) +  Removing O(log N)  => O(N * log N)
 SC : O(N)
/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.Add(val);
 */
