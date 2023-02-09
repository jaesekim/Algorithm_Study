for _ in range(10):
    no = int(input())
    contains = input()
    chars = input()
    answer = 0

    i = 0
    while i < len(chars):
        if chars[i:i+len(contains)] == contains:
            answer += 1
        i += 1
    print(f"#{no} {answer}")