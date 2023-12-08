import time
import board
import busio

DF2301Q_I2C_ADDR = 0x64
DF2301Q_I2C_REG_CMDID = 0x02
DF2301Q_I2C_REG_PLAY_CMDID = 0x03
DF2301Q_I2C_REG_SET_MUTE = 0x04
DF2301Q_I2C_REG_SET_VOLUME = 0x05
DF2301Q_I2C_REG_WAKE_TIME = 0x06
DF2301Q_I2C_MSG_TAIL = 0x5A

class DFRobot_DF2301Q:
    def __init__(self):
        pass

class DFRobot_DF2301Q_I2C(DFRobot_DF2301Q):
    def __init__(self, i2c_addr=DF2301Q_I2C_ADDR, scl=board.GP17, sda=board.GP16):
        self._addr = i2c_addr
        self._i2c = busio.I2C(scl, sda)
        while not self._i2c.try_lock():
            pass
        super(DFRobot_DF2301Q_I2C, self).__init__()

    def get_CMDID(self):
        time.sleep(0.05)
        return self._read_reg(DF2301Q_I2C_REG_CMDID)

    def play_by_CMDID(self, CMDID):
        self._write_reg(DF2301Q_I2C_REG_PLAY_CMDID, CMDID)
        time.sleep(1)

    def get_wake_time(self):
        return self._read_reg(DF2301Q_I2C_REG_WAKE_TIME)

    def set_wake_time(self, wake_time):
        wake_time = wake_time & 0xFF
        self._write_reg(DF2301Q_I2C_REG_WAKE_TIME, wake_time)

    def set_volume(self, vol):
        self._write_reg(DF2301Q_I2C_REG_SET_VOLUME, vol)

    def set_mute_mode(self, mode):
        if mode != 0:
            mode = 1
        self._write_reg(DF2301Q_I2C_REG_SET_MUTE, mode)

    def _write_reg(self, reg, data):
        if isinstance(data, int):
            data = [data]
        self._i2c.writeto(self._addr, bytes([reg] + data))

    def _read_reg(self, reg):
        data = bytearray(1)
        self._i2c.writeto_then_readfrom(self._addr, bytes([reg]), data)
        return data[0]
    

