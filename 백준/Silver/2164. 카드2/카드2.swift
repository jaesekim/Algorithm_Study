struct QueuePointer<T> {
  private var elements: [T] = []
  private var front = 0

  var isEmpty: Bool {
    elements.count < front + 1
  }

  var count: Int {
    elements.count - front
  }

  func peek() -> T? {
    front < elements.count ? elements[front] : nil
  }

  mutating func enqueue(with element: T) {
    elements.append(element)
  }

  @discardableResult
  mutating func dequeue() -> T? {
    if !isEmpty {
      defer { front += 1 }
      return elements[front]
    } else {
      return nil
    }
  }
}

let N = Int(readLine()!)!
var arr = QueuePointer<Int>()
var pointer = 0

for num in 1...N {
    arr.enqueue(with: num)
}

while arr.count != 1 {
    arr.dequeue()
    arr.enqueue(with: arr.dequeue()!)
}

print(arr.peek()!)