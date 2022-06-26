class Solution {
    public int[] countBits(int n) {
        int[] output = new int[n+1];
        for(int i = 0; i<n+1; i++) {
            String str = Integer.toBinaryString(i);
            int count = 0;
            for(int j=0; j<str.length(); j++) {
                if(str.charAt(j) == '1') {
                    count++;
                }
            }
            output[i] = count;
        }
        return output;
    }
}