import Foundation

func solution(_ n:Int, _ control:String) -> Int {
    var result = n
    for chr in control {
        if String(chr) == "w" {
            result += 1
        } else if String(chr) == "s" {
            result -= 1
        } else if String(chr) == "d" {
            result += 10
        } else {
            result -= 10
        }
    }
    return result
}
