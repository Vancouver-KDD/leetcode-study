function totalFruit(fruits: number[]): number {
  const { length } = fruits
  let output = 2
  if (length < 3) {
    return length
  }

  let l = 0
  let r = 0
  const map = new Map()

  while (r < length) {
    const fruit = fruits[r]
    map.set(fruit, map.get(fruit) + 1 || 1)
    const potentialOutput = r - l + 1
    if (map.size < 3) {
      if (output < potentialOutput) {
        output = potentialOutput
      }
    } else {
      const fruitStart = fruits[l]
      map.set(fruitStart, map.get(fruitStart) - 1)

      if (map.get(fruitStart) === 0) {
        map.delete(fruitStart)
      }
      l++
    }
    r++
  }
  return output
}
