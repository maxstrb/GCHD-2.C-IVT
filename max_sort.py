import random

def main():
    a = [-5, 1, 1, 2, 4, 9, 6, 5, -7, 1, 3, 2, 8, 71, 0, 150, -99]
    print(f"The sorted list with my_max is {max_sort_with_my_max(a)}")
    print(f"The sorted list with my_max is {max_sort_without_my_max(a)}")
    
    print(f"They are identical: {max_sort_without_my_max(a)==max_sort_with_my_max(a)}")

def my_max(lst):
    mx = lst[0]
    ind = 0

    for i, v in enumerate(lst):
        mx, ind = (v, i) if mx < v else (mx, ind)
    
    return mx, ind

def max_sort_with_my_max(lst):
    lst = lst.copy()

    for i in range(len(lst)-1):
        mx, ind = my_max(lst[:len(lst)-i])

        lst[ind] = lst[-(i+1)]
        lst[-(i+1)] = mx

    return lst


def max_sort_without_my_max(lst):
    lst = lst.copy()

    for i in range(len(lst)-1):
        mx = max(lst[:len(lst)-i])
        ind = lst.index(mx)

        lst[ind] = lst[-(i+1)]
        lst[-(i+1)] = mx

    return lst

def test():
    for _ in range(100):
        a = random.sample(range(-999, 999), 5)
        
        if sorted(a, reverse=False) != max_sort_with_my_max(a):
            print("Not working with my_max")
            
        if sorted(a, reverse=False) != max_sort_without_my_max(a):
            print("Not working without my_max")

if __name__ == '__main__':
    main()
    #test()
