import RPi.GPIO as GPIO
import time

# Configuracion de pin GPIO
SERVO_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Configuracion PWM
pwm_frequency = 50  # [Hz] de acuerdo con la hoja de datos
pwm = GPIO.PWM(SERVO_PIN, pwm_frequency)
pwm.start(0)

def set_servo_angle(angle):
    duty_cycle = (angle / 9) + 2.5
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)  # Tiempo de retardo para que el servo alcance la posicion solicitada

try:
    # Rotar servo de 0 a 180 [deg] con paso +1[deg]
    for angle in range(90, -91, -10):
        set_servo_angle(angle)

    # Rotar servo de 180 to 0 [deg] con paso -1[deg]
    for angle in range(-90, 91, 10):
        set_servo_angle(angle)

except KeyboardInterrupt:
    # Detener el programa y limpiar el GPIO al interrumpir el programa con ctrl + c
    pwm.stop()
    GPIO.cleanup()
