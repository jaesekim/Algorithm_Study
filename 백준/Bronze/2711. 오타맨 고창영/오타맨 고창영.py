for _ in range(int(input())):
    location, sentence = input().split()
    result = ""
    char_arr = list(sentence)
    char_arr.pop(int(location) - 1)
    print("".join(char_arr))
