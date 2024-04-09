from itertools import permutations
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
new_arr = list(permutations(arr, M))
new_arr.sort()
for item in new_arr:
    print(*item)
