def solution(s):
    dict = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    answer = ""
    idx = 0

    while idx < len(s):
        valid = ""
        if s[idx] in numbers:
            answer += s[idx]
            idx += 1
            continue
        else:
            for j in range(idx, len(s)):
                valid += s[j]
                if dict.get(valid, 0):
                    answer += dict[valid]
                    idx = j + 1
                    break
    return int(answer)