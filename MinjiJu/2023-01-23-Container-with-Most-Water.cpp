class Solution {
public:
    int maxArea(vector<int>& height) {
        // let height h(0) h(1) ... h(i) h(i+1) h(i+2) ... h(j-2) h(j-1) h(j) ... h(n-1) h(n)
        // then area = (j-i)*min(h(i),h(j))
        // if h(i)<h(j) => advance i => i++
        // if h(j)<h(i) => advance j => j--
        
        int i=0, j=height.size()-1;
        int area=0, maxarea=0;
        
        while(i<j){
            area = (j-i)*min(height[i],height[j]);
            if(height[i]<height[j]) i++;
            else j--;
            maxarea = max(maxarea,area);
        }
        return maxarea;
    }
};

