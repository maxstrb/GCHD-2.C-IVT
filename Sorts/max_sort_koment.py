import random

def main():
    a = [-5, 1, 1, 2, 4, 9, 6, 5, -7, 1, 3, 2, 8, 71, 0, 150, -99]
    print(f"The sorted list is {max_sort(a)}")

def max_sort(lst):
    # .copy() slouží k separaci zadaného listu a listu co budeme používat když se to neudělá tak se původní list změní stejně jako ten se kterým pracujeme tady - tento problém je jen u listů
    lst = lst.copy()

    for i in range(len(lst)-1):
        # Najdu největší prvek v listu pomocí funkce max() a uložím si jeho index
        mx = max(lst[:len(lst)-i])
        ind = lst.index(mx)

        # Potom jenom vyměním prvky na indexech posledního a největšího prvku
        lst[ind] = lst[-(i+1)]
        lst[-(i+1)] = mx

    # return vrací hodnotu -> když napíši y = f(x) tak se y nastaví na return této funkce
    return lst

def test():
    for _ in range(100):
        a = random.sample(range(-999, 999), 5)

        if sorted(a, reverse=False) != max_sort(a):
            print("Not working without my_max")
            return
        
    print("Everything went fine ✔")

if __name__ == '__main__':
    main()
    #test()
