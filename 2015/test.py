def pisano_period(N):
    a, b = 0, 1
    period = 0
    while True:
        a, b = b, (a + b) % N
        period += 1
        if a == 0 and b == 1:
            return period

while True:
    N = int(input())
    if N == 0:
        break
    result = pisano_period(N)
    print(result)