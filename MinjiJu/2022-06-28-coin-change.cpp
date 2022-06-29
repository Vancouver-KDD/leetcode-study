// failed solution
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        
        if(amount==0) return 0;
        
        sort(coins.begin(),coins.end());
        int count = 0, temp=0, denom=coins.size()-1;
        
        while(amount>0 && denom>=0){
            temp = amount/coins[denom];
            amount%=coins[denom];
            
            count+=temp;
            denom--;
            
            if(amount==0) return count;
        }
        
        return -1;
    }
};