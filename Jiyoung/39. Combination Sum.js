var combinationSum = function(candidates, target) {
    const result = [];
    const path = [];
    candidates.sort((a, b) => a - b);
    backtrack(candidates, 0, target, path, result);
    return result;
};

function backtrack(candidates, start, target, path, result) {
    if (target === 0) {
        result.push([...path]);
        return;
    }
    if (target < 0) {
        return;
    }
    for (let i = start; i < candidates.length; i++) {
        path.push(candidates[i]);
        backtrack(candidates, i, target - candidates[i], path, result);
        path.pop();
    }
}
