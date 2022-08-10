function isValid(s){
  if(s.length === 0) return true;
  if(s.length % 2 !== 0) return false;

  let bracket = {
    '(' : ')',
    '[' : ']',
    '{' : '}'
  }

  let stack = [];

  for(let char of s){
    // if the bracket has opening bracket
    if(bracket[char]){
      // push the closing bracket
      stack.push(bracket[char])
    } else{
      // if we have closing bracket, pop it
      // and if the pop value is not same with char it means not matching
      if(stack.pop() != char) return false;
    }
  }
  // chek if the stack is empty or not
  return stack.length === 0
}