height_array = [int(input()) for _ in range(9)]


def height_combination():
    length = len(height_array)
    sum_height = sum(height_array)
    for i in range(length - 1):
        for j in range(i + 1, length):
            comb1, comb2 = height_array[i], height_array[j]
            if sum_height - comb1 - comb2 == 100:
                height_array.remove(comb1)
                height_array.remove(comb2)
                return


height_combination()
height_array.sort()
for height in height_array:
    print(height)
