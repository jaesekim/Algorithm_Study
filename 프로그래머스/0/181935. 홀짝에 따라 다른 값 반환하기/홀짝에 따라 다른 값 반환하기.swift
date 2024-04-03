import Foundation

func solution(_ n:Int) -> Int {
    var result = 0
    if n % 2 == 1{
        for num in stride(from: 1, to: n+2, by: 2) {
            result += num
        }
        return result
    } else {
        
        for num in stride(from: 2, to: n+2, by: 2) {
            result += num * num
        }
        return result
    }
}