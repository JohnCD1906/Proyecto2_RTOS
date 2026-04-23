import RPi.GPIO as GPIO
import time

# Configuracion de pin GPIO
MOTOR_DRIVER_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_DRIVER_PIN, GPIO.OUT)

# Configuracion PWM
pwm_frequency = 50  # [Hz] de acuerdo con la hoja de datos
pwm = GPIO.PWM(MOTOR_DRIVER_PIN, pwm_frequency)
pwm.start(0)

try:
    # Rotar servo de 0 a 180 [deg] con paso +1[deg]
    for speed in range(0, 101, 1):
        pwm.ChangeDutyCycle(speed)
        time.sleep(0.1)

    # Rotar servo de 180 to 0 [deg] con paso -1[deg]
    for speed in range(100, -1, -1):
        pwm.ChangeDutyCycle(speed)
        time.sleep(0.1)

except KeyboardInterrupt:
    # Detener el programa y limpiar el GPIO al interrumpir el programa con ctrl + c 
    pwm.stop()
    GPIO.cleanup()