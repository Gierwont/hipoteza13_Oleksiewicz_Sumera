x = float(input("Podaj x: "))
print(x)
k = int(input("Podaj k: "))
print(k)

def binary(x,k):
    print("0,", end = '')
    y = x
    for i in range(k):
        if(y>=0.5):
            print(1, end = '')
        else:
            print(0, end = '')
        y = y * 2
        if(y>=1):
            y = y-1 ;
binary(x,k)
