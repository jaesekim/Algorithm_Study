count = int(input())
switch_list = list(map(int, input().split()))
student_num = int(input())


for num in range(student_num):
    dummy = list(map(int, input().split())) # dummy[0]은 성별
    base = dummy[1] # base는 학생이 받은 수
    if dummy[0] == 1: # 남학생이면
        for idx, _ in enumerate(switch_list): # 인덱스 값만 받아올 목적
            if not ((idx + 1) % base): # base의 배수라면
                if not switch_list[idx]: # switch_list[idx]의 값이 0이라면
                    switch_list[idx] = 1 # 1으로 넣어주기
                elif switch_list[idx] == 1: # # switch_list[idx]의 값이 1이라면
                    switch_list[idx] = 0 # 0으로 넣어주기
    elif dummy[0] == 2: # 여학생이면
        for idx, _ in enumerate(switch_list):
            if base == (idx + 1):
                i = 0
                
                while ((0 <= idx-i) and (idx+i < len(switch_list))):
                    if (switch_list[idx-i] == switch_list[idx+i]):
                        start = idx - i
                        finish = idx + i
                        i += 1
                    else:
                        break
                for no in range(start, finish + 1):
                    if not switch_list[no]: # switch_list[idx]의 값이 0이라면
                        switch_list[no] = 1 # 1으로 넣어주기
                    elif switch_list[no] == 1: # # switch_list[idx]의 값이 1이라면
                        switch_list[no] = 0 # 0으로 넣어주기
for ans_idx in range(1, count+1):
    print(switch_list[ans_idx - 1], end=' ')
    if ans_idx % 20 == 0:
        print("")