while True:
    try:
        unos = input("Unesi prvu točku (x y): ").split()
        x1 = float(unos[0])
        y1 = float(unos[1])
        break
    except:
        print("Greška!")
while True:
    try:
        unos = input("Unesi drugu točku (x y): ").split()
        x2 = float(unos[0])
        y2 = float(unos[1])
        break
    except:
        print("Greška")
if x1 == x2:
    print("x =", x1)  #ako su x koordinate jednake pravac je okomit na x os i ima jednadžbu x=k
else:
    k = (y2 - y1) / (x2 - x1)
    l = y1 - k * x1
    print("y =", k, "x +", l)