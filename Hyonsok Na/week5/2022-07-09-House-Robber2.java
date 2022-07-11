class Solution {
    public int rob(int[] array) {
        
         if(array.length == 0) return 0;
        if(array.length == 1) return array[0];
        
        int first = Math.max(array[0], array[1]);
        int second = array[0];
        
        for(int i=2;i<array.length-1;i++){
            int MaxValue = Math.max(first, second + array[i]);
            second = first;
            first = MaxValue;
        }
        int secondValue = Integer.MIN_VALUE;
        
        if(array.length > 2)
        {
            int first1 = Math.max(array[1], array[2]);
        int second1 = array[1];
        
        for(int i=3;i<array.length;i++){
            int MaxValue = Math.max(first1, second1 + array[i]);
            second1 = first1;
            first1 = MaxValue;
        }
            secondValue = first1;
        }
        
        return secondValue == Integer.MAX_VALUE ? first : Math.max(first, secondValue);
    }
}
