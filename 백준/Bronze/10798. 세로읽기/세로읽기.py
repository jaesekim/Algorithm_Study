row = [list(input()) for _ in range(5)]
chars = [[] for _ in range(15)]
answer = ''
for row_letter in row:
    for idx, letter in enumerate(row_letter):
        chars[idx].append(letter)
for char in chars:
    answer += ''.join(char)
print(answer)