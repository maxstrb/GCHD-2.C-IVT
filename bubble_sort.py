import random

def main():
    a = [1, 4, 2, 9, 5]
    
    print(f"The sorted list is {bubble_sort(a)}")
    
def bubble_sort(mNL):
    mNL = mNL.copy()
    
    for n in range(len(mNL)-1):
        for i in range(len(mNL)-n-1):
            if mNL[i] > mNL[i+1]:
                temp = mNL[i+1]

                mNL[i+1] = mNL[i]
                mNL[i] = temp

    return mNL


def test():
    for _ in range(100):
        a = random.sample(range(-999, 999), 7)
        
        if sorted(a, reverse=False) != bubble_sort(a):
            print("Not working")

if __name__ == '__main__':
    main()
    #test()