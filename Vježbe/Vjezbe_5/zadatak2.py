def iteracija(N):
    x = 5.0
    for _ in range(N):
        x += 1/3
    for _ in range(N):
        x -= 1/3
    return x

for N in [200, 2000, 20000]:
    rezultat = iteracija(N)
    print(f"N = {N}, rezultat = {rezultat}")