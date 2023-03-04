def solution(s):
    p_cnt = 0
    y_cnt = 0
    for char in s:
        if char == 'p' or char == 'P':
            p_cnt += 1
        elif char == 'y' or char == 'Y':
            y_cnt += 1
    if y_cnt == p_cnt:
        return True
    return False