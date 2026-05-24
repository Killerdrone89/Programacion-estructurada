def borrarPantalla():
    print("\033c")

def ventaAutos(opc, autos, acum_pv):
    borrarPantalla()
    while opc == "S":
        marca = input("Marca: ").strip().upper()
        origen = input("Origen: ").strip().upper()
        costo = float(input("Costo: "))

        impuesto = 0
        if origen == "ALEMANIA":
            impuesto = 0.20
        elif origen == "JAPON":
            impuesto = 0.30
        elif origen == "ITALIA":
            impuesto = 0.15
        elif origen == "USA":
            impuesto = 0.08
        else:
            impuesto = 0

        impuesto_peso = costo * impuesto
        pv = impuesto_peso + costo
        autos += 1
        acum_pv += pv
        print(f"El impuesto a pagar es: ${impuesto_peso}\nEl precio de venta es: ${pv}")
        opc = input("¿Deseas realizar otra vez el proceso? (S/N): ").strip().upper()
        print("\033c")
        
    return autos, acum_pv

OPC = "S"
AUTOS = 0
ACUM_PV = 0

tot_autos, acum_precios = ventaAutos(OPC, AUTOS, ACUM_PV)

print(f"El total de los vehículos ingresados es: {tot_autos}\nY el monto total de los precios de venta es: {acum_precios}")
input()
print("\033c")