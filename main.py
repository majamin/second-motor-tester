def on_button_pressed_a():
    motion.drive_straight(50)
    basic.pause(2000)
    motion.turn_left(50)
    basic.pause(2000)
    motion.turn_right(50)
    basic.pause(2000)
    motion.stop()
    basic.pause(2000)
input.on_button_pressed(Button.A, on_button_pressed_a)
