import random

def main():
    a = [5, 6, 74, 4, 6, 54, 1, 5, 6, 1, 32, 1, 859, 15, 156, 651, 32, 0, 65, 1, 32, 5, 46, 54]
    
    print(f"The sorted list is {merge_sort(a)}")
    
def halfs_sort(l1, l2):
    f1 = 0
    f2 = 0
    
    
    l1, l2 = l1.copy(), l2.copy()
    
    output = []
    
    while f1 < len(l1) and f2 < len(l2):
        min_n = min(l1[f1], l2[f2])
        output.append(min_n)
        
        if min_n == l1[f1]:
            f1 += 1
        else:
            f2 += 1
    
    output.extend(l1[f1:])
    output.extend(l2[f2:])
    
    return output

def merge_sort(l):
    if len(l) in {0, 1}:
        return l

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
