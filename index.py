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
            y = y-1
        if(y>=1):
            y = y-2
    return wynik

print(trójkowy(x,k))
