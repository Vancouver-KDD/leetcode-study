var isValid = function (s) {
  let stack = [];
  //boudnary check
  if (
    s[0] === "}" ||
    s[0] === ")" ||
    s[0] === "]" ||
    s[s.length] === "{" ||
    s[s.length] === "[" ||
    s[s.length] === "("
  ) {
    return false;
  }
  /*
        Method1: iterate the string and store character if finds opening bracket
        if closing bracket found check if 'stack' array has opening bracket of current closing bracket
        if passes all conditions remove that openning bracket from 'stack' array

        if 'stack' array results nothing containing means it is a valid pantheses so return true
  */
  for (let i in s) {
    if (s[i] === "}" || s[i] === ")" || s[i] === "]") {
      if (s[i] === "}" && stack.includes("{")) {
        if (stack.lastIndexOf("{") === stack.length - 1)
          stack.splice(stack.lastIndexOf("{"), 1);
        else return false;
      } else if (s[i] === "]" && stack.includes("[")) {
        if (stack.lastIndexOf("[") === stack.length - 1)
          stack.splice(stack.lastIndexOf("["), 1);
        else return false;
      } else if (s[i] === ")" && stack.includes("(")) {
        if (stack.lastIndexOf("(") === stack.length - 1)
          stack.splice(stack.lastIndexOf("("), 1);
        else return false;
      } else return false;
    } else {
      stack.push(s[i]);
    }
  }
  console.log(stack);
  if (stack.length === 0) return true;
  else return false;
};

/*

    for (let i = 0; i < s.length; i++) {
        console.log(s.charCodeAt(i + 1) - s.charCodeAt(i))
        if (s.charCodeAt(i + 1) - s.charCodeAt(i) === 1 || s.charCodeAt(i + 1) - s.charCodeAt(i) === 2) {
        } else {
            return false;
        }
        i++
    }
    return true

*/
