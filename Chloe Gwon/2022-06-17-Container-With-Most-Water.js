var maxArea = function(height) {
    //O(n)
    
    var result = 0;
    var r = height.length - 1;
    var l = 0;
    
    while (l < r){
        var area = (r-l) * Math.min(height[l], height[r]);
        if (height[l] < height[r]){
            l++;
        } else {
            r--;
        }
        result = Math.max(area, result);
    }
    
    return result;
};
