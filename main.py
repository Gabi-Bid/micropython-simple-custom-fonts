from machine import Pin, I2C
import micropython
import ssd1306

# --- Fonts
from Fonts.BoldTiny import BoldTiny

# --- Setup I2C and OLED ---
i2c = I2C(0, scl=Pin(6), sda=Pin(5), freq=400000)
oled = ssd1306.SSD1306_I2C(72, 40, i2c)

# --- Draw text ---
@micropython.native # Extra perfomance boost
def draw_text(oled, x, y, text, font_dict, spacing=1):
    pixel = oled.pixel

    for c in text:
        bitmap = font_dict.get(c, font_dict.get(' ', []))
        if not bitmap:
            continue

        height = len(bitmap)
        width = len(bitmap[0])

        for row in range(height):
            line = bitmap[row]
            for col in range(width):
                # Only call pixel if '1'
                if line[col] == '1':
                    pixel(x + col, y + row, 1)
        x += width + spacing

# --- Example ---
while True: 
    oled.fill(0)
    draw_text(oled, 0, 0, "Hello World!", BoldTiny)
    draw_text(oled, 0, 10, "123456789", BoldTiny)
    oled.show()

