def sumXor(n):
    if n == 0:
        return 1
    c = bin(n)[2:].count('0')
    return 2 ** c

if __name__ == '__main__':
    n = int(input().strip())
    result = sumXor(n)
    print(result)
