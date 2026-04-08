import matplotlib.pyplot as plt
def pravac(x1, y1, x2, y2, spremi=False, ime="graf.pdf"):
    if x1 == x2:
        print("x =", x1, "(pravac okomit na x os)")
        plt.axvline(x=x1) #crtanje vertikalne linije na x1 (axis vertical line)
    else:
        k = (y2 - y1) / (x2 - x1)
        l = y1 - k * x1
        print("y =", k, "x +", l)
        x = [x1, x2]
        y = [y1, y2]
        plt.plot(x, y)
    plt.scatter([x1, x2], [y1, y2])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Pravac kroz dvije točke")
    if spremi:
        plt.savefig(ime)
        print("Spremljeno kao", ime)
    else:
        plt.show()
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
izbor = input("Upiši 's' za spremanje ili bilo što za prikaz: ")
if izbor == "s":
    ime = input("Ime datoteke (npr. graf.pdf): ")
    pravac(x1, y1, x2, y2, True, ime)
else:
    pravac(x1, y1, x2, y2)