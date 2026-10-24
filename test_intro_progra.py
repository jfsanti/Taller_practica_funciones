print("""  MENU PRINCIPAL
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir
""")
      
saldo = 1000

Consultar_saldo = 1
Depositar_dinero = 2
Retirar_dinero = 3
Salir = 4

def new_saldo(saldo, abono):
    nuevo_saldo = saldo + abono
    return nuevo_saldo

def left_saldo(saldo, retiro):
    saldo_actual = saldo - retiro
    return saldo_actual



while True:
    print("\nQué desea realizar?")
    eleccion = int(input(": "))
    if eleccion == 1:
        print("Saldo actual: $", saldo)
    elif eleccion == 2:
        print("\nCuánto desea depositar?")
        abono = int(input(": $"))
        if abono > 0:
            saldo = new_saldo(saldo, abono)
            print("Nuevo saldo: ", saldo)
        else:
            print("Deposito invalido")
    elif eleccion == 3:
        print("\nCuánto desea retirar")
        retiro = int(input(": $"))
        if retiro > 0:
            saldo = left_saldo(saldo, retiro)
            print("Nuevo saldo: ", saldo)
        elif retiro < saldo:
            print("Saldo insuficiente")
        else:
            print("Retiro invalido")
    elif eleccion == 4:
        print("\n==== operacion terminada ====\n")
        break