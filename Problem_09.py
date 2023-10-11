if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    _set = set(arr)
    final = sorted(_set)
    print(final[-2])
