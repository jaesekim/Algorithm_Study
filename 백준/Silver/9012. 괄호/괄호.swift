let n = Int(readLine()!)!
for _ in 1...n {
    let chars = readLine()!
    let arr = chars.map { String($0) }
    var stack: [String] = []
    for item in arr {
        if item == "(" {
            stack.append(item)
        } else if item == ")" {
            if stack.isEmpty {
                stack.append(item)
                break
            } else {
                stack.popLast()
            }
        }
    }
    if stack.isEmpty {
        print("YES")
    } else {
        print("NO")
    }
}