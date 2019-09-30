def main():
    print("Calcular dígito vertificador RUT")
    rut = input("Ingrese RUT sin dígito verificador: ")
    res = dv(rut)
    if res == 10:
        res = 'K'
    print("El dígito verificador es: " + str(res))
    print("El RUT completo es: " + str(rut) + "-" + str(res))

def dv(rut):
    j = 2
    largo = len(rut)
    sum = 0
    for i in range(largo-1,-1,-1):
        if j == 8:
            j = 2
        sum = sum + (int(rut[i])*j)
        j += 1
    mod = sum/11
    mod = int(mod)*11
    dvf = 11-(sum-mod)
    return dvf


if __name__ == '__main__':
    import sys
    sys.exit(main())
