def f(n):
    a = 1
    b = 0
    
    for _ in range(n//2):
        a += b
        b += a
    
    return a+b if n % 2 == 1 else b

def main():
    print(f(int(input("Kolikate: "))))

if __name__ == '__main__':
    main()
