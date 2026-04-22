#!/bin/bash
#GPIO22

buzzer_pin=22
echo "$buzzer_pin" > /sys/class/gpio/export 2>/dev/null
sleep 0.1
echo "out" > /sys/class/gpio/gpio${buzzer_pin}/direction

echo "buzzer encendido" 

#Encender buzzer por 30 segundos
echo "1" > /sys/class/gpio/gpio${buzzer_pin}/value
sleep 30

#Apagar buzzer 
echo "0" > /sys/class/gpio/gpio${buzzer_pin}/value 
echo "buzzer apagado"

#liberar pin

echo "$buzzer_pin" > /sys/class/gpio/unexport 2>/dev/null

exit 0