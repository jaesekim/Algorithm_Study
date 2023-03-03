def immediately(test, speed, make):
    """
    :param test:  테스트 번호
    :param speed: make 개 붕어빵을 만드는 속도
    :param make:  한 번에 만드는 붕어빵 개수
    """
    bread = 0  # 현재 있는 빵의 개수
    time = 0
    last = max(arrival)
    while time <= last:
        if not time % speed and time:
            bread += make
        for booked in arrival:
            if booked == time and not bread:
                return print(f"#{test} Impossible")
            elif booked == time and bread:
                bread -= 1
        time += 1
    return print(f"#{test} Possible")


T = int(input())
for test_no in range(1, T+1):
    N, M, K = map(int, input().split())
    # K개 붕어빵을 M초마다 만듦
    arrival = sorted(list(map(int, input().split())))
    immediately(test_no, M, K)