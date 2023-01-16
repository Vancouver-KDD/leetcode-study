//구현에 가깝나..?
import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int len = nums.length;
        if(len == 1) return nums;

        HashMap<Integer, Integer> map = new HashMap<>();
        for(int num : nums) {
            map.put(num, map.getOrDefault(num, 0)+1);
        }

        List<Integer> [] bucket = new List[len+1];
        for(Integer key: map.keySet()) {
            //특정 숫자에 해당하는 갯수
            int count = map.get(key);

            if(bucket[count] == null) {
                bucket[count] = new ArrayList<>();
            }
            bucket[count].add(key); //동일한 갯수를 가진 수 모으기
        }
        
        List<Integer> list = new ArrayList<>();
        for(int i = bucket.length -1 ;i>=0 && list.size() < k;i--) {
            if(bucket[i] == null) continue;
            list.addAll(bucket[i]);
        }
        int [] result = new int[k];
        for(int i = 0; i<k;i++) {
            result[i] = list.get(i);
        }
        return result;
    }

}