function asteroidCollision(asteroids: number[]): number[] {
  const stack: number[] = [];

  for (const asteroid of asteroids) {
    let alive = true;

    while (
      alive &&
      asteroid < 0 &&
      stack.length > 0 &&
      stack[stack.length - 1] > 0
    ) {
      const top = stack[stack.length - 1];

      if (Math.abs(top) < Math.abs(asteroid)) {
        stack.pop();
      } else if (Math.abs(top) === Math.abs(asteroid)) {
        stack.pop();
        alive = false;
      } else {
        alive = false;
      }
    }

    if (alive) {
      stack.push(asteroid);
    }
  }

  return stack;
}
