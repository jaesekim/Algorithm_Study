import sys
input = sys.stdin.readline

books = {}
result_count = 0
result_title = ""
for _ in range(int(input())):
    title = "".join(input().split("\n"))
    books[title] = books.get(title, 0) + 1

for key, value in books.items():
    if value > result_count:
        result_count = value
        result_title = key
    elif value == result_count:
        tmp = sorted([result_title, key])
        result_title = tmp[0]
print(result_title)
