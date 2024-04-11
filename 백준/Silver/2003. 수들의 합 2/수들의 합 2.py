import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

part = 0
answer = 0
add, sub = 0, 0
while True:
    if part < M:
        if add < N:  # add 리스트 끝까지 다 안갔다면
            part += arr[add]
            add += 1  # add 인덱스 올려주기
        else:  # 구간 합이 M보다 작은데 더 옮길 것이 없으므로 반복문 종료해도 된다.
            break
    elif part > M:  # 값을 초과했다면
        part -= arr[sub]
        sub += 1  # 빼기 포인터 인덱스 늘리
    else:  # 값이 같다면
        answer += 1
        part -= arr[sub]
        sub += 1  # 인덱스 올려주고 값도 빼 주면서  다른 경우의 수 탐색
print(answer)
