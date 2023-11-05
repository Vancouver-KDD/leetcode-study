class Solution {
    var dic: [Int: Int] = [:]

    func fib(_ n: Int) -> Int {
        if n <= 1 {
            return n
        }

        if let result = dic[n] {
            return result
        }

        dic[n] = fib(n-1) + fib(n-2)
        return dic[n] ?? 0
    }
}
