var isAnagram = function (s, t) {
  if (s.split("").sort().join() === t.split("").sort().join()) {
    return true;
  } else {
    return false;
  }
};
