#!/bin/bash
# script de calculo y conversion de m3 a kwh
# el valor predeterminado aproximado es el siguiente:
# 1 m3 = 11,70 kwh
# 1 kwh = .08547008547008547008 m3
#calculamos el valor de m3 a kwh
echo "Introduce el valor de m3"
read m3
kwh=$(echo "scale=2; $m3 * 11.70" | bc)
echo "El valor de $m3 m3 es $kwh kwh aproximadamente"
#calculamos el valor de kwh a m3
echo "Introduce el valor de kwh"
read kwh
m3=$(echo "scale=2; $kwh * 0.8547008547008" | bc)
echo "El valor de $kwh kwh es $m3 m3 aproximadamente"

