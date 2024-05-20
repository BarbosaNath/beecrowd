def solve():
    n = int(input())
    
    count = 0
    while n != 0:
        count += n & 1
        n >>= 1
    print(count)


if __name__ == "__main__":
    solve()
