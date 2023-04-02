def backtracking(i, cul):
    global answer
    if i == N:
        if cul == S:
            answer += 1
        return
    backtracking(i+1, cul+arr[i])  # 해당 숫자 포함
    backtracking(i+1, cul)         # 해당 숫자 미포함
    
    

N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
backtracking(0, 0)
# S가 0이라면 부분 수열이 없을 경우를 빼 준다
if not S:
    answer -= 1
print(answer)