var countBits = function (n) {
  return Array.from(
    { length: n + 1 },
    (_, i) => i.toString(2).replace(/0/g, "").length
  );
};
