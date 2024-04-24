import Foundation

func solution(_ myString:String, _ pat:String) -> Int {
    
    var answer = 0
    let charList = myString.map { String($0) }
    let patList = pat.map { String($0) }
    var i = 0
    while i < charList.count - patList.count + 1 {
        if charList[i] == patList[0] {
            var j = 0
            while j < patList.count {
                if charList[i + j] != patList[j] {
                    break
                }
                j += 1
            }
            if j == patList.count {
                answer += 1
            }
        }
        i += 1
    }
    return answer
}