//limitation: height is null or size is zero, -> return ???? 
// Input: height = [1,8,6,2,5,4,8,3,7] -> Output: 49
// Input: height = [1,1] -> Output: 1

//2023-01-23
//Time Complexity: O(N)
//Space Complexity: O(1)
class Solution{
    public int maxArea(int[] height){
        if(height == null || height.length == 0){
            return 0;
        }

        int maxWater = 0;
        int start = 0;
        int end = height.length -1;
        
        //                  0 1 2 3 4 5 6 7 8
        // Input: height = [1,8,6,2,5,4,8,3,7]
        // {1,7}:8*1=8 -> (8,7):7*7=49 -> (8,3):6*3=18 -> (8,8):5*8=40 ->(8,4):4*4=16 -> 
        //              (8,5):3*5=15 -> (8,2):2*2-4  -> (8,6):1*6=6
        while(start < end){
            int length = Math.min(height[start], height[end]);
            int width = end - start;
            int area = length * width;
            maxWater = Math.max(maxWater, area);

            if(height[start] < height[end]){
                start++;
            }else{
                end--;
            }
        }
        return maxWater;
    }
}
//2022-12-03
//Time Complexity: O(N), Space Complexity: O(1)
/*
class Solution{
    public int maxArea(int[] height){
        if(height == null || height.length == 0){
            return 0;
        }

        int start = 0;
        int end = height.length -1;
        int max = 0;
        while(start < end){
            int width = end - start;
            int minHeight = Math.min(height[start], height[end]);
            max = Math.max(max, width * minHeight);
            if(height[start] <= height[end]){
                start++;
            }else{
                end--;
            }
        }

        return max;
    }
}
*/
//2022-09-25
// Time Complexity: O(N) , Space Complexity: O(1) 
/*
class Solution{
    public int maxArea(int[] height){
        
        if(height == null || height.length == 0){
            return 0;
        }
        
        int start = 0; 
        int end = height.length -1;
        int maxAmount = 0;
        
        // 0 1 2 3 4 5 6 7 8
        //[1,8,6,2,5,4,8,3,7]
        //s:0, e:8  a:8 * 1 = 8  ma:8
        //s:1, e:8, a:7* 7 = 49, max: 49
        //s:1, e:7, a:6*3 = 24, ma:49
        //s:1, e:6  a:5*8 = 40, max:49
        //s:2, e:6 ,a:4*6 = 24, max:49
        //s:3, e:6, a:3*2 = 6, max: 49
        //s:4, e:6, a:2*5 = 10,max: 49
        //s:5, e:6  
        //s:6, e:6
        while(start < end){
            int amount = (end -start) * Math.min(height[start], height[end]);
            maxAmount = Math.max(amount, maxAmount);
            
            if(height[start] <= height[end]){
                //try to find longer height than current start height
                start++;
            }else{
                //try to find longer height than current end height
                end--;
            }
        }
        
        return maxAmount;
    }
}
*/
//2022-09-24
/*
class Solution{
    public int maxArea(int[] height){
        
        if(height == null || height.length == 0){
            return 0;
        }
        
        int start = 0;
        int end = height.length - 1;
        int maxAmount = 0; 
        
        while(start < end){
            int curAmount = (end - start) * Math.min(height[start], height[end]);
            maxAmount = Math.max(maxAmount, curAmount);
            
            if(height[start] < height[end]){                
                start++;
            }else{
                end--;
            }
        }
        
        return maxAmount;
    }
}
*/
//2022-09-07
/*
class Solution {
    public int maxArea(int[] height) {
        
        if(height == null || height.length == 0){
            return 0;
        }
        
        int leftX = 0;
        int rightX = height.length -1;
        int maximumArea = 0;
        
        while(leftX < rightX){
                        
            maximumArea = Math.max(maximumArea, (rightX - leftX) * Math.min(height[leftX], height[rightX]));
        
            if(height[leftX] <= height[rightX]){
                
                leftX++;
                // 여기서는 while 문을 넣는것이 이득이 없음. 원래 위 계산 자체가 단순하기때문. 아래 while 문을 넣은게 코드만 더 복잡해짐.  
                //while( (leftX < rightX) && height[leftX] < height[leftX-1]){ //find bigger height[leftX] 
                //   leftX++;
                //}
                
            }else{ //height[leftX] > height[rightX]
                
                rightX--;
                // 여기서는 while 문을 넣는것이 이득이 없음. 원래 위 계산 자체가 단순하기때문. 아래 while 문을 넣은게 코드만 더 복잡해짐. 
                //while( (leftX < rightX) && height[rightX] < height[rightX+1]){ //find bigger height[rightX] 
                //    rightX--;
                //}
            }

        }
        
        return maximumArea;
    }
}
*/
/*
class Solution {
    public int maxArea(int[] height) {
        
        if(height == null || height.length == 0){
            return 0;
        }
        
        int leftX = 0;
        int rightX = height.length -1;
        int maximumArea = 0;
        int currentArea = 0; 
        int length = 0;
        
        while(leftX < rightX){
                        
            //int currentArea = (rightX - leftX) * (Math.min(height[leftX], height[rightX]));
            //maximumArea = ( currentArea > maximumArea) ? currentArea : maximumArea;
            length = rightX - leftX;
            
            if(height[leftX] <= height[rightX]){
                
                currentArea = length * height[leftX];                
                
                leftX++;
                //while( (leftX < rightX) && height[leftX] < height[leftX-1]){ //find bigger height[leftX] 
                //   leftX++;
                //}
                
            }else{ //height[leftX] > height[rightX]
                
                currentArea = length * height[rightX]; 
                
                rightX--;
                //while( (leftX < rightX) && height[rightX] < height[rightX+1]){ //find bigger height[rightX] 
                //    rightX--;
                //}
            }
            
            maximumArea = ( currentArea > maximumArea) ? currentArea : maximumArea;
        }
        
        return maximumArea;
    }
}
*/