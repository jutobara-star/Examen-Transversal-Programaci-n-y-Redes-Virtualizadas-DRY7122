asn = int(input("Ingrese el número de AS de BGP: "))

if 64512 <= asn <= 65534:
    print("El AS es Privado.")
else:
    print("El AS es Público.")
