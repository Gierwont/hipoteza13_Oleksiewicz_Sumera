x = float(input("Podaj liczbę: "))
k = int(input("Podaj dokładność: "))

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

def trójkowy(x,k):
    wynik = "0,"
    y = x
    for i in range(k):
        if(y>=(2/3)):
            wynik += "2"
        elif(y>=(1/3)):
            wynik += "1"
        elif (y>=0):
            wynik += "0"
        y = y * 3
        if(y>=2):
            y = y-2
        if(y>=1):
            y = y-1
    return wynik

print("Liczba w systemie binarnym wynosi: " + binary(x,k))
print("Liczba w systemie trójkowym wynosi: " + trójkowy(x,k))
