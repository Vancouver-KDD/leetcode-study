var combinationSum = function(candidates, target){
  const result = [];
  const sumOfNums = [];

  const dfs = (sum, startIdx) =>{
    if(sum > target) return;
    if(sum === target) {
      result.push([...sumOfNums])
    }else{
      for (let i = startIdx; i < candidates.length; i++){
        sumOfNums.push(candidates[i]);
        dfs(sum + candidates[i], i);
        sumOfNums.pop();
      }
    }
  }
  dfs(0,0);
  return result;
}