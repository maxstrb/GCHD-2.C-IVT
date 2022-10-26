# optimized - 100% neopisujte, tohle by opravdu poznal, na vlastní nebezpečí
def f1(Rudolf: int): # neboli golf
    # prime numbers up to and including 'Rudolf'
    
    # Handling very funny people
    if type(Rudolf) != int:
        raise TypeError("Entry to this function must be an int")
    
    if Rudolf < 2:
        return []
    # End of handling very funny people
    
    Rudolf += 1 # Rudolf je moc malý, takže ho zvětšuji
    MNL = [True] * Rudolf # MNL = hodněkrát True, přesněji Rudoflkrát True
    MNL[0] = MNL[1] = False # Tyhle dva nechci
    
    for René in range(2, int(Rudolf**0.5) + 1): # Blbý for cyklus, ale funguje
        if MNL[René]: # Pokud je René prvočíslo tak
            for Josef in range(René * René, Rudolf, René): # Všechna čísla, která jsou dělitelná René, jsou neprvočísla
                MNL[Josef] = False # Takže je nastavím na False
    
    # Výstup je seznam prvočísel, od 2 do Rudolfa
    return [René for René, Já in enumerate(MNL) if Já]

# větší šance na, že nepozná okopírování když se to trochu změní
def f2(Karel: int):
    # Handling very funny people
    if type(Karel) != int:
        raise TypeError("Entry to this function must be an int")
    
    if Karel < 2:
        return []
    # End of handling very funny people
    
    output = []
    Karel -= 1
    
    l = [True] * Karel
    
    for František, Jakub in enumerate(l):
        if Jakub:
            output.append(František+2)
            
            for j in range(2*František + 2, Karel, František+2):
                l[j] = False
    
    return output


def main():
    # testovací kód
    print(f1(100))
    print(f2(100))
    
    print([(f1(František), f2(František)) for František in range(500) if f1(František) != f2(František)])

if __name__ == '__main__':
    main()
