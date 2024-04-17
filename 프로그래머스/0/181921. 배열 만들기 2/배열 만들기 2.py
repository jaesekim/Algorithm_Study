def solution(l, r):
    
    def only_zero_or_five(chars):
        for char in chars:
            
            if char == "0" or char == "5":
                continue
            else:
                return False
        return True
    

    answer = []
    arr = [x for x in range(0, r + 1, 5) if not x % 5 and x >= l]
    for num in arr:
        if only_zero_or_five(str(num)):
            answer.append(num)

    if not len(answer):
        return [-1]
    return answer