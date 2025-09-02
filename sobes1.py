s = input()

def solve(s):

    l = -1
    r = -1
    ans = float('inf')
    for i in range(len(s)):
        if s[i] == "X":
            l = i
            if r != -1:
                ans = min(ans, l - r -1)

        elif s[i] == "Y":
            r = i
            if l != -1:
                ans = min(ans, r - l + 1)

    return 0 if ans == float('inf') else ans

print(solve(s))

