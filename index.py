x = float(input("Podaj x: "))
print(x)
k = int(input("Podaj k: "))
print(k)

def binary(x,k):
    wynik = "0,"
    y = x
    for i in range(k):
        if(y>=0.5):
            wynik += "1"
        else:
            wynik += "0"
        y = y * 2
        if(y>=1):
            y = y-1 ;
    return wynik
print(binary(x,k))
