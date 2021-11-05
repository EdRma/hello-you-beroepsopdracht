from microbit import *

while True:
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
    if button_a.was_pressed():
        display.scroll('HELLO!')
        sleep(1000)
        display.show(Image.HAPPY)
        sleep(2000)
    elif button_b.was_pressed():
        display.scroll('hello...')
        sleep(1000)
        display.show(Image.ASLEEP)
        sleep(2000)