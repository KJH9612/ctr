N = int(input())
l = list(map(int, input().split()))
stk, ans = [], []

for i in range(N):
    while stk:
        if stk[-1][1] > l[i]:
            ans.append(stk[-1][0] + 1)
            break
        else:
            stk.pop()
    if not stk:
        ans.append(0)
    stk.append([i, l[i]])

print(" ".join(map(str, ans)))