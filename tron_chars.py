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

class font_tron: # all credits to upiir: https://github.com/upiir/character_display_big_digits
    
    # In this set there are 2 standard character - empty and full and a set of custom ones defined
    # as bytearrays, which can be saved to the LCD's eeprom to create big digits all beeing
    # 2 x 2 characters. Bellow there is a map for ach character from 0 to 9.
    #
    # Map:
    #
    # 0
    # c4 c2
    # c7 full
    #
    # 1
    # empty c5
    # empty c5
    #
    # 2 
    # c0 c2
    # c3 c6
    #
    # 3
    # c0 c2
    # c1 full
    #
    # 4
    # c7    c1
    # empty c5
    #
    # 5
    # c3 c6
    # c6 full
    #
    # 6
    # c3 c6
    # c3 full
    #
    # 7
    # c0    c2
    # empty c5
    #
    # 8
    # c3 c2
    # c3 full
    #
    # 9
    # c3    c2
    # empty c2
        
    empty = chr(254)
    full = chr(255)
    c0 = bytearray(
        [
            0x1f,
            0x18,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00
        ]
    )
    c1 = bytearray(
        [
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x18,
            0x1F
        ]
    )
    c2 = bytearray(
        [
            0x1F,
            0x03,
            0x03,
            0x03,
            0x03,
            0x03,
            0x03,
            0x03
        ]
    )
    c3 = bytearray(
        [
            0x1F,
            0x18,
            0x18,
            0x18,
            0x18,
            0x18,
            0x18,
            0x1F
        ]
    )
    c4 = bytearray(
        [
            0x1F,
            0x18,
            0x18,
            0x18,
            0x18,
            0x18,
            0x18,
            0x18
        ]
    )
    c5 = bytearray(
        [
            0x18,
            0x18,
            0x18,
            0x18,
            0x18,
            0x18,
            0x18,
            0x18
        ]
    )
    c6 = bytearray(
        [
            0x1F,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x1F
        ]
    )
    c7 = bytearray(
        [
            0x18,
            0x18,
            0x18,
            0x18,
            0x18,
            0x18,
            0x18,
            0x1F
        ]
    )