# MFP - C
# Cogumelos

def dist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def solve():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())

    d1 = dist(x1, y1, x2, y2)
    d2 = dist(x1, y1, x3, y3)

    if d1 < d2:
        print(int(d1**2))
    else:
        print(int(d2**2))
        

    

if __name__ == '__main__':
    solve()
