#!/bin/python3
# script de python para calcular la conversion de m3 a kw de gas natural
# conversion de bash a python
# script de calculo y conversion de m3 a kwh
# el valor predeterminado aproximado es el siguiente:
# 1 m3 = 11,70 kwh
# 1 kwh = 0.8547008547008547008 m3
import math # importamos la libreria math
def m3_to_kwh(): # definimos la funcion m3_to_kwh
    m3_gas = float(input("Introduce los m3 de gas natural: ")) # pedimos los m3 de gas natural
    kwh_gas = m3_gas * 11.70 # calculamos los kwh de gas natural
    print("El valor de los m3 de gas natural es: ", kwh_gas, "kwh")    # mostramos el resultado
# conversion ahora de kwh a m3
    kwh_gas = float(input("Introduce los kwh de gas natural: ")) # pedimos los kwh de gas natural
    m3_gas = kwh_gas * 0.8547008547008547008 # calculamos los m3 de gas natural
    print("El valor de los kwh de gas natural es: ", m3_gas, "m3")   # mostramos el resultado
if __name__ == '__main__': # llamamos a la funcion
    m3_to_kwh() # llamamos a la funcion con el valor de 10
