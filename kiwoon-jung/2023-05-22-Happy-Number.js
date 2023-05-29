const sumSet = [];

function happyNumber(n) {
  const input = splitNumber(n);
  console.log("this is input", input);

  if (input == 1) {
    return true;
  } else {
    let sum = 0;
    for (let i = 0; i < input.length; i++) {
      sum += input[i] * input[i];
      console.log("this is sum", sum);
    }

    if (sumSet.find((el) => el === sum)) {
      return false;
    } else if (sum == 1) {
      return true;
    } else {
      sumSet.push(sum);
      console.log("sumSetArr", sumSet);
      return happyNumber(sum);
    }
  }
}

function splitNumber(n) {
  const splitNumber = n.toString().split("");
  const singleNumber = splitNumber.map(Number);

  return singleNumber;
}

console.log(happyNumber(13));
