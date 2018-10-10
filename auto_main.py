import time

from pynput.keyboard import Key, Controller

keyboard = Controller()

keyboard.press(Key.cmd_r)
keyboard.release(Key.cmd_r)

time.sleep(0.01)

keyboard.press('e')
keyboard.release('e')
keyboard.press('d')
keyboard.release('d')
keyboard.press('g')
keyboard.release('g')
keyboard.press('e')
keyboard.release('e')

time.sleep(0.01)

keyboard.press(Key.enter)
keyboard.release(Key.enter)

from pynput.mouse import Button, Controller

mouse = Controller()

mouse.position = (450, 65)
mouse.click(Button.left)

time.sleep(0.01)

