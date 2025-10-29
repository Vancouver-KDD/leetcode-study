function maxArea(height: number[]): number {
    let right=height.length-1;
    let left = 0;
    let maxArea=0;
    while(left<right){    

        let minHeight = Math.min(height[left],height[right]);
        let area = (right-left)*minHeight;
        maxArea = Math.max(maxArea,area);

        if(height[left]<height[right])left++;
        else if(height[left]>height[right])right--;   
        else {
            left++;
            right--;
        } 
    }   

    return maxArea;
};

/**
1. idea
 - L,R두개의 포인터
 - 너비는 어쩌피 R-L
 - 높이만 고려하면 되는데, 높이는 항상 작은쪽으로 계산이 되므로 계속 큰값을 찾는거야
  */