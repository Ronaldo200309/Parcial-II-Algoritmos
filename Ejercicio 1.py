def contar_a(cadena):
    
    cadena = cadena.lower()
   
    return cadena.count('a')


texto = "Aprendiendo a PROGRAMAR Algo"
resultado = contar_a(texto)
print(f"Cantidad de 'a' o 'A': {resultado}")


