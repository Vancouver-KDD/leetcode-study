class TimeMap {
  constructor() {
    this.keyStore = new Map();
  }

  /**
   * @param {string} key
   * @param {string} value
   * @param {number} timestamp
   * @return {void}
   */
  set(key, value, timestamp) {
    // (prev_timestamp <= timestamp)
    if (!this.keyStore.has(key)) {
      this.keyStore.set(key, []);
    }
    this.keyStore.get(key).push([timestamp, value]);
  }

  /**
   * @param {string} key
   * @param {number} timestamp
   * @return {string}
   */
  get(key, timestamp) {
    let result = "";
    if (this.keyStore.has(key)) {
      let timestampArr = this.keyStore.get(key);
      let start = 0;
      let end = timestampArr.length - 1;

      while (start <= end) {
        let mid = Math.floor((start + end) / 2);
        // s   1 e m
        // 1 2 3 4 5 6 7 8 9 10
        if (timestampArr[mid][0] <= timestamp) {
          result = timestampArr[mid][1];
          start = mid + 1;
        } else {
          end = mid - 1;
        }
      }
    }

    return result;
  }
}
