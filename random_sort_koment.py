import random

def main():
    mNL = [1, 2, 4, 3, 6, 7, 15]
    print('The sorted list is: {} and the number of tries is: {}'.format(*rnd_sort(mNL)))

def rnd_sort(mNL, iter=0):
    # iter slouží jako uložení pouču pokusů (iter -> iteration)
    iter += 1
    
    mNL = mNL.copy()

    # Zkontroluje jestli jsou vyšechny prvky seřazené
    ok = all(mNL[i] <= mNL[i+1] for i in range(len(mNL) - 1))
    
    # Když jsou seřazené tak skončí a vrátí seřazený list
    if ok:
        return mNL, iter
    
    # Náhodně zamíchá list
    random.shuffle(mNL)
    
    # Opakujese dokud nejsou seřasené
    return rnd_sort(mNL, iter)

def test():
    for _ in range(100):
        a = random.sample(range(-999, 999), 4)
        
        if sorted(a, reverse=False) != rnd_sort(a)[0]:
            print("Not working")
            return
        
    print("Everything went fine ✔")

if __name__ == '__main__':
    main()
    #test()