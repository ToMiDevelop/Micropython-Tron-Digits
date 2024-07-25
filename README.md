# Micropython-Tron-Digits
A MicroPython application of Tron digits for charcter lcd's.

## 1. Prerequisites

This module is designed to be used with MicroPython on boards capable of using i2c communication protocol. So it can be freely used on example on

- Parpberry Pi Pico / Pico W,
- other RP2040 based boards
- ESP32 chps family based boards,
- ESP82866 based boards,
- others supporting MicroPython and I2C communication.

This module also assumes you're using a module driver (to operate the charcter lcd) very similar to the way it's
done [here](https://github.com/open-sorcerer64/i2c-lcd-pico).

Especially that your module driver uses **move_to**, **put_char** and **custom_char** functions.
From the technical poimt of view the _lcd argument of initialising the class from this module is an instance
of the charcter lcd operation class used by the driver module of your choice and must provide functions mentioned
above.

## 2. Functional idea description
In this module you'll find functions which print big tron font digits
each digit is a 2 x 2 characters object printed at on of the 8 (or 10) places.
It is understood that each place numbered from 0 to 7 and mapped on x axis like this:

- characters 0,  1  - place 0
- characters 2,  3  - place 1
- characters 4,  5  - place 2
- characters 6,  7  - place 3
- characters 8,  9  - place 4
- characters 10, 11 - place 5
- characters 12, 13 - place 6
- characters 14, 15 - place 7

## 3. Initialising the class to operate the module functions

A **Tron** from **tron_digits.py** must be initialised to use the provided functions.

It fairly simple, first we need an instance of the charaters lcd's operation class, lets assume it's called ```lcd```. Now we just initialise aour class like this

``` python
from tron_digits import Tron
TronInstance = Tron(lcd)
```

## 4. Provided functions description

### a) ```seed_eeprom()```

The seed_eeprom function should be used only once, at the moment of first usage ot this module on a certain display. This way we preserve writing cycles of eeprom bulit into the character lcd's controler chip.

### b) ```tron_n(_position)```, where n = 0...9

Functions
- ```tron_0(_position)```,
- ```tron_1(_position)```,
- ```tron_2(_position)```, 
- ...,
- ```tron_9(_position)```.
 
are responsible for printing repectively big 2x2 digits 0, 1, 2, ..., 9.

They all require ```_position``` argument which provides place number briefly described at **point 2**.

### c) Example usage

``` python
# other needed code block bellow
# ....
# ....
# ....
# ....
# other needed code block up

# Importing utime
import utime

# Importing Tron class
from tron_digits import Tron

# Initialisation of Tron class
TronInstance = Tron(lcd)

while True:
    # seedin display's eeprom
    lcd.clear()
    TronInstance.seed_eeprom()
    utime.sleep(2)
    # printing digit 4 at place 5
    lcd.clear()
    TronInstance.tron_4(5)
    utime.sleep(2)
```

## 5. Files in the module

### a) Module files

- tron_digits.py,
- tron_chars.py.
 
The second file is a dependcy of the first one and contains bytearray definitions of small individual characters
used to construct big 2 x 2 digits which are printed to the lcd by the functions from this module.

### b) More complex usage example

- tron_example.py

Here there is an example code provided with a little more complex usage of this module.

## 6. Legal notice

The author of this library - ToMiDevelop makes it publicly availalabe based on the MIT license.

License of this module:

Copyright (c) 2024 ToMiDevelop

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 7. Credits
 
All credits connected with the font implemented here and idea of programing it with the usage
of character dislays go to [upiir](https://github.com/upiir/character_display_big_digits).

All code and materials made publicly available in pointed **upiir's repository** is also published on MIT license.
More details can be found in **upiir's repository**.
