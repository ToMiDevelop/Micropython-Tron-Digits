# In this file you'll find functions which print big tron font digits
# each digit is a 2 x 2 characters object printed at on of the 8 (or 10) places.
# It is understood that each place numbered from 0 to 7 and mapped on x axis like this:
# characters 0,  1  - place 0
# characters 2,  3  - place 1
# characters 4,  5  - place 2
# characters 6,  7  - place 3
# characters 8,  9  - place 4
# characters 10, 11 - place 5
# characters 12, 13 - place 6
# characters 14, 15 - place 7
#
# The seed_eeprom function should be used only once, at the moment of first using the code
# with this library on your device. This way we preserve writing cycles of eeprom bulit into the
# character lcd's controler chip.
#
# Functions tron_0, tron_1, tron_2, ..., tron_9 are resoinsible for printing repectively
# digit 0, 1, 2, ..., 9.
# They all require _position argument which the place number briefly described at the top.
#
# This module contains two files:
# tron_digits.py and tron_chars.py.
# 
# The second file is a dependcy of the first one - contains bytearray definitions of small individual characters
# used to construct big 2 x 2 digits which are printed to the lcd by the functions from this module.
#
# This module also assumes you're using a module driver to operate the charcter lcd very similar to the way it's
# done here: https://github.com/open-sorcerer64/i2c-lcd-pico.
# Especially that it uses move_to, put_char and custom_char functions.
# From the technical poimt of view the _lcd argument of initialising the class from this module is an instance
# of the charcter lcd operation class used by the driver module of your choice and must provide functions mentioned
# above.
#
# Furtheromore there is an example code in tron_example.py file provided with an example usage of this module.
#
# Have Fun!
#
# LEGAL NOTICE
#
# The author of this library - ToMiDevelop makes it publicly availalabe based on the MIT license.
#
# License of this module:
#
# Copyright (c) 2024 ToMiDevelop
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# CREDITS
# 
# All credits connected with the font implemented here and idea of programing it with the usage
# of character dislays go to
# upiir: https://github.com/upiir/character_display_big_digits
#
# All for made publicly available in pointed upiir's repository is also published on MIT license.
# More details can be found in upiir's repository.

from tron_chars import font_tron

