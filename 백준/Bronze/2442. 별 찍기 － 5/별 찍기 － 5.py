row = int(input())
for i in range(row):
    print(' '*int(((2*row - 1) - (2*(i+1)-1))//2) + '*'*(2*(i+1)-1))