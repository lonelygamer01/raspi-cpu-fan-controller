import time

def get_temp():
    # Log teh cpu fan Celsius
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        return int(f.read()) / 1000

def set_fan_speed(speed):
    # Set the fanspeed (0-255).
    try:
        # this folder might be different hwmon2 / hwmon1 ect.
        with open("/sys/class/hwmon/hwmon2/pwm1", "w") as f:
            f.write(str(speed))
    except Exception as e: print(e)

FAN_SPEEDS = [
    (35, 30),   # 35C - 30%
    (45, 50),   # 45C - 50%
    (50, 60),   # 50C - 60%
    (55, 80),   # 55C - 80%
    (60, 100)   # 60C - 100%
]

while True:
    temp = get_temp()
    speed = 0

    for t, s in FAN_SPEEDS:
        if temp >= t:
            speed = s
    # Conver 0-255 to 100%
    set_fan_speed(int(speed * 2.55))
    
    time.sleep(5)
