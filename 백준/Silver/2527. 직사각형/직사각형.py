for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())


    if ((x1, y1) == (p2, q2)) or ((p1, y1) == (x2, q2)) or ((x1, q1) == (p2, y2)) or ((p1, q1) == (x2, y2)):  # 점
        print('c')
    elif (((y1 == q2) or (q1 == y2)) and (len(set(range(x1, p1+1)) & set(range(x2, p2+1))))): # 남북선
        print('b')
    elif (((x1 == p2) or (p1 == x2)) and (len(set(range(y1, q1+1)) & set(range(y2, q2+1))))): # 동서선
        print('b')
    elif len(set(range(y1, q1+1)) & set(range(y2, q2+1))) and len(set(range(x1, p1+1)) & set(range(x2, p2+1))):
        print('a')
    else:
        print('d')