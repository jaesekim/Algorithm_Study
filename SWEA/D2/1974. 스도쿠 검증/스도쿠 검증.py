def check_row(arr):
    for row in arr:
        if len(set(row)) != 9:
            return 0
    return 1

def transposed(arr):
    matrix_T = []
    for i in range(len(arr)):
        row_matrix = []
        for j in range(len(arr)):
            row_matrix.append(arr[j][i])
        matrix_T.append(row_matrix)
    return matrix_T


def check_box(arr):
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            box_matrix = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(box_matrix)) != 9:
                return 0
    return 1


T = int(input())

for no in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]

    row = check_row(matrix)
    col = check_row(transposed(matrix))
    box = check_box(matrix)

    if (not row) or (not col) or (not box):
        print(f"#{no} 0")
    else:
        print(f"#{no} 1")