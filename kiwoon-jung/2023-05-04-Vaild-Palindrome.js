var isPalindrome = function (s) {
  const x = s.replace(/[^0-9A-Z]+/gi, "").toLowerCase();
  const y = s
    .replace(/[^0-9A-Z]+/gi, "")
    .toLowerCase()
    .split("")
    .reverse()
    .join("");
  return x === y;
};
