p1 = p2 = 0
def solve():
    _, team, points = input().split()
    if team == '1':
        global p1
        p1 += int(points)
    else:
        global p2
        p2 += int(points)

# n = 2
n = int(input()) + 1

while(n := n-1): solve()

print(f"{p1} x {p2}")
