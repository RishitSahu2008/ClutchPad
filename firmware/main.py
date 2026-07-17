import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.scanners import DiodeOrientation
# from kmk.modules.layers import Layers - only useful when layers needed
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.display import Display, TextEntry

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP1,board.GP2,board.GP4)
keyboard.row_pins = (board.GP28,board.GP29,board.GP0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.GP26,board.GP27))
encoder_handler.map = ((KC.VOLD, KC.VOLU))

rgb = RGB(
    pixel_pin=board.GP3, num_pixels=9, val_limit=144, animation_mode=AnimationModes.STATIC
)

keyboard.keymap = [
    [KC.Q , KC.W , KC.E ,
     KC.A , KC.S , KC.D ,
     KC.Z , KC.R , KC.C 
     ]
]

disp = Display(display=SSD1306(sda = board.GP6, scl = board.GP7),
               entries=[TextEntry(text='Ready to clutch.'),],
    height=70,)
keyboard.extensions.append(disp)
if __name__ == '__main__':
    keyboard.go()
