t = int(input())
for _ in range(t):
    n, x = map(int, input().split(" "))
    print(x % (n + 1))
