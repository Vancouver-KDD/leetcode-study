var climbStairs = function(n) {
    if (n==0 || n==1){
        return 1;
    }
    var oneStep=1;
    var twoStep=2;
    
    for (var i=3; i<=n; i++){
        var temp = twoStep;
        twoStep = oneStep+twoStep;
        oneStep = temp;
    }
    
    return twoStep;
};
