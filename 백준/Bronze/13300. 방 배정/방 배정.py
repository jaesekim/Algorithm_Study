import math

N, K = map(int, input().split())
students = {
    1: [0, 0],
    2: [0, 0],
    3: [0, 0],
    4: [0, 0],
    5: [0, 0],
    6: [0, 0]
}  # 학년 : [여학생 수, 남학생 수]
rooms = 0  # 필요한 방의 개수
for _ in range(N):
    sex, grade = map(int, input().split())
    students[grade][sex] += 1
for key in students:
    for nums in students[key]:
        rooms += math.ceil(nums / 2)
print(rooms)