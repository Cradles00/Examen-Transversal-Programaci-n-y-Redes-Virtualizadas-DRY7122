def verificar_as(as_number):
    try:
        as_num = int(as_number)
        if 64512 <= as_num <= 65534 or as_num == 4200000000 or (65535 <= as_num <= 4294967294):
            return "privado"
        elif 1 <= as_num <= 64495 or 65536 <= as_num <= 4199999999:
            return "público"
        else:
            return "no válido (fuera de rangos conocidos)"
    except ValueError:
        return "no válido (no es un número)"

def main():
    print("Verificador de AS de BGP")
    print("========================")
    as_input = input("Ingrese el número de AS: ")
    
    resultado = verificar_as(as_input)
    print(f"El AS {as_input} es {resultado}")

if __name__ == "__main__":
    main()