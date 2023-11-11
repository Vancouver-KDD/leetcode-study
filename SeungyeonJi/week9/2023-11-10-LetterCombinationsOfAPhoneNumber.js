let letterCombinations = function (digits) {
  let result = [];

  //alpha has map
  const alpha = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
  };

  const dfs = function (i, digits, state) {
    // base case (condition to sotp this recursive function)

    // If we loop through digits.length time, we will return the result;
    if (i === digits.length) {
      result.push(slate.join(""));
      return;
    }

    //dfs recursive case
    let chars = alpha[digits[i]];

    for (let char of chars) {
      state.push(char);
      dfs(i + 1, digits, state);
      state.pop();
    }
  };

  dfs(0, digits, []);

  return result;
};
