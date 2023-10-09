# using for loop
cube = lambda x: x ** 3


def fibonacci(n):
    lis = [0, 1]
    for i in range(2, n):
        lis.append(lis[i - 2] + lis[i - 1])
    return (lis[0:n])


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# using while loop
cube = lambda x: pow(x,3)

def fibonacci(n):
    lis = [0,1]
    x = 2
    while x<=n:
        lis.append(lis[x-2]+lis[x-1])
        x += 1
    return(lis[0:n])


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))