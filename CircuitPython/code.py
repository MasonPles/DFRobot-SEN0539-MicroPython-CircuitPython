import board
import time
from DFRobot_DF2301Q import DFRobot_DF2301Q_I2C

# Example CircuitPython code, should print command IDs when run. Only tested on RPI Pico WH. 

df2301q = DFRobot_DF2301Q_I2C(scl=board.GP17, sda=board.GP16) # Pins default to GP17, GP16 but can be specified otherwise

def setup():
    df2301q.set_volume(15) # Volume of the speaker onboard the SEN0539/DF2301Q, seems to be in the range 0-20? 
    df2301q.set_mute_mode(0) # 1 = mute, 0 = unmute
    df2301q.set_wake_time(20) # how long to stay in "listening" mode in seconds

    print("wake_time = %u\n" % df2301q.get_wake_time())

    # Uncomment the line below to play the wake-up command
    #df2301q.play_by_CMDID(1)

    # Play a common word ID (for example, 23)
    df2301q.play_by_CMDID(23)

def loop():
    CMDID = df2301q.get_CMDID() # get_CMDID() returns integer corresponding to the Command Words/Wake-up Words ID Table (https://wiki.dfrobot.com/SKU_SEN0539-EN_Gravity_Voice_Recognition_Module_I2C_UART) 
    if CMDID != 0:
        print("CMDID = %u\n" % CMDID)
    time.sleep(1)

if __name__ == "__main__":
    setup()
    while True:
        loop()
