public class Solution {
    public bool IsHappy(int n) {
        HashSet<int> seen = new HashSet<int>();
        while(n >1){
            n = DivideAndAddup(n); 
            if(!seen.Contains(n)) seen.Add(n);
            else break;           
        }        
        return n==1? true:false;
    }

    public int DivideAndAddup(int n) {
        int sum = 0;
        while(n>0){
          int digit =  n%10;
          sum+= (int)Math.Pow(digit,2);
          n/=10;
        }
        return sum;
    }   
}
