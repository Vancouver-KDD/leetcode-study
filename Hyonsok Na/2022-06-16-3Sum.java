// couldn't solve
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> output = new ArrayList();
        List<Integer> listPo = new ArrayList();
        List<Integer> listNe = new ArrayList();
        HashMap<Integer, Integer> map = new HashMap();
        
        //base case
        if(nums.length ==0) return output;
        if(nums.length ==1 && nums[0] ==0) return output;
        
        //add all elements into hashmap
        for(int i =0; i<nums.length; i++) {
            map.put(i, nums[i]);
        }
        
        //split elements by sign
        for(int num: nums) {
            if(num >= 0) listPo.add(num);
            else listNe.add(num);
        }
        
        for(int i=0; i<nums.length; i++) {
            int val = nums[i];
            if(val < 0) {
                for(int j = 0; j<listPo.size(); j++) {
                    List<Integer> tempList = new ArrayList();
                    int twoSum = -1*(val+listPo.get(j));
                    tempList.add(listPo.get(j));
                    tempList.add(val);
                    if(map.containsValue(twoSum)) {
                        tempList.add(twoSum);
                        Collections.sort(tempList);
                        if(!output.contains(tempList)) {
                            output.add(tempList);
                        }
                    } 
                }
            } else {
                for(int j = 0; j<listNe.size(); j++) {
                    List<Integer> tempList = new ArrayList();
                    int twoSum = -1*(val+listNe.get(j));
                    tempList.add(val);
                    tempList.add(listNe.get(j));
                    if(map.containsValue(twoSum)) {
                        tempList.add(twoSum);
                        Collections.sort(tempList);
                        if(!output.contains(tempList)) {
                            output.add(tempList);
                        }
                    } 
                }
            }
        }
        return output;
    }
}

// from reference 
class Solution {
    public List < List < Integer >> threeSum(int[] nums) {
        // Sort the given array
        Arrays.sort(nums);

        List < List < Integer >> result = new ArrayList < > ();
        for (int num1Idx = 0; num1Idx + 2 < nums.length; num1Idx++) {
            // Skip all duplicates from left
            // num1Idx>0 ensures this check is made only from 2nd element onwards
            if (num1Idx > 0 && nums[num1Idx] == nums[num1Idx - 1]) {
                continue;
            }

            int num2Idx = num1Idx + 1;
            int num3Idx = nums.length - 1;
            while (num2Idx < num3Idx) {
                int sum = nums[num2Idx] + nums[num3Idx] + nums[num1Idx];
                if (sum == 0) {
                    // Add triplet to result
                    result.add(Arrays.asList(nums[num1Idx], nums[num2Idx], nums[num3Idx]));

                    num3Idx--;

                    // Skip all duplicates from right
                    while (num2Idx < num3Idx && nums[num3Idx] == nums[num3Idx + 1]) num3Idx--;
                } else if (sum > 0) {
                    // Decrement num3Idx to reduce sum value
                    num3Idx--;
                } else {
                    // Increment num2Idx to increase sum value
                    num2Idx++;
                }
            }
        }
        return result;
    }
}
