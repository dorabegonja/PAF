def pravac(x1, y1, x2, y2):
    if x1 == x2:
        print("x =", x1, "(pravac okomit na x os)")  #ako su x koordinate jednake pravac je okomit na x os i ima jednadžbu x=k
    else:
        k = (y2 - y1) / (x2 - x1)
        l = y1 - k * x1
        print("y =", k, "x +", l)
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
pravac(x1, y1, x2, y2)