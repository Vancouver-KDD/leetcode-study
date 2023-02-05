// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
// Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

var maxArea = function(height) {
    let area=0; i=0, j=height.length-1;
    while(i<j) {
        const temp=(j-i)*Math.min(height[i],height[j])
        area=Math.max(area,temp)
        if(height[i]>height[j]) {
            j-=1;
        } else{
            i+=1;
        }
    }
    return area;
}
// space 0(1)
// time 0(n)