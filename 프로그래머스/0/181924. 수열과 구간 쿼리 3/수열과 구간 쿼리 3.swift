import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {

    var swapArr = arr
    
    for query in queries {

        var tmp = swapArr[query[0]]
        swapArr[query[0]] = swapArr[query[1]]
        swapArr[query[1]] = tmp
    }
    return swapArr
}
