import board
import digitalio

vext_en = digitalio.DigitalInOut(board.VEXT_EN)
vext_en.direction = digitalio.Direction.OUTPUT

def enable_power(value = True):
    vext_en.value = not value

bat_sens_en = digitalio.DigitalInOut(board.BAT_SENS_EN)
bat_sens_en.direction = digitalio.Direction.OUTPUT

def enable_bat_sens(value = True):
    bat_sens_en.value = not value
