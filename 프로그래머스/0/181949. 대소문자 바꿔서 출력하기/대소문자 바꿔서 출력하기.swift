import Foundation

let s1 = readLine()!

var result: String = ""

for chr in s1 {
    let lowerA = Int(UnicodeScalar("a").value)
    let lowerZ = Int(UnicodeScalar("z").value)
    let upperA = Int(UnicodeScalar("A").value)
    let upperZ = Int(UnicodeScalar("Z").value)
    let sub: UInt8 = 32
    var cur = chr.asciiValue!
    
    if lowerA <= cur && cur <= lowerZ {
        result += String(UnicodeScalar(cur - sub))
    } else if upperA <= cur && cur <= upperZ {
        result += String(UnicodeScalar(cur + sub))
    }
}
print(result)
