T = int(input())


def earth_to_alien(earth_arr, alien_arr):
    for earth_index, number in enumerate(earth_arr):
        for alien_index, n in enumerate(alien_arr):
            if number == alien_index:
                earth_arr[earth_index] = n
    return earth_arr


for _ in range(1, T+1):
    no, N = input().split()
    N = int(N)
    code_list = input().split()
    earth_num = [0] * N
    converted_num = []  # 재정렬을 위한 리스트 선언
    alien_code = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    i = 0

    while i < N:
        for idx, num in enumerate(alien_code):
            if num == code_list[i]:
                converted_num.append(idx)
                break
        i += 1
    converted_num.sort()
    converted_num = earth_to_alien(converted_num, alien_code)
    print(f"{no}", *converted_num)