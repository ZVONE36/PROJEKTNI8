def get_kategorija(redni_broj, kategorija):
    print(f"{redni_broj}. {kategorija.naziv}")

def ispis_svih_kategorija(kategorije):
    for kategorija in kategorije:
        print(f"{kategorija.naziv}")
        for artikl in kategorija.artikli:
            artikl.ispis()

