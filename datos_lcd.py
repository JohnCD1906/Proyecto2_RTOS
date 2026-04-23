import board
import busio
import pigpio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# --- Configuración de Pines ---
PIN_MOTOR = 17  # Pin donde entra la señal PWM del motor
PIN_SERVO = 27  # Pin donde entra la señal PWM del servo

# --- Inicialización pigpio (Lectura de Pulsos) ---
pi = pigpio.pi()
if not pi.connected:
    exit()

# Variables globales para almacenar anchos de pulso
pw_motor = 0
pw_servo = 0

def cb_motor(gpio, level, tick):
    global pw_motor
    if level == 1: self.start_tick = tick
    else: pw_motor = pigpio.tickDiff(self.start_tick, tick)

# Usaremos una clase simple para manejar la lectura de PWM
class PWM_Reader:
    def __init__(self, pi, gpio):
        self.pi = pi
        self.gpio = gpio
        self.high_tick = None
        self.period = None
        self.high_time = 0
        self.cb = pi.callback(gpio, pigpio.EITHER_EDGE, self._cbf)

    def _cbf(self, gpio, level, tick):
        if level == 1:
            if self.high_tick is not None:
                self.period = pigpio.tickDiff(self.high_tick, tick)
            self.high_tick = tick
        elif level == 0:
            if self.high_tick is not None:
                self.high_time = pigpio.tickDiff(self.high_tick, tick)

    def get_duty_cycle(self):
        if self.period:
            return (self.high_time / self.period) * 100
        return 0

    def get_pulse_width(self):
        return self.high_time

# Instanciar lectores
lector_motor = PWM_Reader(pi, PIN_MOTOR)
lector_servo = PWM_Reader(pi, PIN_SERVO)

# --- Inicialización OLED ---
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
font = ImageFont.load_default()

try:
    while True:
        # 1. Procesar Datos
        # Para el motor: Supongamos que 100% duty = 5000 RPM
        duty_motor = lector_motor.get_duty_cycle()
        rpm = int(duty_motor * 50) 

        # Para el servo: 1000us = 0°, 2000us = 180°
        pw = lector_servo.get_pulse_width()
        angulo = max(0, min(180, (pw - 1000) * 180 / 1000))

        # 2. Dibujar en OLED
        image = Image.new("1", (128, 64))
        draw = ImageDraw.Draw(image)
        
        draw.text((0, 0),  "MONITOR DE MOTORES", font=font, fill=255)
        draw.text((0, 20), f"Motor: {rpm} RPM", font=font, fill=255)
        draw.text((0, 30), f"Duty: {duty_motor:.1f}%", font=font, fill=255)
        draw.text((0, 40), f"Servo: {angulo:.1f} deg", font=font, fill=255)
        
        oled.image(image)
        oled.show()

except KeyboardInterrupt:
    pi.stop()