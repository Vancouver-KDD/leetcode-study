// using even or odd number
var countBits = function(n) {
  let result = [0];
  if(n === 0) return result;

  for(let i = 1; i < n + 1; i++){
    if(i % 2 === 0){ // even number
      result[i] = result[i/2];
    } else{ // odd number
      result[i] = result[i - 1] + 1;
    }
  }
  return result;
};

// using dp
var countBits2 = function(n) {
  let dp = Array(n + 1).fill(0);
  let offset = 1;

  for(let i = 1; i < n + 1; i++){
    if(offset * 2 === i) {
      offset = i;
    }
    dp[i] = 1 + dp[i - offset];
  }
  return dp;
}