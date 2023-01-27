/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    for (const ch of s) {
        const isParenthesis = ch === '(';
        if (isParenthesis) stack.push(')');
        const isCurly = ch === '{';
        if (isCurly) stack.push('}');
        const isSquare = ch === '[';
        if (isSquare) stack.push(']');

        if (isParenthesis || isCurly || isSquare) continue;
        
        const isEmpty = !stack.length; // if length of stack is 0, then isEmpty will be true
        const isWrongFair = stack.pop() !== ch;
        if (isEmpty || isWrongFair) return false;
    }
    return !stack.length;
};