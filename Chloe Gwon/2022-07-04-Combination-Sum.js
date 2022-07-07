/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const result = [];
    
    const dfs = (startIndex, sum, comb) => {
        if (sum === target) {
            result.push([...comb]);
        }
        
        for (let i = startIndex; i < candidates.length; i++) {
            const nextSum = sum + candidates[i];
            
            if (nextSum <= target) {
                comb.push(candidates[i]);
                dfs(i, sum+candidates[i], comb);
                comb.pop();
            }
        }
        
    }
        
    dfs(0, 0, []);

    return result;
};


