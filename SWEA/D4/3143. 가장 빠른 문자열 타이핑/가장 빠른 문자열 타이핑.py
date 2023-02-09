T = int(input())

for no in range(1, T+1):
    A, B = input().split()
    length_a = len(A)
    length_b = len(B)
    count = 0
    i = 0
    while i <= len(A) - length_b:
        if A[i:i+length_b] == B:
            count += 1
            i += length_b
            continue
        i += 1
    if not count:
        print(f"#{no} {length_a}")
    else:
        left = length_a - (count * length_b)
        print(f"#{no} {count + left}")