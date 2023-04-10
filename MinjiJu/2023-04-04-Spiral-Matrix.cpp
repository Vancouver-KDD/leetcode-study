class Solution {
public:
    
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
        int m=matrix.size(), n=matrix[0].size();
        int top=0, bot=m-1, left=0, right=n-1;
        
        vector<int> res;
        int dir = 0;    // init direction left->right
        
        while(top<=bot && left<=right){
            
            // traverse left->right
            if(dir==0){
                for(int i=left; i<=right; i++){
                    res.push_back(matrix[top][i]);
                }
                top++;
            }
            // traverse top->bot
            else if(dir==1){
                for(int i=top; i<=bot; i++){
                    res.push_back(matrix[i][right]);
                }
                right--;
            }
            // traverse right->left
            else if(dir==2){
                for(int i=right; i>=left; i--){
                    res.push_back(matrix[bot][i]);
                }
                bot--;
            }
            // traverse bot->top
            else if(dir==3){
                for(int i=bot; i>=top; i--){
                    res.push_back(matrix[i][left]);
                }
                left++;
            }
            
            dir = (dir+1)%4;
        }
        return res;
    }
};