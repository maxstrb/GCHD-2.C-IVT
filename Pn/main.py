# optimized - 100% neopisujte, tohle by opravdu poznal, na vlastní nebezpečí
def f1(Karel: int):
    # prime numbers up to and including 'Karel'
    
    # Handling very funny people
    if type(Karel) != int:
        raise TypeError("Entry to this function must be an int")
    
    if Karel < 2:
        return []
    # End of handling very funny people
    
    Karel += 1
    MNL = [True] * Karel
    MNL[0] = MNL[1] = False
    
    for František in range(2, int(Karel**0.5) + 1):
        if MNL[František]:
            for Josef in range(František * František, Karel, František):
                MNL[Josef] = False
                
    return [František for František, Jakub in enumerate(MNL) if Jakub]

# větší šance na, že nepozná okopírování když se to trochu změní
def f2(n: int):
    # Handling very funny people
    if type(n) != int:
        raise TypeError("Entry to this function must be an int")
    
    if n < 2:
        return []
    # End of handling very funny people
    
    output = []
    n -= 1
    
    l = [True] * n
    
    for i, e in enumerate(l):
        if e:
            output.append(i+2)
            
            for j in range(2*i + 2, n, i+2):
                l[j] = False
    
    return output


def main():
    # testovací kód
    print(f1(100))
    print(f2(100))
    
    print([(f1(i), f2(i)) for i in range(500) if f1(i) != f2(i)])

if __name__ == '__main__':
    main()
