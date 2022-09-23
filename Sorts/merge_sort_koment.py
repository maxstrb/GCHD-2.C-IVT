import random

def main():
    a = [5, 6, 74, 4, 6, 54, 1, 5, 6, 1, 32, 1, 859, 15, 156, 651, 32, 0, 65, 1, 32, 5, 46, 54]
    
    print(f"The sorted list is {merge_sort(a)}")
    
def halfs_sort(l1, l2):
    # Přivravení listů se kterými se pracuje
    l1, l2 = l1.copy(), l2.copy()
    output = []
    
    # Vytvoří smičku která se zastaví když délka jednoho listu je < 1
    while min(len(l1), len(l2)) != 0:
        # Vyberu minimum ze 2 možností a to přidám do listu output
        min_n = min(l1[0], l2[0])
        output.append(min_n)
        
        # Najdu ze kterého tato možnost byla a smažu tento item
        if min_n in l1:
            l1.pop(0)
        else:
            l2.pop(0)
    
    # Jakmile se smička zastaví tak vím že jeden list už nemá prvky a druhý ano -> všechny zbývající prvky připojím k listu output
    output.extend(l1)
    output.extend(l2)
    
    return output

def merge_sort(l):
    if len(l) in {0, 1}:
        return l

    # Vytvářím rekurzivní funkci která vrací halfs_sort ze dvou listů sezařených touto funkcí -> vytvoří takový strom funkcí
    return halfs_sort(merge_sort(l[:len(l)//2]), merge_sort(l[len(l)//2:]))


def test():
    for _ in range(100):
        a = random.sample(range(-999, 999), random.randint(5, 64))
        
        if sorted(a, reverse=False) != merge_sort(a):
            print("Not working")
            return
        
    print("Everything went fine ✔")

if __name__ == '__main__':
    main()
    #test()