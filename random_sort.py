import random

# 💣bongo sort💣 - the best of all sorting algorithms out there ❤🧡💛💚💙💜🤎🖤🤍💔💕💞💓💗💖💘

def main():
    mNL = [1, 2, 4, 3]
    print('The sorted list is: {} and the number of tries is: {}'.format(*rnd_sort(mNL, 0)))

def rnd_sort(mNL, iter):
    iter += 1
    mNL = mNL.copy()

    ok = all(mNL[i] <= mNL[i+1] for i in range(len(mNL) - 1))
    
    if ok:
        return mNL, iter
    
    random.shuffle(mNL)
    
    return rnd_sort(mNL, iter)

def test():
    for _ in range(100):
        a = random.sample(range(-999, 999), 4)
        
        if sorted(a, reverse=False) != rnd_sort(a, 0)[0]:
            print("Not working")

if __name__ == '__main__':
    main()
    #test()