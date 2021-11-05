# Add your Python code here. E.g.
from microbit import *
BOAT= Image('00999:90099:00999:90099:00999')
while True:
    display.scroll('HELLO YOU')
    display.show(Image.HEART)
    sleep(3000)
    if button_a.was_pressed():
        display.scroll('Edgar Rikkert')
    elif button_b.was_pressed():
          display.show(BOAT)
          sleep(2000)