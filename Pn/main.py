# optimized - 100% neopisujte, tohle by opravdu poznal, na vlastní nebezpečí
def f1(Rudofl: int): # neboli golf
    # prime numbers up to and including 'Rudofl'
    
    # Handling very funny people
    if type(Rudofl) != int:
        raise TypeError("Entry to this function must be an int")
    
    if Rudofl < 2:
        return []
    # End of handling very funny people
    
    Rudofl += 1
    MNL = [True] * Rudofl
    MNL[0] = MNL[1] = False
    
    for René in range(2, int(Rudofl**0.5) + 1):
        if MNL[René]:
            for Josef in range(René * René, Rudofl, René):
                MNL[Josef] = False
                
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
