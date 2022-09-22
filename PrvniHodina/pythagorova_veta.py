def main():
    inp = input("Are you calculationg hypotenuse (y, n): ")
    while inp not in ("y", "n"):
        inp = input("Not a valid response, try again: \n")
    
    if inp == "y":
        lenght1 = input("Lenght of first side: ")
        lenght2 = input("Lenght of second side: ")
        
        while not isfloat(lenght1, lenght2):
            print("Not valid input try again\n")
            
            lenght1 = input("Lenght of first side: ")
            lenght2 = input("Lenght of second side: ")

        lenght1, lenght2 = float(lenght1), float(lenght2)
        
        if min(lenght1, lenght2) <= 0:
            print("Can't have side with negative lenght\n")
            return
        
        output = (lenght1**2 + lenght2**2)**0.5
    
    else:
        lenght1 = input("Lenght of hypotenuse: ")
        lenght2 = input("Lenght of the other side: ")
        
        while not isfloat(lenght1, lenght2):
            print("Not valid input try again\n")
            
            lenght1 = input("Lenght of hypotenuse: ")
            lenght2 = input("Lenght of the other side: ")
            
        lenght1, lenght2 = float(lenght1), float(lenght2)
        
        if lenght2 >= lenght1:
            print("The other side can't be longer or eaqual to hypotenuse")
            return
        
        if min(lenght1, lenght2) <= 0:
            print("Can't have side with negative lenght")
            return
        
        output = (lenght1**2 - lenght2**2)**0.5
    
    print(output)

def isfloat(num1, num2):
    try:
        float(num1)
        float(num2)
        return True
    
    except ValueError:
        return False

if __name__ == '__main__':
    main()