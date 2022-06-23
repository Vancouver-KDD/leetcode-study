// the naive approach
// iterate through each value and count number of 1s
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> res;
        
        for(int i=0; i<=n; i++){
            int count = 0;  // count number of 1s
            int val = i;    // current value
            
            while(val!=0){
                count+=val%2;
                val/=2;
            }
            res.push_back(count);
        }
        return res;
    }
};