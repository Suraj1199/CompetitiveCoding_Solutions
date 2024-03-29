def poisonousPlants(p):
    stack = []
    max_days = 0
    for i in range(len(p)-1, -1, -1):
        kills = 0
        while (len(stack) > 0) and stack[-1][0] > p[i]:
            kills = max(kills + 1, stack.pop()[1])
        max_days = max(max_days, kills)
        stack.append((p[i], kills))
    return max_days

if __name__ == '__main__':
    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    result = poisonousPlants(p)
    print(result)
