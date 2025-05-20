def on_sound_loud():
    global lightsOn
    lightsOn = not (lightsOn)
    if lightsOn:
        basic.show_leds("""
            . # . # .
            . # . # .
            . # # # .
            . . # . .
            . # # # .
            """)
    else:
        basic.clear_screen()
input.on_sound(DetectedSound.LOUD, on_sound_loud)

lightsOn = False
input.set_sound_threshold(SoundThreshold.LOUD, 150)