import sys
input = sys.stdin.readline


def validation(start, end):
    while start < end:
        if chars[start] != chars[end]:
            return False
        start += 1
        end -= 1
    return True


T = int(input())
for _ in range(T):
    chars = input().rstrip()
    left, right, answer = 0, len(chars) - 1, 0
    while left < right:
        # 문자열 양쪽 끝이 같다면 포인터 변경해 주고 다음 것 검사하기
        if chars[left] == chars[right]:
            left += 1
            right -= 1
        else:  # 두 포인터가 가리키는 문자열이 다를 때
            # 왼쪽 포인터를 옮겨줬을 때 회문 가능성이 남아있으면서 아직 한 번도 변경하지 않았다면
            if validation(left + 1, right) or validation(left, right - 1):
                answer = 1
            else:
                answer = 2
            break
    print(answer)
