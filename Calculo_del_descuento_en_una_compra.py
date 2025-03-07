#Entrada
Compra=int(input("Ingrese el monto de la compra"))
if(Compra<50):
    print("Descuento aplicado:",f"${0}")
    print("Total a pagar:",f"${Compra}")
elif(50<Compra<=100):
    print("Descuento aplicado:",f"${(Compra*0.05)}")
    print("Total a pagar:",f"${Compra-(Compra*0.05)}")
else:
    print("Descuento aplicado:",f"${(Compra*0.10)}")
    print("Total a pagar:",f"${Compra-(Compra*0.10)}")