var climbStairs = function(n) {
    let arr = new Array(n+1);

    arr[1] = 1, arr[2] = 2;
    for(let i=0; i<=n; i++){
        arr[i] = arr[i-1] + arr[i-2];
    } 

    return arr[n];
};

//Dynamic Programming : TC O(n)
// SC O(n) -> New array