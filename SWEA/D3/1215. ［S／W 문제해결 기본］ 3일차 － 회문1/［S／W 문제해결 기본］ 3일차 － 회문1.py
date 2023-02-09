def find_palindrome(chars):
    if chars == chars[::-1]:
        return 1
    return 0


def transposed_matrix(arr):
    """
    :param arr: 문자열이 인자로 있는 1차원 리스트
    :return: arr의 전치행렬. 즉 문자열을 전치.
   """
    converted_arr = []
    for i in range(len(arr)):
        tmp_str = ''
        for j in range(len(arr)):
            tmp_str += arr[j][i]
        converted_arr.append(tmp_str)
    return converted_arr


for no in range(1, 11):
    length = int(input())
    matrix = [input() for _ in range(8)]
    answer = 0  # 정답값을 넣어줄 변수

    # 가로 검사
    for row in matrix:
        for x in range(8 - length + 1):
            check_str = row[x:x+length]
            if find_palindrome(check_str):
                answer += 1

    # 세로 검사
    matrix = transposed_matrix(matrix)
    for col in matrix:
        for y in range(8 - length + 1):
            check_str = col[y:y+length]
            if find_palindrome(check_str):
                answer += 1
    print(f"#{no} {answer}")