class Tron:
    def __init__(self, _lcd):
        self.lcd = _lcd
        self.empty = font_tron.empty
        self.full = font_tron.full   
    #
    def seed_eeprom(self):
        custom_chars = [
            font_tron.c0,
            font_tron.c1,
            font_tron.c2,
            font_tron.c3,
            font_tron.c4,
            font_tron.c5,
            font_tron.c6,
            font_tron.c7
        ]
        for i, char in enumerate(custom_chars):
            self.lcd.custom_char(i, char)
    #
    def tron_0 (self, _position):
        x = 0
        if _position == 0:
            x = 0
        if _position == 1:
            x = 2
        if _position == 2:
            x = 4
        if _position == 3:
            x = 6
        if _position == 4:
            x = 8
        if _position == 5:
            x = 10
        if _position == 6:
            x = 12
        if _position == 7:
            x = 14
        self.lcd.move_to(x,0)
        self.lcd.putchar(chr(4))
        self.lcd.move_to(x+1,0)
        self.lcd.putchar(chr(2))
        self.lcd.move_to(x,1)
        self.lcd.putchar(chr(7))
        self.lcd.move_to(x+1,1)
        self.lcd.putchar(self.full)
    #
    def tron_1 (self, _position):
        x = 0
        if _position == 0:
            x = 0
        if _position == 1:
            x = 2
        if _position == 2:
            x = 4
        if _position == 3:
            x = 6
        if _position == 4:
            x = 8
        if _position == 5:
            x = 10
        if _position == 6:
            x = 12
        if _position == 7:
            x = 14
        self.lcd.move_to(x,0)
        self.lcd.putchar(self.empty)
        self.lcd.move_to(x+1,0)
        self.lcd.putchar(chr(5))
        self.lcd.move_to(x,1)
        self.lcd.putchar(self.empty)
        self.lcd.move_to(x+1,1)
        self.lcd.putchar(chr(5))
    #
    def tron_2 (self, _position):
        x = 0
        if _position == 0:
            x = 0
        if _position == 1:
            x = 2
        if _position == 2:
            x = 4
        if _position == 3:
            x = 6
        if _position == 4:
            x = 8
        if _position == 5:
            x = 10
        if _position == 6:
            x = 12
        if _position == 7:
            x = 14
        self.lcd.move_to(x,0)
        self.lcd.putchar(chr(0))
        self.lcd.move_to(x+1,0)
        self.lcd.putchar(chr(2))
        self.lcd.move_to(x,1)
        self.lcd.putchar(chr(3))
        self.lcd.move_to(x+1,1)
        self.lcd.putchar(chr(6))
    #
    def tron_3 (self, _position):
        x = 0
        if _position == 0:
            x = 0
        if _position == 1:
            x = 2
        if _position == 2:
            x = 4
        if _position == 3:
            x = 6
        if _position == 4:
            x = 8
        if _position == 5:
            x = 10
        if _position == 6:
            x = 12
        if _position == 7:
            x = 14
        self.lcd.move_to(x,0)
        self.lcd.putchar(chr(0))
        self.lcd.move_to(x+1,0)
        self.lcd.putchar(chr(2))
        self.lcd.move_to(x,1)
        self.lcd.putchar(chr(1))
        self.lcd.move_to(x+1,1)
        self.lcd.putchar(self.full)
    #
    def tron_4 (self, _position):
        x = 0
        if _position == 0:
            x = 0
        if _position == 1:
            x = 2
        if _position == 2:
            x = 4
        if _position == 3:
            x = 6
        if _position == 4:
            x = 8
        if _position == 5:
            x = 10
        if _position == 6:
            x = 12
        if _position == 7:
            x = 14
        self.lcd.move_to(x,0)
        self.lcd.putchar(chr(7))
        self.lcd.move_to(x+1,0)
        self.lcd.putchar(chr(1))
        self.lcd.move_to(x,1)
        self.lcd.putchar(self.empty)
        self.lcd.move_to(x+1,1)
        self.lcd.putchar(chr(5))
    #
    def tron_5 (self, _position):
        x = 0
        if _position == 0:
            x = 0
        if _position == 1:
            x = 2
        if _position == 2:
            x = 4
        if _position == 3:
            x = 6
        if _position == 4:
            x = 8
        if _position == 5:
            x = 10
        if _position == 6:
            x = 12
        if _position == 7:
            x = 14
        self.lcd.move_to(x,0)
        self.lcd.putchar(chr(3))
        self.lcd.move_to(x+1,0)
        self.lcd.putchar(chr(6))
        self.lcd.move_to(x,1)
        self.lcd.putchar(chr(6))
        self.lcd.move_to(x+1,1)
        self.lcd.putchar(self.full)
    #
    def tron_6 (self, _position):
        x = 0
        if _position == 0:
            x = 0
        if _position == 1:
            x = 2
        if _position == 2:
            x = 4
        if _position == 3:
            x = 6
        if _position == 4:
            x = 8
        if _position == 5:
            x = 10
        if _position == 6:
            x = 12
        if _position == 7:
            x = 14
        self.lcd.move_to(x,0)
        self.lcd.putchar(chr(3))
        self.lcd.move_to(x+1,0)
        self.lcd.putchar(chr(6))
        self.lcd.move_to(x,1)
        self.lcd.putchar(chr(3))
        self.lcd.move_to(x+1,1)
        self.lcd.putchar(self.full)
    #
    def tron_7 (self, _position):
        x = 0
        if _position == 0:
            x = 0
        if _position == 1:
            x = 2
        if _position == 2:
            x = 4
        if _position == 3:
            x = 6
        if _position == 4:
            x = 8
        if _position == 5:
            x = 10
        if _position == 6:
            x = 12
        if _position == 7:
            x = 14
        self.lcd.move_to(x,0)
        self.lcd.putchar(chr(0))
        self.lcd.move_to(x+1,0)
        self.lcd.putchar(chr(2))
        self.lcd.move_to(x,1)
        self.lcd.putchar(self.empty)
        self.lcd.move_to(x+1,1)
        self.lcd.putchar(chr(5))
    #
    def tron_8 (self, _position):
        x = 0
        if _position == 0:
            x = 0
        if _position == 1:
            x = 2
        if _position == 2:
            x = 4
        if _position == 3:
            x = 6
        if _position == 4:
            x = 8
        if _position == 5:
            x = 10
        if _position == 6:
            x = 12
        if _position == 7:
            x = 14
        self.lcd.move_to(x,0)
        self.lcd.putchar(chr(3))
        self.lcd.move_to(x+1,0)
        self.lcd.putchar(chr(2))
        self.lcd.move_to(x,1)
        self.lcd.putchar(chr(3))
        self.lcd.move_to(x+1,1)
        self.lcd.putchar(self.full)
    #
    def tron_9 (self, _position):
        x = 0
        if _position == 0:
            x = 0
        if _position == 1:
            x = 2
        if _position == 2:
            x = 4
        if _position == 3:
            x = 6
        if _position == 4:
            x = 8
        if _position == 5:
            x = 10
        if _position == 6:
            x = 12
        if _position == 7:
            x = 14
        self.lcd.move_to(x,0)
        self.lcd.putchar(chr(3))
        self.lcd.move_to(x+1,0)
        self.lcd.putchar(chr(2))
        self.lcd.move_to(x,1)
        self.lcd.putchar(self.empty)
        self.lcd.move_to(x+1,1)
        self.lcd.putchar(chr(2))
    #