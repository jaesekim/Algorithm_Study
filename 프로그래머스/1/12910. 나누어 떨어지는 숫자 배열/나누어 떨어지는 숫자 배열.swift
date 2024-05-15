func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
    var answer = arr.filter {
        $0 % divisor == 0
    }
    answer.sort()

    if answer.count == 0 {
        return [-1]
    } else {
        return answer
    }
}