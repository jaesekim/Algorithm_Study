S = input()

if S[0] == "0":
    first = "0"
    opposite = "1"
else:
    first = "1"
    opposite = "0"
idx = 1
answer = 0

while idx < len(S):
    if S[idx - 1] != S[idx] and S[idx] == opposite:
        answer += 1
    idx += 1
print(answer)
