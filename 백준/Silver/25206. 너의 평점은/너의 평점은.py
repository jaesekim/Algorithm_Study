grades = [tuple(input().split()[1:]) for _ in range(20)]
cul_hour = 0
cul_grade = 0
table = {
'A+': 4.5,
'A0': 4.0,
'B+': 3.5,
'B0': 3.0,
'C+': 2.5,
'C0': 2.0,
'D+': 1.5,
'D0': 1.0,
'F' : 0.0
}
for hour, grade in grades:
    if grade == 'P':
        continue
    cul_grade += table[grade] * float(hour)
    cul_hour += float(hour)
print(cul_grade / cul_hour)