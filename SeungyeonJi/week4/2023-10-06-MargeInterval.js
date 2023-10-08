var merge = function (newArr) {
  if (newArr.length <= 1) {
    return newArr;
  }

  // 정렬하여 겹치는 구간을 찾기 쉽게 함
  newArr.sort((a, b) => a[0] - b[0]);

  let mergedArr = [newArr[0]];

  for (let i = 1; i < newArr.length; i++) {
    const current = newArr[i]; //[1,3]
    const lastMerged = mergedArr[mergedArr.length - 1]; //[1, 2]

    if (current[0] <= lastMerged[1]) {
      // 현재 구간과 이전 병합된 구간이 겹칠 경우 병합
      lastMerged[1] = Math.max(lastMerged[1], current[1]); // 뒤만 바뀌게 함
    } else {
      // 겹치지 않을 경우 새로운 구간 추가
      mergedArr.push(current);
    }
  }

  return mergedArr;
};
