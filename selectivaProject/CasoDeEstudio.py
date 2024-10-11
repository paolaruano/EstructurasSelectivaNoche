#DEFINIR CONSTANTES
PRECIO_SENCILLA = 20000
PRECIO_DOBLE = 25000
PRECIO_TRIPLE = 28000
IMPUESTO_TARJETA = 0.07

#FUNCION PARA CALCULAR EL PRECIO
def calcular_precio(tipo_hambuegesa,medio_pago, cantidad):
    #Definir precio segun el tipo de hambuerguesa
    if tipo_hambuegesa == 1:
        precio = PRECIO_SENCILLA
        descripcion = 'Sencilla'
    elif tipo_hambuegesa == 2:
        precio = PRECIO_DOBLE
        descripcion = 'Doble'
    elif tipo_hambuegesa == 3:
        precio = PRECIO_TRIPLE
        descripcion = 'Triple'
    else:
        return None  # Tipo de hamburguesa inválido

    #Calcular el total sin cargos
    total_sin_cargos = precio*cantidad

    #Aplicar impuesto si el medio de pago es tarjeta
    if medio_pago ==1:
        impuesto = round(total_sin_cargos * IMPUESTO_TARJETA)
    else:
        impuesto = 0

    total = round(total_sin_cargos + impuesto)

    #Retornar datos relevantes
    return descripcion, precio,cantidad,impuesto,total

# Funcionar para generar mensaje
def generar_mensaje(descripcion, precio, cantidad, impuesto, total):
    return (f"Tipo de Hambuerguesa: {descripcion} \n"
            f"Precio: ${precio}\n"
            f"Cantidad: {cantidad}\n"
            f"Impuesto: ${impuesto}\n"
            f"Total: ${total}")

#Funcion para validar los datos
def validar_datos(tipo_hambuerguesa,medio_pago,cantidad):
    if 1 <= tipo_hambuerguesa <= 3 and 1 <= medio_pago <= 2 and cantidad > 0:
        resultado = calcular_precio(tipo_hambuerguesa,medio_pago,cantidad)
        #print ("Resultado: ", resultado)
        descripcion,precio,cantidad,impuesto,total=resultado
        mensaje = generar_mensaje(descripcion,precio,cantidad,impuesto,total)
        print("--------------------------\n"+mensaje)
    else:
        print("Varifique las opciones ingresadas")

#Entradas
tipo_hamburguesa = int(input ("Ingrese el tipo de hambuerguesa \n1. Sencilla \n2. Doble \n3. Triple \n"))
medio_pago = int (input("Ingrese medio de pago \n1. Tarjeta \n2. Otro \n "))
cantidad = int(input("Ingrese la cantidad: "))

#Salidas
validar_datos(tipo_hamburguesa, medio_pago, cantidad)
