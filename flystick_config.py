"""
This "demo" configuration is for the most spartanly-named
"Thrustmaster USB Joystick" (http://www.thrustmaster.com/products/usb-joystick).
It was the cheapest joystick in my local electronics shop, and - as an added
bonus - it had just the throttle lever I wanted.
"""
from flystick_conf_models import *

stick = Joystick(0)
stick = joystick(1)

# Raspberry Pi GPIO pin where to output the PPM signal.
# Pin map: http://wiki.mchobby.be/images/3/31/RASP-PIZERO-Correspondance-GPIO.jpg
# (Connect this pin to the RC transmitter trainer port.)
PPM_OUTPUT_PIN = 18

# Output (PPM) channels.
CHANNELS = (
    # channel 1: aileron with trim
    stick.axis(0) ,
    # a more elaborate example with reverse, offset, weight and trim:
    #(-stick.axis(0) + 0.1) * 0.7 + ail_trim * 0.5,
    # channel 2: elevator (reversed)
    -stick.axis(1),
    # channel 3: throttle (reversed)
    -stick.axis(2),
    # channel 4: flight mode
    # hat up-down axis, 5 states to match scrollphat vertical resolution
    stick.hat_switch(hat=0, axis=1, positions=5),
    # channels 5-8: buttons demo
    stick.button(0),
    stick.button(1),
    stick.button(2),
    stick.button(3),
)

