function matrixBlockSum(mat: number[][], k: number): number[][] {
    const m = mat.length
    const n = mat[0].length
    const answer = Array.from({ length: m }, () => Array(n).fill(0))

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let sum = 0
            for (let x = Math.max(0, i - k); x <= Math.min(m - 1, i + k); x++) {
                for (let y = Math.max(0, j - k); y <= Math.min(n - 1, j + k); y++) {
                    sum += mat[x][y]
                }
            }
            answer[i][j] = sum
        }
    }

    return answer
}
