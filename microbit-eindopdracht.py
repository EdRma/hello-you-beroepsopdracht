graden = 0

def on_button_pressed_a():
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(349, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(330, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(294, music.beat(BeatFraction.QUARTER))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(349, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(330, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(349, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(294, music.beat(BeatFraction.QUARTER))
    music.play_tone(294, music.beat(BeatFraction.QUARTER))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(247, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(247, music.beat(BeatFraction.HALF))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.play_tone(247, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    basic.pause(400)
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.play_tone(247, music.beat(BeatFraction.HALF))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global graden
    graden = input.compass_heading()
    if graden < 45 or graden > 315:
        basic.show_string("N")
    elif graden < 135:
        basic.show_string("O")
    elif graden < 225:
        basic.show_string("Z")
    else:
        basic.show_string("W")
basic.forever(on_forever)