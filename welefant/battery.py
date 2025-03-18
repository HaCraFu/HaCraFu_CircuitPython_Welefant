import welefant
import analogio
import board
welefant.enable_bat_sens(True)

from adafruit_simplemath import map_range

battery_pin = analogio.AnalogIn(board.BAT_SENS)

def voltage():
    return 4.9 * ((battery_pin.value/65535)*battery_pin.reference_voltage)

def level():
    return map_range(voltage(), 3.3, 4.1, 0, 100)
