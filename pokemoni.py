import json
tabulka_typov = {}
data = json.load(open("effectiveness.json", "r"))
koeficienty = {"super effective": 2, "normal effective": 1, "not very effective": 0.5, "no effect": 0, }

for kategoria in data:
    for utocny_typ in data[kategoria]:
        if utocny_typ not in tabulka_typov:
            tabulka_typov[utocny_typ] = {}

        for obranny_typ in data[kategoria][utocny_typ]:
            tabulka_typov[utocny_typ][obranny_typ] = koeficienty[kategoria]

def vypocitaj_sila_utoku(utocnik, obranca):
    typy_utocnika = utocnik.split()
    typy_obrancu = obranca.split()

    sily_utokov = []

    for utok in typy_utocnika:
        sila_tohto_utoku = 1.0

        for obrana in typy_obrancu:
            nasobok = tabulka_typov.get(utok, {}).get(obrana, 1.0)
            sila_tohto_utoku = sila_tohto_utoku * nasobok

        sily_utokov.append(sila_tohto_utoku)

    return max(sily_utokov)
def attack(n1, n2, zoznam_text):
    vsetci_pokemonov = []
    for p in zoznam_text.split(","):
        vsetci_pokemonov.append(p.strip())

    tim1 = vsetci_pokemonov[:n1]
    tim2 = vsetci_pokemonov[n1: n1 + n2]
    f1 = 0.0
    f2 = 0.0
    for pok1 in tim1:
        for pok2 in tim2:
            f1 = f1 + vypocitaj_sila_utoku(pok1, pok2)
    for pok2 in tim2:
        for pok1 in tim1:
            f2 = f2 + vypocitaj_sila_utoku(pok2, pok1)
    f1 = round(f1, 1)
    f2 = round(f2, 1)
    if f1 > f2:
        vitaz = "ME"
    elif f1 < f2:
        vitaz = "FOE"
    else:
        vitaz = "EQUAL"
    return f1, f2, vitaz