for _ in range(int(input())):
    location, sentence = input().split()
    location = int(location)
    print(sentence[:location - 1] + sentence[location:])