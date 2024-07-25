# This is a test file for ToMiDevelop's tron_digits module.
# 
# The wiring of the lcd is decribed in the code itself.
#
# This example file was tested on a ESP-32 C3 Super Mini board
# Just like this one: https://pl.aliexpress.com/item/1005005967641936.html?spm=a2g0o.order_detail.order_detail_item.3.282e43ceH2adQV&gatewayAdapt=glo2pol
#
# Here also this module driver is used to operate the lcd: https://github.com/open-sorcerer64/i2c-lcd-pico
#
# More information can be found in ToMiDevelop's repo:
#
# Have fun and enjoy!

# Base modules import

from machine import Pin, SoftI2C
import utime

# External modules import

from pico_i2c_lcd import I2cLcd
from tron_digits import Tron

# Giving understandable names to functional pins and pin numbers

i2c_display_sda = 5
i2c_display_scl = 6

# Inicjalizacja wyświetlacza

# Zdefiniowanie adresu i2c wyświetlacza i jego rozmiarów

i2c_addr = 0x27
i2c_rows = 2
i2c_cols = 16

# Initialisation of i2c connection and the lcd display instance

i2c = SoftI2C(sda=Pin(5), scl=Pin(6), freq=400000)
lcd = I2cLcd(i2c, i2c_addr, i2c_rows, i2c_cols)

# Initialising Tron class instance

bigNumbers = Tron(lcd)

# The line bellow should be uncommented when using the tron_gigits module for the first time
#bigNumbers.seed_eeprom()
# Comment it again after the first usage

# Initial lcd message

lcd.clear()
lcd.move_to(0,0)
lcd.putstr('Tron digits')
utime.sleep_ms(150)
lcd.move_to(0,1)
lcd.putstr('Loop test')
utime.sleep_ms(2000)

# main app loop

while True:
    # Big digits 0, 1, 2 at places 0, 2, 4
    lcd.clear()
    bigNumbers.tron_0(0)
    utime.sleep_ms(100)
    bigNumbers.tron_1(2)
    utime.sleep_ms(100)
    bigNumbers.tron_2(4)
    utime.sleep(3)
    # Big digits 3, 4, 5 at places 1, 3, 5
    lcd.clear()
    bigNumbers.tron_3(1)
    utime.sleep_ms(100)
    bigNumbers.tron_4(3)
    utime.sleep_ms(100)
    bigNumbers.tron_5(5)
    utime.sleep(3)
    # Big digits 6, 7, 8, 9 at places 0, 2, 4, 6
    lcd.clear()
    bigNumbers.tron_6(0)
    utime.sleep_ms(100)
    bigNumbers.tron_7(2)
    utime.sleep_ms(100)
    bigNumbers.tron_8(4)
    utime.sleep_ms(100)
    bigNumbers.tron_9(6)
    utime.sleep(3)