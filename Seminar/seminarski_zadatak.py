import numpy as np
import matplotlib.pyplot as plt

#parametri
g = 9.81
m = 80.0

rho0 = 1.225  #gustoća zraka na razini mora
H = 8400.0  #visina skale atmosfere (kombinacija hidrostatske jednadžbe i jednadžbe idealnog plina)

Cd_pad = 1.0  #jer se uzima položaj trbuhom prema Zemlji
A_pad = 0.7   #efektivna površina tijela u tom položaju

Cd_padobran = 1.5
A_padobran = 35.0

sigurna_brzina = 6.0

vrijeme_otvaranja = 3.0

#sigurnosna rezerva
minimalna_visina_potpuno_otvoren = 200.0


#terminalne brzine
vt_pad = np.sqrt(2*m*g/(rho0*Cd_pad*A_pad))
vt_padobran = np.sqrt(2*m*g/(rho0*Cd_padobran*A_padobran))

print("\nTERMINALNE BRZINE")
print(f"Bez padobrana: {vt_pad:.2f} m/s")
print(f"S padobranom: {vt_padobran:.2f} m/s")


#gustoća zraka
def rho(h):
    return rho0*np.exp(-h/H)


#simulacija
def simulacija(h0, h_open, dt=0.001):
    h = h0
    v = 0
    t = 0
    otvaranje_zapocelo = False
    vrijeme_pocetka_otvaranja = None
    potpuno_otvoren_na = None

    T = []
    Hh = []
    V = []

    while h > 0:
        if h > h_open: #padobran nije otvoren
            Cd = Cd_pad
            A = A_pad
        else:
            if not otvaranje_zapocelo:
                otvaranje_zapocelo = True
                vrijeme_pocetka_otvaranja = t
            tau = (t - vrijeme_pocetka_otvaranja) / vrijeme_otvaranja
            tau = min(max(tau, 0), 1)
            Cd = Cd_pad + tau*(Cd_padobran - Cd_pad)
            A = A_pad + tau*(A_padobran - A_pad)
            if tau >= 1 and potpuno_otvoren_na is None:
                potpuno_otvoren_na = h

        a = g - 0.5*rho(h)*Cd*A*v**2/m
        v += a*dt
        h -= v*dt
        t += dt

        T.append(t)
        Hh.append(max(h, 0))
        V.append(v)

    return (np.array(T), np.array(Hh), np.array(V), potpuno_otvoren_na)


#provjera je li slijetanje sigurno
def sigurno_slijetanje(h0, h_open):

    T, Hh, V, potpuno_otvoren_na = simulacija(h0, h_open)

    uvjet_brzine = abs(V[-1]) <= sigurna_brzina 
    #zadnja brzina je brzina slijetanja
    
    uvjet_otvaranja = (
        potpuno_otvoren_na is not None and
        potpuno_otvoren_na >= minimalna_visina_potpuno_otvoren
    )

    return uvjet_brzine and uvjet_otvaranja



#binarna pretraga
def min_visina(h0):

    donja = 0
    gornja = h0

    for i in range(60):

        sredina = (donja + gornja)/2

        if sigurno_slijetanje(h0, sredina):
            gornja = sredina
        else:
            donja = sredina

    return gornja


#tablica
visine_skoka = [1000, 2000, 4000, 6000, 8000, 10000]

visine_otvaranja = []

print("\nREALISTIČNI MODEL")
print("Visina skoka [m] | Min. visina otvaranja [m]")
print("-"*45)

for h0 in visine_skoka:

    h_open = min_visina(h0)

    visine_otvaranja.append(h_open)

    print(f"{h0:15.0f} | {h_open:25.2f}")


#detaljna simulacija za primjer
h0_primjer = 4000

h_open = min_visina(h0_primjer)

t, h, v, potpuno_otvoren_na = simulacija(
    h0_primjer,
    h_open
)

print("\nDETALJNA SIMULACIJA")
print("Početna visina =", h0_primjer, "m")
print("Početak otvaranja =", round(h_open, 2), "m")
print("Potpuno otvoren na =", round(potpuno_otvoren_na, 2), "m")
print("Brzina slijetanja =", round(v[-1], 2), "m/s")
print("Maksimalna brzina =", round(np.max(v), 2), "m/s")


#graf 1
plt.figure(figsize=(8,5))
plt.plot(visine_skoka, visine_otvaranja, 'o-')
plt.xlabel("Početna visina [m]")
plt.ylabel("Minimalna visina otvaranja [m]")
plt.title("Ovisnost minimalne visine otvaranja o početnoj visini skoka")
plt.grid()

#graf 2
plt.figure(figsize=(8,5))
plt.plot(t, h)
plt.axhline(h_open, linestyle='--')
plt.axhline(minimalna_visina_potpuno_otvoren, linestyle=':')
plt.xlabel("Vrijeme [s]")
plt.ylabel("Visina [m]")
plt.title("Visina tijekom pada")
plt.legend(["Visina", "Početak otvaranja", "Sigurnosna rezerva"])
plt.grid()

#graf 3
plt.figure(figsize=(8,5))
plt.plot(t, v)
plt.axhline(sigurna_brzina, linestyle='--')
plt.axhline(vt_pad, linestyle=':')
plt.xlabel("Vrijeme [s]")
plt.ylabel("Brzina [m/s]")
plt.title("Brzina tijekom pada")
plt.legend(["Brzina", "Sigurna brzina", "Terminalna brzina"])
plt.grid()
plt.show()