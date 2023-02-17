di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

T = int(input())
for t in range(1, T +1):
    N, M = map(int, input().split())
    ans = 0  # 답을 넣어줄 변수

    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)

    for i in range(N):
        for j in range(M):
            cnt = 0  # cnt 초기화
            for k in range(8):  # 인접구역 검사
                try:
                    # !!! 여기서 오류 났었음 뒤에 0보다 크다는 조건이 없을 경우 인덱스가 -1로 빠지며 오류날 수 있움.
                    if (arr[i+di[k]][j+dj[k]] < arr[i][j]) and (i+di[k] >= 0) and(j+dj[k] >= 0):
                        cnt += 1
                        # print('k', k)
                        # print('ij',  arr[i][j])
                        # print(arr[i+di[k]][j+dj[k]])
                except IndexError:
                    pass
            if cnt >= 4:
                ans += 1
# ans 저장되늕지 확인
    print(f'#{t} {ans}')