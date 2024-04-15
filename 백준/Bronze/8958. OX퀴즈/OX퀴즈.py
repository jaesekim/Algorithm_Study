for _ in range(int(input())):
    answer = [0]
    results = input()
    for result in results:
        if result == "O":
            answer.append(answer[-1] + 1)
        else:
            answer.append(0)
    print(sum(answer))