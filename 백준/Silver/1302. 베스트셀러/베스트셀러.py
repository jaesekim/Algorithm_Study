N = int(input())
books = {}
for _ in range(N):
    title = input()
    if title in books:
        books[title] += 1
    else:  # key 값 없으면 넣어주고 1로 초기화
        books[title] = 1
print(sorted(books, key=lambda x: (-books[x], x))[0])  # 내림차순 정렬, 사전 순 정렬