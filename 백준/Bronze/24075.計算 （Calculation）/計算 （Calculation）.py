import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

print(a + b if a + b > a - b else a - b)
print(a + b if a + b < a - b else a - b)

