
class Solution {
    public int[] plusOne(int[] digits) {
        int Carry =1;
        int allNineChecker = 0;
        for(int i= digits.length -1; i>= 0; i--){
            int sum = Carry + digits[i];
            if(sum==10){
                digits[i] =0;
                Carry =1;                
            }else{
                digits[i] =sum;
                Carry =0;
            }
            allNineChecker += digits[i];
        }
        if(allNineChecker==0 && Carry ==1)
        {
          digits = new int[digits.length+1];
          digits[0]=1;
        }
        return digits; 
    }
}
