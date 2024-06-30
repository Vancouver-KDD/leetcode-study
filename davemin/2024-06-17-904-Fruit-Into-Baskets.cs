public class Solution {
    public int TotalFruit(int[] fruits) {
        // 1,2,3,4,5,4 
        Dictionary<int,int> dic = new Dictionary<int,int>();
        int l=0,r=0, sum=0;
        
        while(r<fruits.Length){
            if(dic.ContainsKey(fruits[r]))
                dic[fruits[r]]++;
            else{
                dic[fruits[r]]=1;
                while(dic.Count>2){
                    dic[fruits[l]]--;
                    if(dic[fruits[l]]==0)
                        dic.Remove(fruits[l]);
                    l++;    
                }
            }            
            sum = Math.Max(sum,r-l+1);
            r++;
        }
        return sum;
    }
}
