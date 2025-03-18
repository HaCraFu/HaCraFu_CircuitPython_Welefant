import board
import neopixel
from adafruit_pixel_framebuf import PixelFramebuffer

pixels_m = neopixel.NeoPixel(board.LED_MATRIX, 20, brightness=0.05, auto_write=False)

matrix = PixelFramebuffer(
    pixels_m,
    4,
    5,
    alternating=False,
)
