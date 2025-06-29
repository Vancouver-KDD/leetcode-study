function isValid(s: string): boolean {
  const leftRegex = /[\(\{\[]/;
  const pair = { "(": ")", "[": "]", "{": "}" };
  const lookup: string[] = [];

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (leftRegex.test(char)) {
      lookup.push(char);
    } else {
      const left = lookup.pop()!;
      if (pair[left] !== char) return false;
    }
  }

  return lookup.length ? false : true;
}
