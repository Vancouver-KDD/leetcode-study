//XOR로 풀 수 없는지 다시 생각해보기
import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i : nums) { // -> O(N)
            if(map.containsKey(i)) { //->generally, o(1) , but in worst case, o(N)
                return true;
            }else {
                map.put(i, 1);
            }
        }
        return false;
    }
}
