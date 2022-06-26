class Solution {
    public int[] countBits(int n) {
    int[] arr = new int[n+1];
    arr[0] = 0;
     for (int i=1; i<=n; i++){
         int sum = 0;
         int value = i;
         while(value != 0){
             sum += value%2;
             value /= 2;
         }
         arr[i] = sum;
     }
    return arr;
    }
}
