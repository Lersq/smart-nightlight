from machine import Pin, ADC
import time

# 30% от 4095 (максимума)
THRESHOLD = 4095 / 100 * 30

# светодиод
led = Pin(4, Pin.OUT)

# фоторезистор
ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

try:
    # вечный цикл
    while True:
        # чтение значения фоторезистора
        ldr_value = ldr.read()
        
        # проверка значения фоторезистора
        if ldr_value <= THRESHOLD:
            led.value(1)
        else:
            led.value(0)
        
        # задержка в 100 мс
        time.sleep_ms(100)
        
# действия при любом завершении программы
finally:
    # выключение светодиода
    led.value(0)