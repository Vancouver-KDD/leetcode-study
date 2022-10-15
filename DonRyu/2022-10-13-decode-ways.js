const numDecodings = (s) => {
    if (s[0] === '0' ) return 0

    const howManyDecodes = Array(s.length+1).fill(0)
    howManyDecodes[0] = 1
    howManyDecodes[1] = 1

    for (let i = 2; i <= s.length; i++) {
      const single = s.slice(i-1, i);
      const double = s.slice(i-2, i);

      if (single > 0) howManyDecodes[i] = howManyDecodes[i-1];
      if (double >= 10 && double <= 26) howManyDecodes[i] += howManyDecodes[i-2]
    }
    return howManyDecodes[s.length]
};
