S = input()
M = S.split('-')
first = sum(map(int, M[0].split('+')))

for i in M[1:]:
    first -= sum(map(int, i.split('+')))
print(first)
