var combine = function(n, k) {
    let result = [];
    let combination = [];

//will generate all possible combinations of size k from the numbers starting from start up to n
    function backtrack(start) {
        if (combination.length === k) {
            result.push([...combination])
            return;
        }

        for (let i = start; i <= n; i++){
            //add it to the current comb list to form the combination
            combination.push(i);
            //ensures that each number can only be used once in each combination, avoiding duplicate combinations
            backtrack(i + 1);
            //backtrack and try other numbers for the current position in the combination
            combination.pop();
        }
    }
//we want to start forming combinations with the numbers from 1 to n
    backtrack(1);

    return result;
};