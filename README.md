# DFRobot SEN0539 Micro/CircuitPython

<img src="/Images/board.png" width=30%>

![](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white) ![](https://img.shields.io/badge/adafruit-000000?style=for-the-badge&logo=adafruit&logoColor=white) ![](https://img.shields.io/badge/espressif-%23E7352C.svg?&style=for-the-badge&logo=espressif&logoColor=white)



Modification of the library for DFRobot's SEN0539 (DF2301Q) Voice Recognition module to MicroPython and CircuitPython for use with the Raspberry Pi Pico (RP2040)

Code was modified from DFRobot's ( https://github.com/DFRobot/DFRobot_DF2301Q ) Raspberry Pi Python code to work with both CircuitPython and MicroPython. UART code was not included because I only needed I2C and so didn't bother porting the UART interface. This was a fast conversion so there's bound to be bugs and things done incorrectly, but I saw quite a few people online looking for this and figured I might be able to speed up someone's project.

## Product Link

- [DFRobot Store](https://www.dfrobot.com/product-2665.html)
- [DigiKey 🇨🇦](https://www.digikey.ca/en/products/detail/dfrobot/SEN0539-EN/20500165) 
- [Amazon 🇨🇦](https://www.amazon.ca/Gravity-Language-Learning-Recognition-Raspberry/dp/B0C5XG3BXW)

## Compatability

| Board | Working | Not Working | Not Tested |
| ----------- | ----------- | ----------- | ----------- |
| Raspberry Pi Pico | ✅ |  |  |
| BBC micro:bit |  |  | ✅ |
| Any ESP8266 |  |  | ✅ |
| Any ESP32 |  |  | ✅ | 

## Usage

### Summary

- This library can be used to both send commands to, and read command IDs from the DFRobot Gravity speech recognition board.
- Possible operations include setting wake (listening) state duration, muting/unmuting the board, setting volume, entering wake (listening) state, and reseting the module.
- Reading from the module gives an integer corresponding to the Command IDs which are described here ( https://wiki.dfrobot.com/SKU_SEN0539-EN_Gravity_Voice_Recognition_Module_I2C_UART )

### Installation

- Include the `DFRobot_DF2301Q.py` file alongside your code. Examples of how to use this library are included in `code.py` for CircuitPython and `main.py` for MicroPython.

## Credits

Original code written by qsjhyy ( yihuan.huang@dfrobot.com ), 2022. Conversion by Mason Plested ( https://github.com/MasonPles ), 2023.

