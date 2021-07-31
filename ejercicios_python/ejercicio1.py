def aplica_IVA(subtotal):
    iva = subtotal*float(0.16)
    return iva


def aplica_descuento(producto,precio):

    if producto == 'Agua':
        precio = precio-(precio*float(0.1))
        return precio
    elif producto == 'Tortillas':
        precio = precio-(precio*float(0.2))
        return precio
    else:
        return precio


def inicia_precios():
    precios = {
        'Leche':24,
        'Agua':15,
        'Canela':2,
        'Huevo':40,
        'Tortillas':20
    }
    
    return precios


def run():
    try:
        precios = inicia_precios()

        print('Los productos y precios disponibles son los siguientes: ')
        i=0

        keys = list(precios.keys())
        values = list(precios.values())
        
        for producto,precio in precios.items():
            print(f'{i}.-{producto}: ${precio} MXN')
            i+=1
            
        seleccion = input('Ingresa lo que quieres comprar, para salir escribe "Q"\n =>')
        cesta = {}

        while seleccion != "Q":
            cesta[keys[int(seleccion)]] = values[int(seleccion)]
            seleccion = input('Ingresa nuevo producto, para salir escribe "Q" \n =>')

        subtotal=0

        for producto,precio in cesta.items():
            sub = aplica_descuento(producto,float(precio))
            subtotal +=sub

        iva = aplica_IVA(float(subtotal))

        total = subtotal + iva

        print(f'''El total de tu compra es:\n
        subtotal: {subtotal}\n
        IVA: {iva} \n
        Total: {total}
        ''')
    except:
        print('Se ingresó un valor incorrecto')

if __name__ == "__main__":
    run()
