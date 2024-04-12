def solution(command):
    # 상 우 하 좌
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    idx = 0
    answer = [0, 0]
    for move in command:
        if move == "G":
            answer = [answer[0] + dx[idx], answer[1] + dy[idx]]
        elif move == "L":
            idx = (idx - 1) % 4
        elif move == "R":
            idx = (idx + 1) % 4
        else:  # move == "B"
            answer = [answer[0] - dx[idx], answer[1] - dy[idx]]
    return answer
